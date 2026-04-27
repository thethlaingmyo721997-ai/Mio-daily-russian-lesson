import os
import requests
import datetime
import json

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    # သင်ခန်းစာ ၉၀ (အပေါ်က Lesson တွေအတိုင်း အကုန်ပြန်ထည့်ထားပေးပါ)
    lessons = {
 1: "🇷🇺 Lesson 1: Greetings\n\nWord: Привет (ပရီ-ဗျက်)\nMeaning: မင်္ဂလာပါ (ရင်းနှီးသူများအကြား)",
        2: "🇷🇺 Lesson 2: Formal Greetings\n\nWord: Здравствуйте (ဇဒြား-စတွူ-ကျီ)\nMeaning: မင်္ဂလာပါ (လူကြီး/သူစိမ်း)",
        3: "🇷🇺 Lesson 3: Good morning\n\nWord: Доброе утро (ဒိုး-ဘရိုး အူ-တြာ)\nMeaning: မင်္ဂလာနံနက်ခင်းပါ",
        4: "🇷🇺 Lesson 4: Good day\n\nWord: Добрый день (ဒိုး-ဘရီ ကျင်း)\nMeaning: မင်္ဂလာနေ့လယ်ခင်းပါ",
        5: "🇷🇺 Lesson 5: Good evening\n\nWord: Добрый вечер (ဒိုး-ဘရီ ဗျဲ-ချယ်)\nMeaning: မင်္ဂလာညနေခင်းပါ",
        6: "🇷🇺 Lesson 6: Farewell\n\nWord: До свидания (ဒါ-စဝီ-ဒါး-နီး-ယာ)\nMeaning: ပြန်တွေ့ကြမယ်",
        7: "🇷🇺 Lesson 7: Gratitude\n\nWord: Спасибо (စပါ-စီး-ဗား)\nMeaning: ကျေးဇူးတင်ပါတယ်",
        8: "🇷🇺 Lesson 8: Politeness\n\nWord: Пожалуйста (ပါ-ရှော-လ်စတာ)\nMeaning: ရပါတယ် / ကျေးဇူးပြု၍",
        9: "🇷🇺 Lesson 9: Apology\n\nWord: Извините (အစ်ဇ်-ဝီ-နီး-ကျီ)\nMeaning: တောင်းပန်ပါတယ် / ခွင့်လွှတ်ပါ",
        10: "🇷🇺 Lesson 10: Yes/No\n\nWord: Да / Нет (ဒါး / ညက်)\nMeaning: ဟုတ်ကဲ့ / မဟုတ်ဘူး",
        11: "🇷🇺 Lesson 11: Okay\n\nWord: Хорошо (ဟာ-ရာ-ရှိုး)\nMeaning: ကောင်းပါပြီ / အိုကေ",
        12: "🇷🇺 Lesson 12: How are you?\n\nWord: Как дела? (ကပ် ဒီ-လား?)\nMeaning: နေကောင်းလား?",
        13: "🇷🇺 Lesson 13: Name\n\nWord: Меня зовут... (မိ-ညာ ဇာ-ဗွတ်...)\nMeaning: ကျွန်တော့်နာမည်က... ပါ",
        14: "🇷🇺 Lesson 14: Nice to meet you\n\nWord: Приятно познакомиться\nMeaning: တွေ့ရတာ ဝမ်းသာပါတယ်",
        15: "🇷🇺 Lesson 15: Friend\n\nWord: Мой друг (မွိုင်း ဒရုခ်)\nMeaning: ကျွန်တော့်သူငယ်ချင်း",
        16: "🇷🇺 Lesson 16: I understand\n\nWord: Я понимаю (ယာ ပါ-နီ-မား-ယူး)\nMeaning: ကျွန်တော် နားလည်ပါတယ်",
        17: "🇷🇺 Lesson 17: I don't understand\n\nWord: Я не понимаю\nMeaning: ကျွန်တော် နားမလည်ပါဘူး",
        18: "🇷🇺 Lesson 18: Please repeat\n\nWord: Повторите, пожалуйста\nMeaning: နောက်တစ်ခေါက်လောက်ပြောပေးပါ",
        19: "🇷🇺 Lesson 19: Number 1\n\nWord: Один (အာ-ဂျင်း)\nMeaning: တစ်",
        20: "🇷🇺 Lesson 20: Number 2\n\nWord: Два (ဒွါး)\nMeaning: နှစ်",
        21: "🇷🇺 Lesson 21: Number 3\n\nWord: Три (တြီး)\nMeaning: သုံး",
        22: "🇷🇺 Lesson 22: Number 4\n\nWord: Четыре (ချီ-တီး-ရီ)\nMeaning: လေး",
        23: "🇷🇺 Lesson 23: Number 5\n\nWord: Пять (ပျတ်)\nMeaning: ငါး",
        24: "🇷🇺 Lesson 24: Number 6\n\nWord: Шесть (ရှက်စ်တ်)\nMeaning: ခြောက်",
        25: "🇷🇺 Lesson 25: Number 7\n\nWord: Семь (ဆင်မ်)\nMeaning: ခုနစ်",
        26: "🇷🇺 Lesson 26: Number 8\n\nWord: Восемь (ဝိုး-ဆင်မ်)\nMeaning: ရှစ်",
        27: "🇷🇺 Lesson 27: Number 9\n\nWord: Девять (ဂျဲ-ဗျတ်)\nMeaning: ကိုး",
        28: "🇷🇺 Lesson 28: Number 10\n\nWord: Десять (ဂျဲ-ဆတ်)\nMeaning: တစ်ဆယ်",
        29: "🇷🇺 Lesson 29: Number 0\n\nWord: Ноль (နိုးလ်)\nMeaning: သုည",
        30: "🇷🇺 Lesson 30: Hundred\n\nWord: Сто (စတိုး)\nMeaning: တစ်ရာ"
    }
    
    # မြန်မာစံတော်ချိန် ယူခြင်း
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=6, minutes=30)
    hour = now.hour # ၀ နာရီ ကနေ ၂၃ နာရီ အထိ ရှိမည်

    # စမ်းသပ်ရန်အတွက်: နာရီအလိုက် Lesson နံပါတ် ရွေးခြင်း
    # ဥပမာ - မနက် ၁၀ နာရီဆိုရင် Lesson 10 ကို ပို့ပေးပါလိမ့်မယ်
    idx = hour
    if idx == 0: idx = 24 # ညသန်းခေါင်ဆိုရင် Lesson 24 လို့ သတ်မှတ်
    if idx > 90: idx = 90
    
    # သင်ခန်းစာ စာသားကို ယူခြင်း (မရှိရင် Lesson 1 ပို့မည်)
    content = lessons.get(idx, f"🇷🇺 Lesson {idx}\n\nContent coming soon!")
    return content

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    keyboard = {"inline_keyboard": [[{"text": "💬 Viber Chat", "url": "https://viber.me/959693548605"}]]}
    
    payload = {
        "chat_id": str(CHAT_ID).strip(),
        "text": f"{text}\n\n<b>Mio Hourly Test Mode</b>",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}, Sent Hour: {datetime.datetime.now().hour}")

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
