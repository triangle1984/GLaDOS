import vk_api, math, random, os, datetime, time, requests
from vk_api.utils import get_random_id
import wikipedia
from token2 import group_idd
wikipedia.set_lang("ru")
helpspisok = ["/help", "/хелп", "/начать", "/помощь", "/команды"]
help = """Дроу. Ето бот команды овощей. Возможности:
🧾Калькулятор - передавать значения через пробел: /калькулятор 2 + 2
☁/погода - мона писать город на русском, не сработает = ингиш, игнор = ошибка
❤привет\споки - :З
🐱 /каты - скинет пикчу котика или неко
🇬🇧 - /переводчик
🏳‍🌈/яой, юри, трапы, геббельс, махно, калян, мем, ноги\ножки, адольф\гитлер - сделает вашу жизнь лучше 🌚
а так же, ключ -c может указать количество пикч.
Например: /яой -c 7
👍🏻/оцени - оценка по 10ти бальной шкале
📚 /вики - информация из вики
🎬/видео название - рандомное видео с вашим названием
✔/вероятность /шансы - вероятность чего либо
🌚/хентай - 🌚🌚🌚
❓/выбери - /выбери огурцы с молоком или гречка с кетчупом
🐴/смех - генератор смеха, без аргументов или с неправильными -  выдаст справку
👅/повтори - повторение вашего сообщения
💾/гиф или /док - скинет вам гифку или документ с переданным названием
&#128064;/кто - выбирает рандомного человека в беседе под вашим предлогом
&#128181;/курс - курс доллара и евро
⚰/дата - когда произойдет переданное вами событие
🎲/число - выбрать число из диапазона. Пример: /число 1 500
&#128101;/онлайн - покажет онлайн беседы
🔔/призыв - призовет всех участников в беседе
👤/префикс - как вас будет называть бот
для админов:
    ⛔ - /бан - забанит юзера(Бот не будет ему отвечать)
    ✅ - /разбан - следовательно, разбанит
github.com/anar66/vk-bot
"""
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
    return {"message":"Ваш результат: {}".format(result), }
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
            return {"message":"Перевод: {}".format(encode),}
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
    return {"message":f"""Город: {q}
    🌥Погода: {w}
    🌡Температура: {temp}°
    💧Влажность: {vlaga}
    💨Скорость ветра: {wind}м/с""",
    }
def answer(text):
    zapros = text[0].lower()
    if zapros == "споки" or zapros == "спокойной":
        answer = ["Спотьки", "Спокойной ночи", "Спи, но я приду и выебу тебя историей аир"
                  ,"Сладких снов", "Эротишных снов🌚🌚🌚"]
    else:
        answer = ["Кук", "зиг хайль", "куку нахуй",
                   "🇺🇦слава украине🇺🇦", "здравствуй", "здравия желаю"]
    return {"message":random.choice(answer),}
def doulikethis(text):
    osenka = random.randint(0, 10)
    text = " ".join(text[1:])
    return {"message": f"Моя оценка на {text}: {osenka}/10", }
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
    return {"message":wikiotvet}
def video(vk, text):
    text = " ".join(text[1:])
    max_num = vk.video.search(q=text, count=0)['count']
    while 1:
        num = random.randint(0, max_num)
        if num > 4000:
            continue
        else:
            break
    try:
        video = vk.video.search(q=text, count=1, offset=num)["items"][0]
    except KeyboardInterrupt:
        return
    except IndexError:
        return{"message": "Ничего не найдено!"}
    videoid = video["id"]
    videoow = video["owner_id"]
    video = f"video{videoow}_{videoid}"
    return{"message": f"Ведосик по заказу - {text}:", "attachment":video}
def chance(text):
    text = " ".join(text[1:])
    rnd =  random.randint(0, 100)
    message = f"Вероятность {text} равна {rnd}%"
    return {"message":message, }
def oror(text):
    text = " ".join(text[1:])
    text = random.choice(text.split("или"))
    return {"message":f"я выбираю: {text}", }
def repeat(text):
    text = " ".join(text[1:])
    return{"message": text, }
def rdocs(vk, text):
    text = " ".join(text[1:])
    try:
        docs = vk.docs.search(q=text, count=200)
        docs = random.choice(docs["items"])
    except IndexError:
        return{"message": "Ничего не найдено!"}
    docsid = docs["id"]
    docsow = docs["owner_id"]
    docs = f"doc{docsow}_{docsid}"
    return{"message": f"Гифка/документ по заказу - {text}:", "attachment":docs}
# def nowtime():
#     vrema = datetime.datetime.now()
#     return f"{vrema.day} числа, {vrema.hour}:{vrema.minute}"
def status(vk, msgcount):
    vk.status.set(text=f"✉сообщений: {msgcount}", group_id=group_idd)

def who(vk, event, text):
    try:
        whotext = ' '.join(text[1:])
        whoid = random.choice(vk.messages.getConversationMembers(peer_id=event.object.peer_id)['profiles'])
        whofirstname = whoid['first_name']
        wholastname = whoid['last_name']
        whoidstr = whoid['id']
        return {"message":f"Кто {whotext}? Я думаю, это @id{whoidstr} ({whofirstname} {wholastname})", }
    except:
        return {"message":"Для работы этой команды боту нужна админка в беседе!", }
def valute(text):
        api = "https://www.cbr-xml-daily.ru/daily_json.js"
        r = requests.get(api)
        encode = r.json()
        usd = encode["Valute"]["USD"]["Value"]
        eur = encode["Valute"]["EUR"]["Value"]
        return {"message":"Доллар: {}₽\nЕвро: {}₽".format(usd, eur), }
def date(text):
    text = " ".join(text[1:])
    day = random.randint(1,31)
    moth = random.randint(1,12)
    year = random.randint(2019, 2100)
    when = year-2019
    event = f"Дата {text}: {day}.{moth}.{year}, через {when} лет"
    return {"message":event, }
def number(text):
    try:
        x = int(text[1])
        y = int(text[2])
        nubmer2 = random.randint(x, y)
    except:
        return
    return {"message":f"Число: {nubmer2}"}
def online(vk, event):
    onlinenumber = 0
    onlinelist = []
    onlineid = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['profiles']
    for a in onlineid:
        if a['online'] == 1:
            onlinenumber+=1
            onlinelist.append(f"{str(onlinenumber)}. {a['first_name']} {a['last_name']}")
    onlinejoin = "\n".join(onlinelist)
    return {"message":f"Участники онлайн:\n{onlinejoin}"}
def callall(vk, event):
    calllist = []
    callid = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['profiles']
    for a in callid:
        calllist.append(f"@id{str(a['id'])} ({a['first_name']} {a['last_name']})")
    calljoin = ", ".join(calllist)
    return {"message":f"Я ПРИЗЫВАЮ ВАС:\n{calljoin}"}
def getusername(vk, uid):
    try:
        requests = vk.users.get(user_ids=uid, fields="first_name")
    except vk_api.exceptions.ApiError:
        return
    response = requests[0]["first_name"]
    return response
def kick(vk, event):
    checkadmin = vk.messages.getConversationMembers(peer_id=event.object.peer_id)['items']
    for a in checkadmin:
        try:
            if a['is_admin'] == True:
                vk.messages.removeChatUser(chat_id=event.chat_id, user_id=event.object.reply_message['from_id'])
            else:
                None
        except TypeError:
            None
        except vk_api.exceptions.ApiError:
            return {'message':"Вы не можете кикнуть этого пользователя!"}
        except KeyError:
            None
