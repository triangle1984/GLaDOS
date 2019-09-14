import vk_api, requests, math, random, os
from vk_api.utils import get_random_id
help = """Дроу. Ето бот от андрея. Возможности:
🧾Калькулятор - передавать значения через пробел: калькулятор 2 + 2
☁погода - мона писать город на русском, не сработает = ингиш, игнор = ошибка
❤привет\споки - :З
🐱 каты - скинет пикчу котика
🇬🇧 - переводчик
github.com/anar66/vk-bot"""
def calc(text):
    try:
        x = text[1]; x = int(x)
        encalc = text[2]; encalc = encalc.lower()
        y = text[3]; y = int(y)
    except:
        return
    if encalc == "+" or encalc == "сложение":
        result = x + y
    elif encalc == "-" or encalc == "вычитание":
        result = x - y
    elif encalc == "*" or encalc == "умножение":
        result = x * y
    elif encalc == "**" or encalc == "степень" or encalc == "^":
        result = x ** y
    elif encalc == "/":
        try:
            x / y
        except ZeroDivisionError:
            result = "взорвать планету хочешь?"
    elif encalc == "корень":
        result = math.sqrt(x), math.sqrt(y)
    elif encalc == "синус":
        result = math.sin(x), math.sin(y)
    elif encalc == "косинус":
        result = math.cos(x), math.cos(y)
    else:
        return
    return "Ваш результат: {}".format(result)
def translit(text, vk=None):
        apikey = "trnsl.1.1.20190508T201810Z.385ebfa1e596baa0.90672cf8655555b1b51ced31b03c2e8bb9bde46c"
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        params = {"key": apikey,
                "text":text[0:],
                "lang":"ru-en"}
        r = requests.get(url, params=params)
        encode = r.json()
        if vk:
            encode = " ".join(encode["text"][1:])
            return "Перевод: {}".format(encode)
        else:
            return encode["text"][0]
def weather(vk, text, event):
    try:
        qr = text[1]
    except:
        return
    q = translit(text=qr); q.lower()
    apiurl = "http://api.openweathermap.org/data/2.5/find"
    appid = '22c7bf8e593c47b0cf88f390e8e5376a'
    params = {
                'q': q,
                'appid': appid,
                'units': 'metric',
                'lang': 'ru'
                }
    try:
        r = requests.get(apiurl, params=params, timeout=5)
        encode = r.json()
        w = encode['list'][0]['weather'][0]['description']
        temp = encode["list"][0]["main"]["temp"]
        vlaga = encode["list"][0]["main"]["humidity"]
        wind = encode["list"][0]["wind"]["speed"]
    except:
        return
    return f"""Город: {qr}
    🌡Погода: {w}
    🌥Температура: {temp}°
    💧Влажность: {vlaga}
    💨Скорость ветра: {wind}м/с"""
def answer(vk,text,  event):
    zapros = text[0].lower()
    if zapros == "споки":
        answer = ["Спотьки", "Спокойной ночи", "Спи, но я приду и выебу тебя историей аир"
                  ,"Сладких снов", "Эротишных снов🌚🌚🌚"]
    else:
        answer = ["Ку", "зиг хайль", "куку нахуй",
                   "слава украине", "здравствуй", "здравия желаю"]
    return random.choice(answer)
def cats(vk,text,event,vk_session):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    r = r.json()
    command = "wget {} -O test.jpg".format(r[0]["url"])
    os.system(command)
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(
        '/home/archie/vk-bot/test.jpg',
        album_id=268910446
        )
    vk_photo_url = 'photo{}_{}'.format(
            photo[0]['owner_id'], photo[0]['id'])

    if "chat_id" in dir(event):
        vk.messages.send(chat_id=event.chat_id, random_id=get_random_id()
                        , message="шавуха по заказу",
                        attachment=vk_photo_url)
    else:
        vk.messages.send(user_id=event.user_id, random_id=get_random_id()
                        , message="шавуха по заказу",
                        attachment=vk_photo_url)
