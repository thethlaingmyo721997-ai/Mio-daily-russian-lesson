import os
import requests
import datetime

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_lesson_by_time():
    now = datetime.datetime.now()
    # မြန်မာစံတော်ချိန် တွက်ချက်ခြင်း (UTC + 6:30)
    hour = (now.hour + 6) % 24
    day_of_month = now.day

    # --- မနက်ခင်း: နှုတ်ဆက်စကား (Greetings) ---
    morning_lessons = {
        1: "Привет (ပရီ-ဗျက်) - မင်္ဂလာပါ",
        2: "Доброе утро (ဒိုး-ဘရွဲ အူ-ထရို) - မင်္ဂလာနံနက်ခင်းပါ",
        3: "Здравствуйте (ဇဒရပ်-တ်စ-ဗွီ-ကျဲ) - မင်္ဂလာပါ (အများဆိုင်)",
        4: "Как дела? (ကပ် ဒီ-လား) - နေကောင်းလား?",
        5: "Приятно познакомиться (ပရီ-ယတ်-နာ ပါ-ဇနာ-ကို-မစ်-ဆာ) - တွေ့ရတာ ဝမ်းသာပါတယ်",
        # ... (ကျန်တဲ့ရက်တွေအတွက်လည်း ဒီပုံစံအတိုင်း ဖြည့်နိုင်ပါတယ်)
    }

    # --- နေ့လည်ခင်း: စကားပြော (Phrases) ---
    afternoon_lessons = {
        1: "Меня зовут... (မိ-ညာ ဇာ-ဗွတ်...) - ကျွန်တော့်နာမည်က... ပါ",
        2: "Я из Мьянмы (ယာ အစ် မြန်း-မား) - ကျွန်တော် မြန်မာနိုင်ငံကပါ",
        3: "Сколько это стоит? (စကိုးလ်-ကာ အက်-တာ စတိုး-အစ်) - ဒါ ဘယ်လောက်လဲ?",
        4: "Я понимаю (ယာ ပါ-နီ-မာ-ယူ) - ကျွန်တော် နားလည်ပါတယ်",
        5: "Помогите мне (ပါ-မာ-ဂီး-ကျဲ မိ-ညဲ) - ကျွန်တော့်ကို ကူညီပါ",
    }

    # --- ညနေခင်း: ဝေါဟာရ (Vocabulary) ---
    evening_lessons = {
        1: "Вода (ဗာ-ဒါး) - ရေ",
        2: "Хлеб (ခလျပ်) - ပေါင်မုန့်",
        3: "Машина (မာ-ရှီး-နား) - ကား",
        4: "Дом (ဒုမ်း) - အိမ်",
        5: "Книга (ကနီး-ဂါး) - စာအုပ်",
    }

    # အချိန်အလိုက် သင်ခန်းစာ ရွေးချယ်ခြင်း
    if 7 <= hour <= 10:
        lesson = morning_lessons.get(day_of_month, morning_lessons[1])
        header = "☀️ <b>မနက်ခင်း နှုတ်ဆက်စကား သင်ခန်းစာ</b>"
    elif 11 <= hour <= 13:
        lesson = afternoon_lessons.get(day_of_month, afternoon_lessons[1])
        header = "🌤 <b>နေ့လည်ခင်း စကားပြော သင်ခန်းစာ</b>"
    elif 14 <= hour <= 17:
        lesson = evening_lessons.get(day_of_month, evening_lessons[1])
        header = "☕ <b>ညနေခင်း ဝေါဟာရ သင်ခန်းစာ</b>"
    else:
        return None # သတ်မှတ်ချိန်မဟုတ်ရင် စာမပို့ပါ

    return f"{header}\n\n{lesson}"

def send_message(text):
    if text is None: return
    
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"{text}\n\n---\nMioRussianLanguage Center",
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    message = get_lesson_by_time()
    send_message(message)
