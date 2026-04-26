import os
import requests
import datetime

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    # ရက် ၃၀ စာ သင်ခန်းစာများ
    lessons = {
        1: "🇷🇺 Lesson 1: Greetings\n\nПривет (ပရီ-ဗျက်) - မင်္ဂလာပါ",
        2: "🇷🇺 Lesson 2: Gratitude\n\nСпасибо (စပါ-စီး-ဗား) - ကျေးဇူးတင်ပါတယ်",
        3: "🇷🇺 Lesson 3: Politeness\n\nПожалуйста (ပါ-ရှော-လ်စတာ) - ရပါတယ်",
        4: "🇷🇺 Lesson 4: Yes/No\n\nДа (ဒါး) - ဟုတ်ကဲ့ / Нет (ညက်) - မဟုတ်ဘူး",
        5: "🇷🇺 Lesson 5: Well-being\n\nКак дела? (ကပ် ဒီ-လား?) - နေကောင်းလား?",
        6: "🇷🇺 Lesson 6: Introductions\n\nМеня зовут... (မိ-ညာ ဇာ-ဗွတ်...) - ကျွန်တော့်နာမည်က... ပါ",
        7: "🇷🇺 Lesson 7: Understanding\n\nЯ понимаю (ယာ ပါ-နီ-မာ-ယူ) - ကျွန်တော် နားလည်ပါတယ်",
        8: "🇷🇺 Lesson 8: Not Understanding\n\nЯ не понимаю (ယာ ညဲ ပါ-နီ-မာ-ယူ) - ကျွန်တော် နားမလည်ပါဘူး",
        9: "🇷🇺 Lesson 9: Farewell\n\nДо свидания (ဒါ့စ-ဗီ-ဒါး-နီး-ယား) - ပြန်တွေ့ကြမယ်",
        10: "🇷🇺 Lesson 10: Farewell (Casual)\n\nПока (ပါ-ကား) - တာ့တာ"
    }

    # --- စမ်းသပ်ရန်အတွက် Logic ---
    # လက်ရှိ မိနစ်ကို ၅ နဲ့စားပြီး သင်ခန်းစာ နံပါတ်ထုတ်ယူခြင်း
    # ဥပမာ - မိနစ် ၅ မှာ Lesson 1၊ မိနစ် ၁၀ မှာ Lesson 2၊ မိနစ် ၁၅ မှာ Lesson 3 ပို့ပါမယ်။
    now = datetime.datetime.now()
    current_minute = now.minute
    lesson_index = (current_minute // 5) + 1
    
    # သင်ခန်းစာ နံပါတ် ၁၀ ကျော်သွားရင် ပြန်စဖို့ (သို့မဟုတ်) default Lesson 1 ပေးဖို့
    return lessons.get(lesson_index, lessons[1])

def send_message(text):
    now = datetime.datetime.now() + datetime.timedelta(hours=6, minutes=30)
    current_time = now.strftime("%H:%M:%S")
    
    # စမ်းသပ်နေစဉ်အတွင်း အချိန်ကိုပါ တစ်ခါတည်း ပြပေးခြင်း
    formatted_text = f"🕒 <b>ပို့လွှတ်ချိန်: {current_time}</b>\n\n{text}"
    
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"{formatted_text}\n\n---\nMioRussianLanguage Center",
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
