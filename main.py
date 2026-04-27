import os
import requests
import datetime
import json

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    # သင်ခန်းစာ ၉၀ လုံး (အရင်အတိုင်း အကုန်ထည့်ထားပါ)
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
    }
    
    # မြန်မာစံတော်ချိန် ယူခြင်း
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=6, minutes=30)
    day = now.day
    hour = now.hour

    # --- ဧပြီ ၂၇ မှ စမ်းသပ်ရန် Logic ---
    # ဒီနေ့ (၂၇ ရက်) ကို Day 1 လို့ သတ်မှတ်ဖို့ ၂၆ နှုတ်ပါမည်။
    # ၂၇ ရက်နေ့ဆိုရင် (27 - 26) = Day 1 ဖြစ်သွားပါမည်။
    # ၂၈ ရက်နေ့ဆိုရင် (28 - 26) = Day 2 ဖြစ်သွားပါမည်။
    
    test_day = day - 26 
    
    if test_day < 1: test_day = 1 # အကယ်၍ ၂၇ မတိုင်ခင် ရက်တွေဖြစ်နေခဲ့ရင်

    if hour < 11:
        idx = (test_day * 3 - 2)
    elif hour < 14:
        idx = (test_day * 3 - 1)
    else:
        idx = (test_day * 3)

    if idx > 90: idx = 90
    
    return lessons.get(idx, lessons[1])

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    keyboard = {"inline_keyboard": [[{"text": "💬 Viber Chat", "url": "https://viber.me/959693548605"}]]}
    
    payload = {
        "chat_id": str(CHAT_ID).strip(),
        "text": f"{text}\n\n<b>MioRussianLanguage Center</b>",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    r = requests.post(url, json=payload)
    print(f"Status: {r.status_code}, Sent Lesson Index: {text.splitlines()[0]}")

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
