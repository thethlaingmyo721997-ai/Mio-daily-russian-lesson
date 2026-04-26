import os
import requests
import datetime

# GitHub Secrets မှ အချက်အလက်ယူခြင်
API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def send_message(text):
    if not API_TOKEN or not CHAT_ID:
        print("Error: API_TOKEN or CHAT_ID is missing!")
        return
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Successfully sent to Telegram!")
        else:
            print(f"Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    today = datetime.datetime.now().strftime("%d %B %Y")
    content = f"🇷🇺 Russian Lesson for {today}\n\nWord: Учить (U-cheet)\nMeaning: သင်ယူသည်\nExample: Я учу русский язык.\n\n🎬 TikTok: ရုရှားစာကို အတူတူလေ့လာကြရအောင်!"
    send_message(content)
