import vk_api, requests, math, random, os
from vk_api.utils import get_random_id
import wikipedia
wikipedia.set_lang("ru")
help = """Дроу. Ето бот от *slava_a_i_r(андрея) Возможности:
🧾Калькулятор - передавать значения через пробел: /калькулятор 2 + 2
☁/погода - мона писать город на русском, не сработает = ингиш, игнор = ошибка
❤привет\споки - :З
🐱 /каты - скинет пикчу котика или неко
🇬🇧 - /переводчик
🏳‍🌈/яой, юри, трапы, геббельс, махно - сделает вашу жизнь лучше 🌚
👍🏻/оцени - оценка по 10ти бальной шкале
📚 /вики - информация из вики
🎬/видео название - рандомное видео с вашим названием
✔/вероятность /шансы - вероятность чего либо
🌚/хентай - 🌚🌚🌚
❓/выбери - /выбери огурцы с молоком или гречка с кетчупом
🐴/смех - генератор смеха, без аргументов или с неправильными -  выдаст справку
👅/повтори - повторение вашего сообщения
💾/гиф или /док - скинет вам гифку или документ с переданным названием
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
    return {"message":"Ваш результат: {}".format(result), "attachment": None}
def translit(text, vk=None):
        apikey = "trnsl.1.1.20190508T201810Z.385ebfa1e596baa0.90672cf8655555b1b51ced31b03c2e8bb9bde46c"
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        params = {"key": apikey,
                "text":text[0:],
                "lang":"ru-en"}
        r = requests.get(url, params=params)
        encode = r.json()
        # if vk:
        #     encode = " ".join(encode["text"][1:])
        #     return {"message":"Перевод: {}".format(encode),"attachment": None}
        return encode["text"][0]
def weather(text):
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
    return {"message":f"""Город: {qr}
    🌥Погода: {w}
    🌡Температура: {temp}°
    💧Влажность: {vlaga}
    💨Скорость ветра: {wind}м/с""",
    "attachment": None}
def answer(text):
    zapros = text[0].lower()
    if zapros == "споки" or zapros == "спокойной":
        answer = ["Спотьки", "Спокойной ночи", "Спи, но я приду и выебу тебя историей аир"
                  ,"Сладких снов", "Эротишных снов🌚🌚🌚"]
    else:
        answer = ["Кук", "зиг хайль", "куку нахуй",
                   "🇺🇦слава украине🇺🇦", "здравствуй", "здравия желаю"]
    return {"message":random.choice(answer),"attachment": None}
def doulikethis(text):
    osenka = random.randint(0, 10)
    text = " ".join(text[1:])
    return {"message": f"Моя оценка на {text}: {osenka}/10", "attachment": None}
def wiki(text):
    text = " ".join(text[1:])
    try:
        wikiotvet = wikipedia.summary(text, sentences=3)
        if len(wikiotvet) < 355:
            wikiotvet = wikipedia.summary(text, sentences=6)
    except wikipedia.exceptions.DisambiguationError:
        wikiotvet = "точнее, пожалуйста"
    except wikipedia.exceptions.PageError:
        wikiotvet = "такого нет"
    return {"message":wikiotvet, "attachment":None}
def video(vk, text):
    text = " ".join(text[1:])
    video = vk.video.search(q=text, count=50)
    try:
        videor = random.choice(video["items"])
    except:
        return
    videoid = videor["id"]
    videoow = videor["owner_id"]
    video = f"video{videoow}_{videoid}"
    return{"message": f"Ведосик по заказу - {text}:", "attachment":video}
def chance(text):
    text = " ".join(text[1:])
    rnd =  random.randint(0, 100)
    message = f"Вероятность {text} равна {rnd}%"
    return {"message":message, "attachment": None}
def oror(text):
    text = " ".join(text[1:])
    text = random.choice(text.split("или"))
    return {"message":f"я выбираю: {text}", "attachment": None}
def repeat(text):
    text = " ".join(text[1:])
    return{"message": text, "attachment": None}
def rdocs(vk, text):
    text = " ".join(text[1:])
    docs = vk.docs.search(q=text, count=100)
    try:
        docs = random.choice(docs["items"])
    except:
        return
    docsid = docs["id"]
    docsow = docs["owner_id"]
    docs = f"doc{docsow}_{docsid}"
    return{"message": f"Гифка/документ по заказу - {text}:", "attachment":docs}
