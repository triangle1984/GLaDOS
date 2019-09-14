import vk_api, requests
from vk_api.utils import get_random_id
import math
def calc(vk, text, event):
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
    elif encalc == "**" or encalc == "степень":
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
    if "chat_id" in dir(event):
        vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),
                        message=f"Ваш результат: {result}")
    else:
        vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                            message=f"Ваш результат: {result}")
def translit(text, vk=None, event=None):
        apikey = "trnsl.1.1.20190508T201810Z.385ebfa1e596baa0.90672cf8655555b1b51ced31b03c2e8bb9bde46c"
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        params = {"key": apikey,
                "text":text,
                "lang":"ru-en"}
        r = requests.get(url, params=params)
        encode = r.json()
        if vk:
            if "chat_id" in dir(event):
                vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),
                                message=f"Перевод: {text}")
            else:
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                    message=f"Ваш результат: {text}")
        else:
            return encode["text"][0]
def weather(vk, text, event):
    q = text[1]
    q = translit(text=q); q.lower()
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
    vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                     message=f"""Город: {q}
            Погода: {w}
            Температура: {temp}°
            Влажность: {vlaga}
            Скорость ветра: {wind}м/с""")
