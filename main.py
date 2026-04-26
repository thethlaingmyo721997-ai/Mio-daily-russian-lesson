import os
import requests
import datetime
import json

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    # သင်ခန်းစာ ၃၀ (Lesson နံပါတ်များ ဖြုတ်ထားသည်)
    lessons = {
        1: "🇷🇺 Greetings\n\nПривет (ပရီ-ဗျက်)\nမင်္ဂလာပါ",
        2: "🇷🇺 Gratitude\n\nСпасибо (စပါ-စီး-ဗား)\nကျေးဇူးတင်ပါတယ်",
        3: "🇷🇺 Politeness\n\nПожалуйста (ပါ-ရှော-လ်စတာ)\nရပါတယ် / ကျေးဇူးပြု၍",
        4: "🇷🇺 Yes/No\n\nДа (ဒါး) - ဟုတ်ကဲ့\nНет (ညက်) - မဟုတ်ဘူး",
        5: "🇷🇺 Well-being\n\nКак дела? (ကပ် ဒီ-လား?)\nနေကောင်းလား?",
        6: "🇷🇺 Introductions\n\nМеня зовут... (မိ-ညာ ဇာ-ဗွတ်...)\nကျွန်တော့်နာမည်က... ပါ",
        7: "🇷🇺 Understanding\n\nЯ понимаю (ယာ ပါ-နီ-မာ-ယူ)\nကျွန်တော် နားလည်ပါတယ်",
        8: "🇷🇺 Not Understanding\n\nЯ не понимаю (ယာ ညဲ ပါ-နီ-မာ-ယူ)\nကျွန်တော် နားမလည်ပါဘူး",
        9: "🇷🇺 Farewell\n\nДо свидания (ဒါ့စ-ဗီ-ဒါး-နီး-ယား)\nပြန်တွေ့ကြမယ်",
        10: "🇷🇺 Farewell (Casual)\n\nПока (ပါ-ကား)\nတာ့တာ",
        11: "🇷🇺 Apology\n\nИзвините (အစ်ဇ်-ဗီ-နီး-ကျဲ)\nတောင်းပန်ပါတယ်",
        12: "🇷🇺 Agreement\n\nХорошо (ဟာ-ရာ-ရှော)\nကောင်းပြီ / အိုကေ",
        13: "🇷🇺 Water\n\nВода (ဗာ-ဒါး)\nရေ",
        14: "🇷🇺 Bread\n\nХлеб (ခလျပ်)\nပေါင်မုန့်",
        15: "🇷🇺 Family\n\nСемья (ဆိမျ-ယာ)\nမိသားစု",
        16: "🇷🇺 Mother\n\nМама (မား-မား)\nအမေ",
        17: "🇷🇺 Father\n\nПапа (ပား-ပား)\nအဖေ",
        18: "🇷🇺 Friend\n\nДруг (ဒရုခ်)\nသူငယ်ချင်း",
        19: "🇷🇺 Work\n\nРабота (ရာ-ဘိုး-တာ)\nအလုပ်",
        20: "🇷🇺 Car\n\nМашина (မာ-ရှီး-နား)\nကား",
        21: "🇷🇺 City\n\nГород (ဂိုး-ရတ်)\nမြို့",
        22: "🇷🇺 House\n\nДом (ဒုမ်း)\nအိမ်",
        23: "🇷🇺 School\n\nШкола (ရှကိုး-လား)\nကျောင်း",
        24: "🇷🇺 Teacher\n\nУчитель (အူ-ချီး-ကျိလ်)\nဆရာ/ဆရာမ",
        25: "🇷🇺 Book\n\nКнига (ကနီး-ဂါး)\nစာအုပ်",
        26: "🇷🇺 Time\n\nВремя (ဗရီ-မျာ)\nအချိန်",
        27: "🇷🇺 Today\n\nСегодня (စီး-ဗိုး-ဒနီး-ယာ)\nဒီနေ့",
        28: "🇷🇺 Tomorrow\n\nЗавтра (ဇားဖ်-တြာ)\nမနက်ဖြန်",
        29: "🇷🇺 Love\n\nЯ люблю тебя (ယာ လျူ-ဗလျူ တီ-ဗျာ)\nမင်းကို ချစ်တယ်",
        30: "🇷🇺 Good luck\n\nУдачи! (အူ-ဒါး-ချီ)\nကံကောင်းပါစေ!"
    }
    
    # စမ်းသပ်ရန်: မိနစ်အလိုက် သင်ခန်းစာပြောင်းခြင်း
    now = datetime.datetime.now()
    lesson_index = (now.minute // 2) + 1
    return lessons.get(lesson_index, lessons[1])

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    
    # Keyboard ခလုတ်များကို ပိုမိုရိုးရှင်းအောင် ပြင်ဆင်ထားသည်
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "📞 Call", "url": "tel:+959693548605"},
                {"text": "💬 Viber", "url": "https://msng.link/o/?959693548605=vi"}
            ],
            [
                {"text": "📱 TikTok Channel", "url": "https://www.tiktok.com/@miorusskiy"}
            ]
        ]
    }

    payload = {
        "chat_id": CHAT_ID,
        "text": f"{text}\n\n<b>သင်တန်းအပ်ရန်နှင့် အသေးစိတ်စုံစမ်းရန်-</b>\n---\nMioRussianLanguage Center",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    
    # Request ပို့ပြီး Result ကို log ထုတ်မည်
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}")

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
