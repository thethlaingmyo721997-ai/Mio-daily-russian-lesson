import os

import requests

import datetime



API_TOKEN = os.getenv('BOT_TOKEN')

CHAT_ID = os.getenv('CHAT_ID')



def get_daily_content():

    # ရက် ၃၀ စာ သင်ခန်းစာများ (မြန်မာအသံထွက်နှင့် အဓိပ္ပာယ် အပြည့်အစုံ)

    lessons = {

        1: "🇷🇺 Lesson : Greetings\n\nПривет\n(ပရီ-ဗျက်)\nမင်္ဂလာပါ (ရင်းနှီးသူများအကြား)",

        2: "🇷🇺 Lesson : Gratitude\n\nСпасибо\n(စပါ-စီး-ဗား)\nကျေးဇူးတင်ပါတယ်",

        3: "🇷🇺 Lesson : Politeness\n\nПожалуйста\n(ပါ-ရှော-လ်စတာ)\nရပါတယ် / ကျေးဇူးပြု၍",

        4: "🇷🇺 Lesson : Yes/No\n\nДа (ဒါး) - ဟုတ်ကဲ့\nНет (ညက်) - မဟုတ်ဘူး",

        5: "🇷🇺 Lesson : Well-being\n\nКак дела?\n(ကပ် ဒီ-လား?)\nနေကောင်းလား?",

        6: "🇷🇺 Lesson : Introductions\n\nМеня зовут...\n(မိ-ညာ ဇာ-ဗွတ်...)\nကျွန်တော့်နာမည်က... ပါ",

        7: "🇷🇺 Lesson : Understanding\n\nЯ понимаю\n(ယာ ပါ-နီ-မာ-ယူ)\nကျွန်တော် နားလည်ပါတယ်",

        8: "🇷🇺 Lesson : Not Understanding\n\nЯ не понимаю\n(ယာ ညဲ ပါ-နီ-မာ-ယူ)\nကျွန်တော် နားမလည်ပါဘူး",

        9: "🇷🇺 Lesson : Farewell\n\nДо свидания\n(ဒါ့စ-ဗီ-ဒါး-နီး-ယား)\nပြန်တွေ့ကြမယ် (တာ့တာ)",

        10: "🇷🇺 Lesson : Farewell (Casual)\n\nПока\n(ပါ-ကား)\nတာ့တာ (ရင်းနှီးသူများအကြား)",

        11: "🇷🇺 Lesson : Apology\n\nИзвините\n(အစ်ဇ်-ဗီ-နီး-ကျဲ)\nတောင်းပန်ပါတယ်",

        12: "🇷🇺 Lesson : Agreement\n\nХорошо\n(ဟာ-ရာ-ရှော)\nကောင်းပြီ / အိုကေ",

        13: "🇷🇺 Lesson : Water\n\nВода\n(ဗာ-ဒါး)\nရေ",

        14: "🇷🇺 Lesson : Bread\n\nХлеб\n(ခလျပ်)\nပေါင်မုန့်",

        15: "🇷🇺 Lesson : Family\n\nСемья\n(ဆိမျ-ယာ)\nမိသားစု",

        16: "🇷🇺 Lesson : Mother\n\nМама\n(မား-မား)\nအမေ",

        17: "🇷🇺 Lesson : Father\n\nПапа\n(ပား-ပား)\nအဖေ",

        18: "🇷🇺 Lesson : Friend\n\nДруг\n(ဒရု(ခ်))\nသူငယ်ချင်း",

        19: "🇷🇺 Lesson : Work\n\nРабота\n(ရာ-ဘိုး-တာ)\nအလုပ်",

        20: "🇷🇺 Lesson : Car\n\nМашина\n(မာ-ရှီး-နား)\nကား",

        21: "🇷🇺 Lesson : City\n\nГород\n(ဂိုး-ရတ်)\nမြို့",

        22: "🇷🇺 Lesson : House\n\nДом\n(ဒုမ်း)\nအိမ်",

        23: "🇷🇺 Lesson : School\n\nШкола\n(ရှကိုး-လား)\nကျောင်း",

        24: "🇷🇺 Lesson : Teacher\n\nУчитель\n(အူ-ချီး-ကျိလ်)\nဆရာ/ဆရာမ",

        25: "🇷🇺 Lesson : Book\n\nКнига\n(ကနီး-ဂါး)\nစာအုပ်",

        26: "🇷🇺 Lesson : Time\n\nВремя\n(ဗရီ-မျာ)\nအချိန်",

        27: "🇷🇺 Lesson : Today\n\nСегодня\n(စီး-ဗိုး-ဒနီး-ယာ)\nဒီနေ့",

        28: "🇷🇺 Lesson : Tomorrow\n\nЗавтра\n(ဇားဖ်-တြာ)\nမနက်ဖြန်",

        29: "🇷🇺 Lesson : Love\n\nЯ люблю тебя\n(ယာ လျူ-ဗလျူ တီ-ဗျာ)\nမင်းကို ချစ်တယ်",

        30: "🇷🇺 Lesson : Good luck\n\nУдачи!\n(အူ-ဒါး-ချီ)\nကံကောင်းပါစေ!"

    }

    

    day_of_month = datetime.datetime.now().day

    return lessons.get(day_of_month, lessons[1])



def send_message(text):

    today = datetime.datetime.now().strftime("%d %B %Y")

    formatted_text = f"📅 {today}\n\n{text}\n\-------------- \nMioRussianLanguage Center"

    

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
