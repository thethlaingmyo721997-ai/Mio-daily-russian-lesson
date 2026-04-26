import os
import requests
import datetime
import json

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    # သင်ခန်းစာ ၃၀
    lessons = {
        1: "🇷🇺 Greetings\n\nПривет (ပရီ-ဗျက်)\nမင်္ဂလာပါ",
        2: "🇷🇺 Gratitude\n\nСпасибо (စပါ-စီး-ဗား)\nကျေးဇူးတင်ပါတယ်",
        # ... (ကျန်တဲ့ သင်ခန်းစာတွေလည်း ဒီအတိုင်းပဲ ဆက်သွားပါမယ်)
        29: "🇷🇺 Love\n\nЯ люблю тебя\nမင်းကို ချစ်တယ်",
        30: "🇷🇺 Good luck\n\nУдачи! (အူ-ဒါး-ချီ)\nကံကောင်းပါစေ!"
    }
    now = datetime.datetime.now()
    lesson_index = (now.minute // 5) + 1
    return lessons.get(lesson_index, lessons[1])

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    
    # ခလုတ်များ စီစဉ်မှု (Call Button ကို format ပြန်ညှိထားပါသည်)
    keyboard = {
        "inline_keyboard": [
            [
                # tel: နောက်မှာ // ထည့်ပြီး စမ်းသပ်ကြည့်ပါမည် (ဒါမှမဟုတ် စာသားထဲမှာ နံပါတ်မပါဘဲ ခလုတ်သက်သက်ပဲ ထားပါမည်)
                {"text": "📞 Direct Call", "url": "tel:09693548605"}, 
                {"text": "💬 Viber Chat", "url": "https://viber.me/959693548605"}
            ],
            [
                {"text": "📱 TikTok Channel", "url": "https://www.tiktok.com/@miorusskiy"}
            ]
        ]
    }

    payload = {
        "chat_id": str(CHAT_ID).strip(),
        "text": f"{text}\n\n<b>သင်တန်းအပ်ရန်နှင့် အသေးစိတ်စုံစမ်းရန် အောက်ကခလုတ်များကို နှိပ်ပါ-</b>\n---\nMioRussianLanguage Center",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}, Response: {r.text}")

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
