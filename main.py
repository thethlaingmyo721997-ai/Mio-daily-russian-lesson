import os
import requests
import datetime
import json

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    lessons = {
        1: "🇷🇺 Greetings\n\n<code>Привет\t(ပရီ-ဗျက်)\tမင်္ဂလာပါ</code>",
        2: "🇷🇺 Gratitude\n\n<code>Спасибо\t(စပါ-စီး-ဗား)\tကျေးဇူးတင်ပါတယ်</code>",
        3: "🇷🇺 Politeness\n\n<code>Пожалуйста\t(ပါ-ရှော-လ်စတာ)\tရပါတယ်</code>",
        4: "🇷🇺 Yes/No\n\n<code>Да\t(ဒါး)\tဟုတ်ကဲ့\nНет\t(ညက်)\tမဟုတ်ဘူး</code>",
        5: "🇷🇺 Well-being\n\n<code>Как дела?\t(ကပ် ဒီ-လား?)\tနေကောင်းလား?</code>",
        6: "🇷🇺 Introductions\n\n<code>Меня зовут...\t(မိ-ညာ ဇာ-ဗွတ်...)\tကျွန်တော့်နာမည်က... ပါ</code>",
        7: "🇷🇺 Understanding\n\n<code>Я понимаю\t(ယာ ပါ-နီ-မာ-ယူ)\tနားလည်ပါတယ်</code>",
        8: "🇷🇺 Not Understanding\n\n<code>Я не понимаю\t(ယာ ညဲ ပါ-နီ-မာ-ယူ)\tနားမလည်ပါဘူး</code>",
        9: "🇷🇺 Farewell\n\n<code>До свидания\t(ဒါ့စ-ဗီ-ဒါး-နီး-ယား)\tပြန်တွေ့ကြမယ်</code>",
        10: "🇷🇺 Farewell (Casual)\n\n<code>Пока\t(ပါ-ကား)\tတာ့တာ</code>",
        11: "🇷🇺 Apology\n\n<code>Извините\t(အစ်ဇ်-ဗီ-နီး-ကျဲ)\tတောင်းပန်ပါတယ်</code>",
        12: "🇷🇺 Agreement\n\n<code>Хорошо\t(ဟာ-ရာ-ရှော)\tကောင်းပြီ / အိုကေ</code>",
        13: "🇷🇺 Water\n\n<code>Вода\t(ဗာ-ဒါး)\tရေ</code>",
        14: "🇷🇺 Bread\n\n<code>Хлеб\t(ခလျပ်)\tပေါင်မုန့်</code>",
        15: "🇷🇺 Family\n\n<code>Семья\t(ဆိမျ-ယာ)\tမိသားစု</code>",
        16: "🇷🇺 Mother\n\n<code>Мама\t(မား-မား)\tအမေ</code>",
        17: "🇷🇺 Father\n\n<code>Папа\t(ပား-ပား)\tအဖေ</code>",
        18: "🇷🇺 Friend\n\n<code>Друг\t(ဒရုခ်)\tသူငယ်ချင်း</code>",
        19: "🇷🇺 Work\n\n<code>Работа\t(ရာ-ဘိုး-တာ)\tအလုပ်</code>",
        20: "🇷🇺 Car\n\n<code>Машина\t(မာ-ရှီး-နား)\tကား</code>",
        21: "🇷🇺 City\n\n<code>Город\t(ဂိုး-ရတ်)\tမြို့</code>",
        22: "🇷🇺 House\n\n<code>Дом\t(ဒုမ်း)\tအိမ်</code>",
        23: "🇷🇺 School\n\n<code>Школа\t(ရှကိုး-လား)\tကျောင်း</code>",
        24: "🇷🇺 Teacher\n\n<code>Учитель\t(အူ-ချီး-ကျိလ်)\tဆရာ/ဆရာမ</code>",
        25: "🇷🇺 Book\n\n<code>Книга\t(ကနီး-ဂါး)\tစာအုပ်</code>",
        26: "🇷🇺 Time\n\n<code>Время\t(ဗရီ-မျာ)\tအချိန်</code>",
        27: "🇷🇺 Today\n\n<code>Сегодня\t(စီး-ဗိုး-ဒနီး-ယာ)\tဒီနေ့</code>",
        28: "🇷🇺 Tomorrow\n\n<code>Завтра\t(ဇားဖ်-တြာ)\tမနက်ဖြန်</code>",
        29: "🇷🇺 Love\n\n<code>Я люблю тебя\t(ယာ လျူ-ဗလျူ တီ-ဗျာ)\tချစ်တယ်</code>",
        30: "🇷🇺 Good luck\n\n<code>Удачи!\t(အူ-ဒါး-ချီ)\tကံကောင်းပါစေ!</code>"
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
        
        "📞 Phone Call: 09693548605\n"
    )

    payload = {
        "chat_id": str(CHAT_ID).strip(),
        "text": f"{text}\n\n{contact_info}\n---\n<b>MioRussianLanguage Center</b>",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}, Response: {r.text}")

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
