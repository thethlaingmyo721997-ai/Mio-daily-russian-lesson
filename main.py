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
        
        # Gist ID သို့မဟုတ် Token မှားနေရင် 404/401 ပြပါလိမ့်မယ်
        if r.status_code != 200:
            print(f"Gist Access Error: Status {r.status_code}")
            return 1
            
        gist_data = r.json()
        # file data ကို ယူတဲ့နေရာမှာ ပိုပြီး စိတ်ချရအောင် ရေးထားပါတယ်
        files = gist_data.get('files', {})
        target_file = files.get('lesson_counter.txt')
        
        if target_file:
            return int(target_file['content'])
        else:
            print("Error: 'lesson_counter.txt' not found in Gist")
            return 1
    except Exception as e:
        print(f"Exception: {e}")
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
    # Lesson ၁ ကနေ ၉၀ အထိ Mio ရဲ့ သင်ခန်းစာတွေ ဒီမှာ ရှိရပါမယ်
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
        30: "🇷🇺 Lesson 30: Hundred\n\nWord: Сто (စတိုး)\nMeaning: တစ်ရာ",
        31: "🇷🇺 Lesson 31: Father\n\nWord: Папа (ပါး-ပါး)\nMeaning: အဖေ",
        32: "🇷🇺 Lesson 32: Mother\n\nWord: Мама (မား-မား)\nMeaning: အေမ",
        33: "🇷🇺 Lesson 33: Family\n\nWord: Семья (ဆင်မ်-ယား)\nMeaning: မိသားစု",
        34: "🇷🇺 Lesson 34: Today\n\nWord: Сегодня (စီး-ဗိုး-ဒနီး-ယာ)\nMeaning: ဒီနေ့",
        35: "🇷🇺 Lesson 35: Tomorrow\n\nWord: Завтра (ဇားဖ်-တြာ)\nMeaning: မနက်ဖြန်",
        36: "🇷🇺 Lesson 36: Yesterday\n\nWord: Вчера (ဖ်ချီ-ရား)\nMeaning: မနေ့က",
        37: "🇷🇺 Lesson 37: Home\n\nWord: Дом (ဒုမ်း)\nMeaning: အိမ်",
        38: "🇷🇺 Lesson 38: School\n\nWord: Школа (ရှကိုး-လား)\nMeaning: ကျောင်း",
        39: "🇷🇺 Lesson 39: Work\n\nWord: Работа (ရာ-ဘိုး-တာ)\nMeaning: အလုပ်",
        40: "🇷🇺 Lesson 40: I want\n\nWord: Я хочу (ယာ ဟာ-ချူး)\nMeaning: ကျွန်တော် အလိုရှိတယ်",
        41: "🇷🇺 Lesson 41: Help\n\nWord: Помогите (ပါ-မာ-ဂီး-ကျီ)\nMeaning: ကူညီပါဦး",
        42: "🇷🇺 Lesson 42: Where?\n\nWord: Где? (ဂဂျဲ?)\nMeaning: ဘယ်မှာလဲ?",
        43: "🇷🇺 Lesson 43: Left\n\nWord: Налево (နာ-လျဲ-ဗား)\nMeaning: ဘယ်ဘက်",
        44: "🇷🇺 Lesson 44: Right\n\nWord: Направо (နာ-ပရား-ဗား)\nMeaning: ညာဘက်",
        45: "🇷🇺 Lesson 45: Straight\n\nWord: Прямо (ပရျား-မာ)\nMeaning: တည့်တည့်",
        46: "🇷🇺 Lesson 46: Food\n\nWord: Еда (ယီ-ဒါး)\nMeaning: အစားအစာ",
        47: "🇷🇺 Lesson 47: Water\n\nWord: Вода (ဗာ-ဒါး)\nMeaning: ရေ",
        48: "🇷🇺 Lesson 48: Bread\n\nWord: Хлеб (ခလပ်)\nMeaning: ပေါင်မုန့်",
        49: "🇷🇺 Lesson 49: Tea\n\nWord: Чай (ချိုင်း)\nMeaning: လက်ဖက်ရည်",
        50: "🇷🇺 Lesson 50: Coffee\n\nWord: Кофе (ကိုး-ဖှီ)\nMeaning: ကော်ဖီ",
        51: "🇷🇺 Lesson 51: Milk\n\nWord: Молоко (မာ-လာ-ကိုး)\nMeaning: နို့",
        52: "🇷🇺 Lesson 52: Restaurant\n\nWord: Ресторан (ရီ-စတာ-ရန်)\nMeaning: စားသောက်ဆိုင်",
        53: "🇷🇺 Lesson 53: Bill\n\nWord: Счёт (ရှော့တ်)\nMeaning: ဘေလ်ရှင်းမယ်",
        54: "🇷🇺 Lesson 54: Delicious\n\nWord: Вкусно (ဗကူး-စနာ)\nMeaning: အရသာရှိတယ်",
        55: "🇷🇺 Lesson 55: Shop\n\nWord: Магазин (မာ-ဂါ-ဇင်း)\nMeaning: ဆိုင် / ဈေးဆိုင်",
        56: "🇷🇺 Lesson 56: Price\n\nWord: Цена (စီ-နား)\nMeaning: ဈေးနှုန်း",
        57: "🇷🇺 Lesson 57: How much?\n\nWord: Сколько стоит?\nMeaning: ဘယ်လောက်ကျလဲ?",
        58: "🇷🇺 Lesson 58: Clothes\n\nWord: Одежда (အာ-ဂျဲ-ရှ်ဒါ)\nMeaning: အဝတ်အစား",
        59: "🇷🇺 Lesson 59: Shoes\n\nWord: Обувь (အိုး-ဘူဖှ်)\nMeaning: ဖိနပ်",
        60: "🇷🇺 Lesson 60: Big / Small\n\nWord: Большой / Маленький\nMeaning: ကြီးသော / သေးသော",
        61: "🇷🇺 Lesson 61: Happy\n\nWord: Счастлив (ရှတ်-စလစ်)\nMeaning: ပျော်ရွှင်သော",
        62: "🇷🇺 Lesson 62: Sad\n\nWord: Грустный (ဂရုစ်-နီ)\nMeaning: ဝမ်းနည်းသော",
        63: "🇷🇺 Lesson 63: Tired\n\nWord: Я устал (ယာ အူ-စတားလ်)\nMeaning: ကျွန်တော် ပင်ပန်းနေတယ်",
        64: "🇷🇺 Lesson 64: Weather\n\nWord: Погода (ပါ-ဂိုး-ဒါ)\nMeaning: ရာသီဥတု",
        65: "🇷🇺 Lesson 65: Hot\n\nWord: Жарко (ရှဲ-ကာ)\nMeaning: ပူတယ်",
        66: "🇷🇺 Lesson 66: Cold\n\nWord: Холодно (ဟိုး-လဒ်-နာ)\nMeaning: အေးတယ်",
        67: "🇷🇺 Lesson 67: Sun\n\nWord: Солнце (ဆိုးလ်န်-စီ)\nMeaning: နေမင်း",
        68: "🇷🇺 Lesson 68: Rain\n\nWord: Дождь (ဒိုးရှ်တ်)\nMeaning: မိုးရွာခြင်း",
        69: "🇷🇺 Lesson 69: Beautiful\n\nWord: Красиво (ကရာ-စီး-ဗား)\nMeaning: လှပတယ်",
        70: "🇷🇺 Lesson 70: Doctor\n\nWord: Врач (ဗရတ်ချ်)\nMeaning: ဆရာဝန်",
        71: "🇷🇺 Lesson 71: Pharmacy\n\nWord: Аптека (အပ်-ဂျဲ-ကာ)\nMeaning: ဆေးဆိုင်",
        72: "🇷🇺 Lesson 72: Hospital\n\nWord: Больница (ဘယ်လ်-နီး-ဆာ)\nMeaning: ဆေးရုံ",
        73: "🇷🇺 Lesson 73: Car\n\nWord: Машина (မာ-ရှီး-နား)\nMeaning: ကား",
        74: "🇷🇺 Lesson 74: Bus\n\nWord: Автобус (အပ်-တိုး-ဘုစ်)\nMeaning: ဘတ်စ်ကား",
        75: "🇷🇺 Lesson 75: Airport\n\nWord: Аэропорт (အာ-အီ-ရာ-ပို့တ်)\nMeaning: လေဆိပ်",
        76: "🇷🇺 Lesson 76: Speak\n\nWord: Говорить (ဂါ-ဗာ-ရီးတ့်)\nMeaning: ပြောဆိုသည်",
        77: "🇷🇺 Lesson 77: Russian\n\nWord: Русский (ရုစ်-ကီး)\nMeaning: ရုရှား",
        78: "🇷🇺 Lesson 78: English\n\nWord: Английский\nMeaning: အင်္ဂလိပ်",
        79: "🇷🇺 Lesson 79: Book\n\nWord: Книга (ကနီး-ဂါ)\nMeaning: စာအုပ်",
        80: "🇷🇺 Lesson 80: Music\n\nWord: Музыка (မူး-ဇီ-ကာ)\nMeaning: ဂီတ",
        81: "🇷🇺 Lesson 81: Movie\n\nWord: Кино (ကီ-နိုး)\nMeaning: ရုပ်ရှင်",
        82: "🇷🇺 Lesson 82: Time\n\nWord: Время (ဗရျဲ-မျာ)\nMeaning: အချိန်",
        83: "🇷🇺 Lesson 83: Hour\n\nWord: Час (ချပ်စ်)\nMeaning: နာရီ",
        84: "🇷🇺 Lesson 84: Minute\n\nWord: Минута (မိ-နူး-တာ)\nMeaning: မိနစ်",
        85: "🇷🇺 Lesson 85: Color\n\nWord: Цвет (စဗျက်)\nMeaning: အရောင်",
        86: "🇷🇺 Lesson 86: Red\n\nWord: Красный (ကရက်စ်-နီ)\nMeaning: အနီရောင်",
        87: "🇷🇺 Lesson 87: Blue\n\nWord: Синий (စီး-နီ)\nMeaning: အပြာရောင်",
        88: "🇷🇺 Lesson 88: Love\n\nWord: Любовь (လျူ-ဘိုးဖှ်)\nMeaning: အချစ်",
        89: "🇷🇺 Lesson 89: Peace\n\nWord: Мир (မီရ်)\nMeaning: ငြိမ်းချမ်းရေး",
        90: "🇷🇺 Lesson 90: Good luck\n\nWord: Удачи! (အူ-ဒါး-ချီ)\nMeaning: ကံကောင်းပါစေ!"
    }
    raw_content = lessons.get(idx, f"🇷🇺 Lesson {idx}\n\nContent Loading...")
    final_content = re.sub(r'Lesson \d+:', '', raw_content).strip()
    return final_content.replace('🇷🇺  ', '🇷🇺 ')

def send_message(text):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    footer = "\n\n<b>MioRussianLanguage Center</b>\n<b>Viber/Phone : +959693548605</b>"
    payload = {
        "chat_id": str(CHAT_ID).strip(),
        "text": f"{text}{footer}",
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=6, minutes=30)
    
    # စမ်းသပ်နေချိန်မှာ အချိန်ကန့်သတ်ချက်ကို ခေတ္တပိတ်ထားပါမယ် (Run workflow နှိပ်ရင် ချက်ချင်းပို့အောင်လို့ပါ)
    idx = get_current_index()
    message = get_daily_content(idx)
    send_message(message)
    update_index(idx + 1)
