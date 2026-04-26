import os
import requests
import datetime

API_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def get_daily_content():
    # ရက် ၃၀ စာ သင်ခန်းစာများ
    lessons = {
        1: "Привет (Pre-vyet) - မင်္ဂလာပါ (ရင်းနှီးသူများအကြား)",
        2: "Спасибо (Spa-see-ba) - ကျေးဇူးတင်ပါတယ်",
        3: "Пожалуйста (Pa-zhal-sta) - ရပါတယ် / ကျေးဇူးပြု၍",
        4: "Да (Da) - ဟုတ်ကဲ့ / Нет (Nyet) - မဟုတ်ဘူး",
        5: "Как дела? (Kak dye-la) - နေကောင်းလား?",
        6: "Доброе утро (Dob-ro-ye ut-ro) - မင်္ဂလာနံနက်ခင်းပါ",
        7: "Меня зовут... (Me-nya za-vut) - ကျွန်တော့်နာမည်က... ပါ",
        8: "Я понимаю (Ya po-ni-ma-yu) - ကျွန်တော် နားလည်ပါတယ်",
        9: "Я не понимаю (Ya nye po-ni-ma-yu) - ကျွန်တော် နားမလည်ပါဘူး",
        10: "Сколько стоит? (Skol-ko sto-it) - ဒါ ဘယ်လောက်လဲ?",
        11: "Где туалет? (Gdye tu-a-lyet) - အိမ်သာ ဘယ်မှာလဲ?",
        12: "Извините (Iz-vi-ni-tye) - တောင်းပန်ပါတယ် / တစ်ဆိပ်လောက်",
        13: "Хорошо (Ha-ra-sho) - ကောင်းပြီ / အိုကေ",
        14: "Плохо (Plo-ha) - မကောင်းဘူး",
        15: "Я люблю тебя (Ya lyub-lyu tyeb-ya) - မင်းကို ချစ်တယ်",
        16: "Друг (Drug) - သူငယ်ချင်း",
        17: "Вода (Va-da) - ရေ",
        18: "Хлеб (Khlyeb) - ပေါင်မုန့်",
        19: "Мама (Ma-ma) - အမေ / Папа (Pa-pa) - အဖေ",
        20: "Семья (Syem-ya) - မိသားစု",
        21: "Работа (Ra-bo-ta) - အလုပ်",
        22: "Машина (Ma-shi-na) - ကား",
        23: "Город (Go-rat) - မြို့",
        24: "Дом (Dom) - အိမ်",
        25: "Школа (Shko-la) - ကျောင်း",
        26: "Учитель (U-chi-tyel) - ဆရာ",
        27: "Книга (Kni-ga) - စာအုပ်",
        28: "Время (Vrye-mya) - အချိန်",
        29: "Сегодня (Sye-vod-nya) - ဒီနေ့",
        30: "Завтра (Zav-tra) - မနက်ဖြန်"
    }
    
    day_of_month = datetime.datetime.now().day
    content = lessons.get(day_of_month, lessons[1])
    return content

def send_message(text):
    today = datetime.datetime.now().strftime("%d %B %Y")
    # ဒီနေရာမှာ TikTok စာသားကို ဖြုတ်ထားပါတယ်
    formatted_text = f"🇷🇺 Russian Lesson for {today}\n\n{text}"
    
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": formatted_text})

if __name__ == "__main__":
    message = get_daily_content()
    send_message(message)
