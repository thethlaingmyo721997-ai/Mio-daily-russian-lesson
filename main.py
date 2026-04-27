import os
import requests
import datetime
import json
import re

# GitHub Secrets
API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
GIST_ID = os.getenv('GIST_ID')   
GH_TOKEN = os.getenv('GH_TOKEN') 

def get_current_index():
    try:
        url = f"https://api.github.com/gists/{GIST_ID}"
        headers = {"Authorization": f"token {GH_TOKEN}"}
        r = requests.get(url, headers=headers)
        
        if r.status_code != 200:
            print(f"Gist Access Error: Status {r.status_code}")
            return 1
            
        gist_data = r.json()
        files = gist_data.get('files', {})
        target_file = files.get('lesson_counter.txt')
        
        if target_file:
            return int(target_file['content'])
        else:
            print("Error: 'lesson_counter.txt' not found in Gist")
            return 1
    except Exception as e:
        print(f"Gist Exception: {e}")
        return 1

def update_index(new_index):
    if new_index > 90: new_index = 1
    try:
        url = f"https://api.github.com/gists/{GIST_ID}"
        headers = {"Authorization": f"token {GH_TOKEN}"}
        data = {"files": {"lesson_counter.txt": {"content": str(new_index)}}}
        requests.patch(url, headers=headers, json=data)
    except:
        pass

def get_daily_content(idx):
    lessons = {
        1: "🇷🇺 Lesson 1: Greetings\n\nWord: Привет (ပရီ-ဗျက်)\nMeaning: မင်္ဂလာပါ",
        2: "🇷🇺 Lesson 2: Formal Greetings\n\nWord: Здравствуйте (ဇဒြား-စတွူ-ကျီ)\nMeaning: မင်္ဂလာပါ (လူကြီး/သူစိမ်း)",
        # ... သင်ခန်းစာ ၉၀ အထိ Mio ဆီမှာ ရှိတဲ့အတိုင်း ဒီကြားထဲမှာ ထည့်ပေးပါ ...
        90: "🇷🇺 Lesson 90: Good luck\n\nWord: Удачи! (အူ-ဒါး-ချီ)\nMeaning: ကံကောင်းပါစေ!"
    }
    raw_content = lessons.get(idx, f"🇷🇺 Lesson {idx}\n\nContent Loading...")
    final_content = re.sub(r'Lesson \d+:', '', raw_content).strip()
    return final_content.replace('🇷🇺  ', '🇷🇺 ')

def send_message(text):
    """စာပို့တဲ့အခါ Telegram ကပြန်လာတဲ့ Error ကို Print ထုတ်ကြည့်မည့်အပိုင်း"""
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    
    # CHAT_ID မှာ Space ပါနေရင် ဖယ်ထုတ်ပစ်ပါမယ်
    clean_chat_id = str(CHAT_ID).strip()
    
    footer = "\n\n<b>MioRussianLanguage Center</b>\n<b>Viber/Phone : +959693548605</b>"
    payload = {
        "chat_id": clean_chat_id,
        "text": f"{text}{footer}",
        "parse_mode": "HTML"
    }
    
    r = requests.post(url, json=payload)
    
    # ဒီစာသားကို Actions Log ထဲမှာ သွားကြည့်ရပါမယ်
    print(f"Telegram API Response: {r.text}")
    
    if r.status_code == 200:
        print("Success: Message sent to Telegram!")
    else:
        print(f"Failed: Telegram returned status {r.status_code}")

if __name__ == "__main__":
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=6, minutes=30)
    
    # စမ်းသပ်နေစဉ်အတွင်း Run workflow နှိပ်ရင် ချက်ချင်းပို့အောင် အချိန်မကန့်သတ်ထားပါ
    idx = get_current_index()
    print(f"Attempting to send Lesson Index: {idx}")
    
    message = get_daily_content(idx)
    send_message(message)
    update_index(idx + 1)
