import os
import requests
import datetime
import json

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    lessons = {
        1: "🇷🇺 Greetings\n\nПривет (ပရီ-ဗျက်)\nမင်္ဂလာပါ",
        2: "🇷🇺 Gratitude\n\nСпасибо (စပါ-စီး-ဗား)\nကျေးဇူးတင်ပါတယ်",
        3: "🇷🇺 Politeness\n\nПожалуйста (ပါ-ရှော-လ်စတာ)\nရပါတယ် / ကျေးဇူးပြု၍",
        4: "🇷🇺 Yes/No\n\nДа (ဒါး) - ဟုတ်ကဲ့\nНет (ညက်) - မဟုတ်ဘူး",
        5: "🇷🇺 Well-being\n\nКак дела? (ကပ် ဒီ-လား?)\nနေကောင်းလား?",
        6: "🇷🇺 Introductions\n\nМеня зовут... (မိ-ညာ ဇာ-ဗွတ်...)\nကျွန်တော့်နာမည်က... ပါ",
        29: "🇷🇺 Love\n\nЯ люблю тебя (ယာ လျူ-ဗလျူ တီ-ဗျာ)\nမင်းကို ချစ်တယ်",
        30: "🇷🇺 Good luck\n\nУдачи! (အူ-ဒါး-ချီ)\nကံကောင်းပါစေ!"
    }
    
    now = datetime.datetime.now()
    lesson_index = (now.minute // 5) + 1
    return lessons.get(lesson_index, lessons[1])

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    
    # ခလုတ်များ (Error ဖြစ်စေသော tel: ကို ဖယ်ရှားထားသည်)
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "💬 Viber Chat", "url": "https://viber.me/959693548605"},
                {"text": "📱 TikTok Channel", "url": "https://www.tiktok.com/@miorusskiy"}
            ]
        ]
    }

    # ဖုန်းနံပါတ်ကို စာသားထဲမှာ တိုက်ရိုက်နှိပ်လို့ရအောင် လုပ်ထားပေးသည်
    contact_info = (
        "<b>သင်တန်းအပ်ရန်နှင့် အသေးစိတ်စုံစမ်းရန်:</b>\n"
        "📞 ဖုန်းဖြင့်တိုက်ရိုက်ခေါ်ဆိုရန်: +959693548605\n"
        "(ဖုန်းနံပါတ်ကို နှိပ်၍ တိုက်ရိုက်ခေါ်ဆိုနိုင်ပါသည်)"
    )

    payload = {
        "chat_id": str(CHAT_ID).strip(),
        "text": f"{text}\n\n{contact_info}\n---\nMioRussianLanguage Center",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}, Response: {r.text}")

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
