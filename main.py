import os
import requests
import datetime
import json

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    # သင်ခန်းစာ ၃၀ လုံး
    lessons = {
        1: "🇷🇺 Greetings\n\n<code>Word:\tПривет\t(ပရီ-ဗျက်)\nMeaning:\tမင်္ဂလာပါ</code>",
        2: "🇷🇺 Gratitude\n\n<code>Word:\tСпасибо\t(စပါ-စီး-ဗား)\nMeaning:\tကျေးဇူးတင်ပါတယ်</code>",
        3: "🇷🇺 Politeness\n\n<code>Word:\tПожалуйста\t(ပါ-ရှော-လ်စတာ)\nMeaning:\tရပါတယ်</code>",
        4: "🇷🇺 Yes/No\n\n<code>Word:\tДа\t(ဒါး)\nMeaning:\tဟုတ်ကဲ့\n\nWord:\tНет\t(ညက်)\nMeaning:\tမဟုတ်ဘူး</code>",
        5: "🇷🇺 Well-being\n\n<code>Word:\tКак дела?\t(ကပ် ဒီ-လား?)\nMeaning:\tနေကောင်းလား?</code>",
        6: "🇷🇺 Introductions\n\n<code>Word:\tМеня зовут...\t(မိ-ညာ ဇာ-ဗွတ်...)\nMeaning:\tကျွန်တော့်နာမည်က... ပါ</code>",
        7: "🇷🇺 Understanding\n\n<code>Word:\tЯ понимаю\t(ယာ ပါ-နီ-မာ-ယူ)\nMeaning:\tနားလည်ပါတယ်</code>",
        8: "🇷🇺 Not Understanding\n\n<code>Word:\tЯ не понимаю\t(ယာ ညဲ ပါ-နီ-မာ-ယူ)\nMeaning:\tနားမလည်ပါဘူး</code>",
        9: "🇷🇺 Farewell\n\n<code>Word:\tДо свидания\t(ဒါ့စ-ဗီ-ဒါး-နီး-ယား)\nMeaning:\tပြန်တွေ့ကြမယ်</code>",
        10: "🇷🇺 Farewell (Casual)\n\n<code>Word:\tПока\t(ပါ-ကား)\nMeaning:\tတာ့တာ</code>",
        11: "🇷🇺 Apology\n\n<code>Word:\tИзвините\t(အစ်ဇ်-ဗီ-နီး-ကျဲ)\nMeaning:\tတောင်းပန်ပါတယ်</code>",
        12: "🇷🇺 Agreement\n\n<code>Word:\tХорошо\t(ဟာ-ရာ-ရှော)\nMeaning:\tကောင်းပြီ / အိုကေ</code>",
        13: "🇷🇺 Water\n\n<code>Word:\tВода\t(ဗာ-ဒါး)\nMeaning:\tရေ</code>",
        14: "🇷🇺 Bread\n\n<code>Word:\tХлеб\t(ခလျပ်)\nMeaning:\tပေါင်မုန့်</code>",
        15: "🇷🇺 Family\n\n<code>Word:\tСемья\t(ဆိမျ-ယာ)\nMeaning:\tမိသားစု</code>",
        16: "🇷🇺 Mother\n\n<code>Word:\tМама\t(မား-မား)\nMeaning:\tအမေ</code>",
        17: "🇷🇺 Father\n\n<code>Word:\tПапа\t(ပား-ပား)\nMeaning:\tအဖေ</code>",
        18: "🇷🇺 Friend\n\n<code>Word:\tДруг\t(ဒရုခ်)\nMeaning:\tသူငယ်ချင်း</code>",
        19: "🇷🇺 Work\n\n<code>Word:\tРабота\t(ရာ-ဘိုး-တာ)\nMeaning:\tအလုပ်</code>",
        20: "🇷🇺 Car\n\n<code>Word:\tМашина\t(မာ-ရှီး-နား)\nMeaning:\tကား</code>",
        21: "🇷🇺 City\n\n<code>Word:\tГород\t(ဂိုး-ရတ်)\nMeaning:\tမြို့</code>",
        22: "🇷🇺 House\n\n<code>Word:\tДом\t(ဒုမ်း)\nMeaning:\tအိမ်</code>",
        23: "🇷🇺 School\n\n<code>Word:\tШкола\t(ရှကိုး-လား)\nMeaning:\tကျောင်း</code>",
        24: "🇷🇺 Teacher\n\n<code>Word:\tУчитель\t(အူ-ချီး-ကျိလ်)\nMeaning:\tဆရာ/ဆရာမ</code>",
        25: "🇷🇺 Book\n\n<code>Word:\tКнига\t(ကနီး-ဂါး)\nMeaning:\tစာအုပ်</code>",
        26: "🇷🇺 Time\n\n<code>Word:\tВремя\t(ဗရီ-မျာ)\nMeaning:\tအချိန်</code>",
        27: "🇷🇺 Today\n\n<code>Word:\tСегодня\t(စီး-ဗိုး-ဒနီး-ယာ)\nMeaning:\tဒီနေ့</code>",
        28: "🇷🇺 Tomorrow\n\n<code>Word:\tЗавтра\t(ဇားဖ်-တြာ)\nMeaning:\tမနက်ဖြန်</code>",
        29: "🇷🇺 Love\n\n<code>Word:\tЯ люблю тебя\t(ယာ လျူ-ဗလျူ တီ-ဗျာ)\nMeaning:\tချစ်တယ်</code>",
        30: "🇷🇺 Good luck\n\n<code>Word:\tУдачи!\t(အူ-ဒါး-ချီ)\nMeaning:\tကံကောင်းပါစေ!</code>"
    }
    
    # မြန်မာစံတော်ချိန် တွက်ချက်ခြင်း
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=6, minutes=30)
    hour = now.hour

    # အချိန်ပေါ်မူတည်ပြီး Lesson နံပါတ်ရွေးခြင်း
    # မနက်ပိုင်း (၉ နာရီဝန်းကျင်) ဆိုလျှင် Lesson 1
    if hour < 11:
        idx = 1
    # နေ့လယ်ပိုင်း (၁၂ နာရီဝန်းကျင်) ဆိုလျှင် Lesson 2
    elif hour < 14:
        idx = 2
    # ညနေပိုင်း (၃ နာရီဝန်းကျင်) ဆိုလျှင် Lesson 3
    else:
        idx = 3

    return lessons.get(idx, lessons[1])

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    
    keyboard = {
        "inline_keyboard": [[
            {"text": "💬 Viber Chat", "url": "https://viber.me/959693548605"},
            {"text": "📱 TikTok", "url": "https://www.tiktok.com/@miorusskiy"}
        ]]
    }

    caption_text = (
        f"{text}\n\n"
        f"<b>သင်တန်းစုံစမ်းရန်:</b>\n"
        f"Viber: +959693548605\n"
        f"Phone: +959693548605\n"
        f"---\n"
        f"MioRussianLanguage Center"
    )

    payload = {
        "chat_id": str(CHAT_ID).strip(),
        "text": caption_text,
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}, Sent Lesson: {text.splitlines()[0]}")

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
