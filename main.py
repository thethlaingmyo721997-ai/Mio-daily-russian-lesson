import os
import requests
import datetime

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    # ရက် ၃၀ စာ သင်ခန်းစာများ (မြန်မာအသံထွက်နှင့် အဓိပ္ပာယ်)
    lessons = {
        1: "🇷🇺 Lesson 1: Greetings\n\nПривет (ပရီ-ဗျက်)\nမင်္ဂလာပါ (ရင်းနှီးသူများအကြား)",
        2: "🇷🇺 Lesson 2: Gratitude\n\nСпасибо (စပါ-စီး-ဗား)\nကျေးဇူးတင်ပါတယ်",
        3: "🇷🇺 Lesson 3: Politeness\n\nПожалуйста (ပါ-ရှော-လ်စတာ)\nရပါတယ် / ကျေးဇူးပြု၍",
        4: "🇷🇺 Lesson 4: Yes/No\n\nДа (ဒါး) - ဟုတ်ကဲ့\nНет (ညက်) - မဟုတ်ဘူး",
        5: "🇷🇺 Lesson 5: Well-being\n\nКак дела?\n(ကပ် ဒီ-လား?)\nနေကောင်းလား?",
        6: "🇷🇺 Lesson 6: Introductions\n\nМеня зовут...\n(မိ-ညာ ဇာ-ဗွတ်...)\nကျွန်တော့်နာမည်က... ပါ",
        7: "🇷🇺 Lesson 7: Understanding\n\nЯ понимаю\n(ယာ ပါ-နီ-မာ-ယူ)\nကျွန်တော် နားလည်ပါတယ်",
        8: "🇷🇺 Lesson 8: Not Understanding\n\nЯ не понимаю\n(ယာ ညဲ ပါ-နီ-မာ-ယူ)\nကျွန်တော် နားမလည်ပါဘူး",
        9: "🇷🇺 Lesson 9: Farewell\n\nДо свидания\n(ဒါ့စ-ဗီ-ဒါး-နီး-ယား)\nပြန်တွေ့ကြမယ် (တာ့တာ)",
        10: "🇷🇺 Lesson 10: Farewell (Casual)\n\nПока\n(ပါ-ကား)\nတာ့တာ (ရင်းနှီးသူများအကြား)",
        11: "🇷🇺 Lesson 11: Apology\n\nИзвините\n(အစ်ဇ်-ဗီ-နီး-ကျဲ)\nတောင်းပန်ပါတယ်",
        12: "🇷🇺 Lesson 12: Agreement\n\nХорошо\n(ဟာ-ရာ-ရှော)\nကောင်းပြီ / အိုကေ",
        13: "🇷🇺 Lesson 13: Water\n\nВода\n(ဗာ-ဒါး)\nရေ",
        14: "🇷🇺 Lesson 14: Bread\n\nХле็บ\n(ခလျပ်)\nပေါင်မုန့်",
        15: "🇷🇺 Lesson 15: Family\n\nСемья\n(ဆိမျ-ယာ)\nမိသားစု",
        16: "🇷🇺 Lesson 16: Mother\n\nМама\n(မား-မား)\nအမေ",
        17: "🇷🇺 Lesson 17: Father\n\nПапа\n(ပား-ပား)\nအဖေ",
        18: "🇷🇺 Lesson 18: Friend\n\nДруг\n(ဒရုခ်)\nသူငယ်ချင်း",
        19: "🇷🇺 Lesson 19: Work\n\nРабота\n(ရာ-ဘိုး-တာ)\nအလုပ်",
        20: "🇷🇺 Lesson 20: Car\n\nМашина\n(မာ-ရှီး-နား)\nကား",
        21: "🇷🇺 Lesson 21: City\n\nГород\n(ဂိုး-ရတ်)\nမြို့",
        22: "🇷🇺 Lesson 22: House\n\nДом\n(ဒုမ်း)\nအိမ်",
        23: "🇷🇺 Lesson 23: School\n\nШкола\n(ရှကိုး-လား)\nကျောင်း",
        24: "🇷🇺 Lesson 24: Teacher\n\nУчитель\n(အူ-ချီး-ကျိလ်)\nဆရာ/ဆရာမ",
        25: "🇷🇺 Lesson 25: Book\n\nКнига\n(ကနီး-ဂါး)\nစာအုပ်",
        26: "🇷🇺 Lesson 26: Time\n\nВремя\n(ဗရီ-မျာ)\nအချိန်",
        27: "🇷🇺 Lesson 27: Today\n\nСегодня\n(စီး-ဗိုး-ဒနီး-ယာ)\nဒီနေ့",
        28: "🇷🇺 Lesson 28: Tomorrow\n\nЗавтра\n(ဇားဖ်-တြာ)\nမနက်ဖြန်",
        29: "🇷🇺 Lesson 29: Love\n\nЯ люблю тебя\n(ယာ လျူ-ဗလျူ တီ-ဗျာ)\nမင်းကို ချစ်တယ်",
        30: "🇷🇺 Lesson 30: Good luck\n\nУдачи!\n(အူ-ဒါး-ချီ)\nကံကောင်းပါစေ!"
    }

    # စမ်းသပ်ရန်: လက်ရှိမိနစ်ကို ၅ နဲ့စားပြီး Lesson Index ယူခြင်း
    now = datetime.datetime.now()
    lesson_index = (now.minute // 2) + 1 # ပိုမြန်အောင် ၂ မိနစ်တစ်ခါ ပြောင်းကြည့်ရအောင်
    
    return lessons.get(lesson_index, lessons[1])

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"{text}\n\n---\nMioRussianLanguage Center",
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
