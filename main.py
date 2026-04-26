import os
import requests
import datetime

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_lesson_by_time():
    now = datetime.datetime.now()
    # မြန်မာစံတော်ချိန် ပြောင်းလဲတွက်ချက်ခြင်း (UTC + 6:30)
    hour = (now.hour + 6) % 24 
    
    # ၁။ မနက်ခင်း သင်ခန်းစာ (မနက် ၉ နာရီ ဝန်းကျင်)
    if 8 <= hour <= 10:
        return "☀️ <b>မနက်ခင်း ရုရှားစာ သင်ခန်းစာ</b>\n\nДоброе утро!\n(ဒိုးဘရွဲ အူထရို)\nမင်္ဂလာနံနက်ခင်းပါ"
    
    # ၂။ နေ့လည်ခင်း သင်ခန်းစာ (နေ့လည် ၁၂ နာရီ ဝန်းကျင်)
    elif 11 <= hour <= 13:
        return "🌤 <b>နေ့လည်ခင်း ရုရှားစာ သင်ခန်းစာ</b>\n\nПриятного аппетита!\n(ပရီ-ယတ်-နာ-ဗာ အာ-ပီ-ကျီး-တာ)\nစားကောင်းပါစေ"
    
    # ၃။ ညနေခင်း သင်ခန်းစာ (ညနေ ၃ နာရီ ဝန်းကျင်)
    elif 14 <= hour <= 16:
        return "☕ <b>ညနေခင်း ရုရှားစာ သင်ခန်းစာ</b>\n\nКак прошёл день?\n(ကပ် ပရာ-ရှောလ် ဒျင်း?)\nဒီနေ့ ဘယ်လိုဖြတ်သန်းခဲ့လဲ?"
    
    else:
        return "🇷🇺 သင်ခန်းစာအသစ် မကြာမီ လာပါမည်..."

def send_message(text):
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
