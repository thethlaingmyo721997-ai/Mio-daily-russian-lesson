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
            print(f"Gist Error: {r.status_code}")
            return 1
        gist_data = r.json()
        return int(gist_data['files']['lesson_counter.txt']['content'])
    except:
        return 1

def update_index(new_index):
    if new_index > 90: new_index = 1
    url = f"https://api.github.com/gists/{GIST_ID}"
    headers = {"Authorization": f"token {GH_TOKEN}"}
    data = {"files": {"lesson_counter.txt": {"content": str(new_index)}}}
    requests.patch(url, headers=headers, json=data)

def get_daily_content(idx):
    # Mio ရဲ့ သင်ခန်းစာ ၉၀ ကို ဒီမှာ ထည့်ထားပါ (နမူနာ ၁၀ ခု ပြပေးထားပါတယ်)
    lessons = {
        1: "🇷🇺 Lesson 1: Greetings\n\nWord: Привет (ပရီ-ဗျက်)\nMeaning: မင်္ဂလာပါ",
        2: "🇷🇺 Lesson 2: Formal Greetings\n\nWord: Здравствуйте (ဇဒြား-စတွူ-ကျီ)\nMeaning: မင်္ဂလာပါ (လူကြီး/သူစိမ်း)",
        3: "🇷🇺 Lesson 3: Good morning\n\nWord: Доброе утро (ဒိုး-ဘရိုး အူ-တြာ)\nMeaning: မင်္ဂလာနံနက်ခင်းပါ",
        4: "🇷🇺 Lesson 4: Good day\n\nWord: Добрый день (ဒိုး-ဘရီ ကျင်း)\nMeaning: မင်္ဂလာနေ့လယ်ခင်းပါ",
        5: "🇷🇺 Lesson 5: Good evening\n\nWord: Добрый вечер (ဒိုး-ဘရီ ဗျဲ-ချယ်)\nMeaning: မင်္ဂလာညနေခင်းပါ",
        6: "🇷🇺 Lesson 6: Farewell\n\nWord: До свидания (ဒါ-စဝီ-ဒါး-နီး-ယာ)\nMeaning: ပြန်တွေ့ကြမယ်",
        7: "🇷🇺 Lesson 7: Gratitude\n\nWord: Спасибо (စပါ-စီး-ဗား)\nMeaning: ကျေးဇူးတင်ပါတယ်",
        8: "🇷🇺 Lesson 8: Politeness\n\nWord: Пожалуйста (ပါ-ရှော-လ်စတာ)\nMeaning: ရပါတယ် / ကျေးဇူးပြု၍",
        9: "🇷🇺 Lesson 9: Apology\n\nWord: Извините (အစ်ဇ်-ဝီ-နီး-ကျီ)\nMeaning: တောင်းပန်ပါတယ် / ခွင့်လွှတ်ပါ",
        10: "🇷🇺 Lesson 10: Yes/No\n\nWord: Да / Нет (ဒါး / ညက်)\nMeaning: ဟုတ်ကဲ့ / မဟုတ်ဘူး"
    }
    raw = lessons.get(idx, f"🇷🇺 Lesson {idx}\n\nContent Loading...")
    return re.sub(r'Lesson \d+:', '', raw).strip().replace('🇷🇺  ', '🇷🇺 ')

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    footer = "\n\n<b>MioRussianLanguage Center</b>\n<b>Viber/Phone : +959693548605</b>"
    payload = {"chat_id": str(CHAT_ID).strip(), "text": f"{text}{footer}", "parse_mode": "HTML"}
    r = requests.post(url, json=payload)
    print(f"Telegram Response: {r.text}")

if __name__ == "__main__":
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=6, minutes=30)
    # မြန်မာစံတော်ချိန် ၈ နာရီမှ ၂၄ နာရီအတွင်းဖြစ်မှ ပို့မည်
    if 8 <= now.hour < 24:
        idx = get_current_index()
        send_message(get_daily_content(idx))
        update_index(idx + 1)
