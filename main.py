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
        6: "🇷🇺 Introductions\n\nМенያ ဇာဗွတ်... (မိ-ညာ ဇာ-ဗွတ်...)\nကျွန်တော့်နာမည်က... ပါ",
        7: "🇷🇺 Understanding\n\nယာ ပါနီမာယူ (ယာ ပါ-နီ-မာ-ယူ)\nကျွန်တော် နားလည်ပါတယ်",
        8: "🇷🇺 Not Understanding\n\nယာ ညဲ ပါနီမာယူ (ယာ ညဲ ပါ-နီ-မာ-ယူ)\nကျွန်တော် နားမလည်ပါဘူး",
        9: "🇷🇺 Farewell\n\nဒါ့စဗီဒါးနီးယား (ဒါ့စ-ဗီ-ဒါး-နီး-ယား)\nပြန်တွေ့ကြမယ်",
        10: "🇷🇺 Farewell (Casual)\n\nပါကား (ပါ-ကား)\nတာ့တာ",
        29: "🇷🇺 Love\n\nယာ လျူဗလျူ တီဗျာ (ယာ လျူ-ဗလျူ တီ-ဗျာ)\nမင်းကို ချစ်တယ်",
        30: "🇷🇺 Good luck\n\nအူဒါးချီ! (အူ-ဒါး-ချီ)\nကံကောင်းပါစေ!"
    }
    
    now = datetime.datetime.now()
    # စမ်းသပ်ရန်: ၅ မိနစ်တစ်ခါ သင်ခန်းစာပြောင်းခြင်း
    lesson_index = (now.minute // 5) + 1
    return lessons.get(lesson_index, lessons[1])

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    
    # ခလုတ်များကို Telegram က လက်ခံနိုင်ဆုံး link ပုံစံများသို့ ပြောင်းလဲထားသည်
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "📞 Call", "url": "tel:+959693548605"},
                {"text": "💬 Viber", "url": "https://viber.me/959693548605"}
            ],
            [
                {"text": "📱 TikTok Channel", "url": "https://www.tiktok.com/@miorusskiy"}
            ]
        ]
    }

    payload = {
        "chat_id": str(CHAT_ID).strip(), # Space ပါနေရင် ဖယ်ထုတ်ရန်
        "text": f"{text}\n\n<b>သင်တန်းအပ်ရန်နှင့် အသေးစိတ်စုံစမ်းရန်-</b>\n---\nMioRussianLanguage Center",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    
    r = requests.post(url, json=payload)
    
    # အရေးကြီး: GitHub Actions ရဲ့ Log မှာ အဖြေကို ကြည့်နိုင်ရန်
    print(f"--- BOT LOG ---")
    print(f"Status Code: {r.status_code}")
    print(f"Response Body: {r.text}")
    print(f"----------------")

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
