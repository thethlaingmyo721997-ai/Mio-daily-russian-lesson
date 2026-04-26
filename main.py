import os
import requests
import datetime
import json

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    lessons = {
        1: "🇷🇺 Greetings\n\n<code>Word:\tПривет\t(ပရီ-ဗျက်)\nMeaning:\tမင်္ဂလာပါ</code>",
        2: "🇷🇺 Gratitude\n\n<code>Word:\tСпасибо\t(စပါ-စီး-ဗား)\nMeaning:\tကျေးဇူးတင်ပါတယ်</code>",
        3: "🇷🇺 Politeness\n\n<code>Word:\tПожалуйста\t(ပါ-ရှော-လ်စတာ)\nMeaning:\tရပါတယ်</code>",
        4: "🇷🇺 Yes/No\n\n<code>Word:\tДа\t(ဒါး)\nMeaning:\tဟုတ်ကဲ့\n\nWord:\tНет\t(ညက်)\nMeaning:\tမဟုတ်ဘူး</code>",
        5: "🇷🇺 Well-being\n\n<code>Word:\tКак дела?\t(ကပ် ဒီ-လား?)\nMeaning:\tနေကောင်းလား?</code>",
        29: "🇷🇺 Love\n\n<code>Word:\tЯ люблю тебя\t(ယာ လျူ-ဗလျူ တီ-ဗျာ)\nMeaning:\tချစ်တယ်</code>",
        30: "🇷🇺 Good luck\n\n<code>Word:\tУдачи!\t(အူ-ဒါး-ချီ)\nMeaning:\tကံကောင်းပါစေ!</code>"
    }
    
    now = datetime.datetime.now()
    lesson_index = (now.minute // 5) + 1
    return lessons.get(lesson_index, lessons[1])

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    
    # ခလုတ်ထဲမှာ TikTok ကိုပဲ ထားပါမည် (Error ကင်းစေရန်)
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "📱 TikTok Channel", "url": "https://www.tiktok.com/@miorusskiy"}
            ]
        ]
    }

    # Viber link ကို စာသားထဲမှာ တိုက်ရိုက်နှိပ်လို့ရအောင် ထည့်ထားပေးပါသည်
    # viber://chat?number=... format သည် App ကို တိုက်ရိုက်ပွင့်စေပါသည်
    viber_link = "viber://chat?number=959693548605"
    
    caption_text = (
        f"{text}\n\n"
        f"<b>စုံစမ်းရန်:</b>\n"
        f"💬 <a href='{viber_link}'>Viber App ဖြင့် တိုက်ရိုက်ဆက်သွယ်ရန် နှိပ်ပါ</a>\n"
        f"📞 Phone: +959693548605"
    )

    payload = {
        "chat_id": str(CHAT_ID).strip(),
        "text": f"{caption_text}\n---\nMioRussianLanguage Center",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}, Response: {r.text}")

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
