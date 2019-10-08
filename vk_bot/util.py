import vk_api, math, random, requests, base64, wikipedia, subprocess
from vk_api.utils import get_random_id
from token2 import group_idd, apinews
from vksql import *
from vk_api import VkUpload
from datetime import timedelta
import pyPrivnote
wikipedia.set_lang("ru")
helpspisok = ["/help", "/хелп", "/начать", "/помощь", "/команды", "/старт"]
help = """Дроу. Ето бот команды овощей. Возможности:
🧾Калькулятор - передавать значения через пробел: /калькулятор 2 + 2
☁/погода - мона писать город на русском, не сработает = ингиш, игнор = ошибка
❤привет\споки - :З
🐱 /каты - скинет пикчу котика или неко
🇬🇧 - /переводчик
🏳‍🌈/яой, юри, трапы, геббельс, махно, калян, мем, ноги\ножки, адольф\гитлер, хес - сделает вашу жизнь лучше 🌚
а так же, ключ -c может указать количество пикч.
Например: /яой -c 7
👍🏻/оцени - оценка по 10ти бальной шкале
📚 /вики - информация из вики
🎬/видео название - рандомное видео с вашим названием
✔/вероятность /шансы - вероятность чего либо
🌚/хентай - 🌚🌚🌚
❓/выбери - /выбери огурцы с молоком или гречка с кетчупом
🐴/смех - генератор смеха, с -h выдаст справку
👅/повтори - повторение вашего сообщения
💾/гиф или /док - скинет вам гифку или документ с переданным названием
&#128064;/кто - выбирает рандомного человека в беседе под вашим предлогом
&#128181;/курс - курс доллара и евро
⚰/дата - когда произойдет переданное вами событие
🎲/число - выбрать число из диапазона. Пример: /число 1 500
&#128101;/онлайн - покажет онлайн беседы
🔔/призыв - призовет всех участников в беседе
👤/префикс - как вас будет называть бот
💱/конвертер - конвертер валюты, с usd и eur (/конвертер 5000 usd)
🔒/зашифровать <ваш текст> /расшифровать <Текст, который вернул бот после шифрования>
📰/новость - покажет последние новости
&#128102;/профиль - информация о вашем профиле
📝/бинарный0/1: 0 - зашифрует текст в бинарный код, а 1 - расшифрует
🏝/перешли - пересылает фото для сохранения
🔍/аниме на фото - подскажет вам аниме изображенное на фото
👋🏻/приветствие - устанавливает приветствие для новых участников беседы
📚/альбомы - настройка вашего личного альбома. Вызов без всего скинет справку
📋/айди - скинуть цифровой айди группы\человека, например: /айди slava_air
🔒/encodeqr - зашифрует текст в qrcode , /decodeqr - расшифрует qrcode
📁/группы - настройка ваших групп, из которых будет браться рандомный пост
✍🏻/длина - сколько символов в вашем сообщение, не считая саму команду
для админов:
    ⛔/бан - забанит юзера(Бот не будет ему отвечать)
    ✅/разбан - следовательно, разбанит
    👑/вип - дает випку юзеру
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
        if x > 999 or y > 999:
            return
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
def translit(text, vk=False, english=False):
    apikey = "trnsl.1.1.20190508T201810Z.385ebfa1e596baa0.90672cf8655555b1b51ced31b03c2e8bb9bde46c"
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    url2 = "https://translate.yandex.net/api/v1.5/tr.json/detect"
    params = {"key": apikey,
                "text":text[1:]}
    r = requests.get(url2, params=params)
    encode = r.json()
    lang = f"{encode['lang']}-ru"
    if english:
        lang = "ru-en"
    params = {"key": apikey,
            "text":text[0:],
            "lang":lang}
    r = requests.get(url, params=params)
    encode = r.json()
    try:
        if vk:
            encode = " ".join(encode["text"][1:])
            return {"message":"Перевод: {}".format(encode),}
    except:
        return
    return encode["text"][0]
def weather(text):
    try:
        qr = text[1]
    except:
        return
    q = translit(text=qr, english=True); q.lower()
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
    try:
        video = vk.video.search(q=text, count=50)
        video = random.choice(video["items"])
        videoid = video["id"]
        videoow = video["owner_id"]
    except IndexError:
        return {"message":"ничо не найдено"}
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
    callid = vk.messages.getConversationMembers(peer_id=event.object.peer_id)
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
def ping():
    return {"message":"JA JA Führer"}
def convvalute(text):
        api = "https://www.cbr-xml-daily.ru/daily_json.js"
        r = requests.get(api)
        encode = r.json()
        usd = encode["Valute"]["USD"]["Value"]
        eur = encode["Valute"]["EUR"]["Value"]
        try:
            val = float(text[1])
        except ValueError:
            return {"message": "Ты должен ввести цифру!\nНапример: /конвертер 5 usd"}
        if val <= 0:
            return {"message": "Число должно быть больше 0!"}
        elif text[2] == "usd":
            return {"message": f"💰{'%g'%val}$:\nВ рублях: {round(val*usd, 3)}₽\nВ евро: {round(val*usd/eur, 3)}€"}
        elif text[2] == "eur":
            return {"message": f"💰{'%g'%val}€:\nВ рублях: {round(val*eur, 3)}₽\nВ долларах:{round(val*eur/usd, 3)}$"}
        else:
            return {"message": "Выбери: usd или eur!\nНапример: /конвертер 5 usd"}
def news():
    api = 'https://newsapi.org/v2/top-headlines'
    params = {
                'apiKey': apinews,
                'country': 'ru'
                }
    r = requests.get(api, params=params, timeout=5)
    encode = r.json()
    newsjson = random.choice(encode['articles'])
    return {'message': f"{newsjson['title']}\n\n{newsjson['description']}\n\nПолную статью вы можете прочитать здесь: {newsjson['url']}"}
def vkbase64(text, encode=False, decode=False):
    text = " ".join(text[1:])
    try:
        if encode:
            result = base64.b64encode(bytes(text, 'utf-8'))
        else:
            result = base64.b64decode(text)
    except:
        return {"message":"!error"}
    return {"message":result.decode('utf-8')}
def profile(uid, mc2):
    msg = checktable('messages', 'id', uid)["msg"]
    if mc2["admins"]:
        user = "Админ😎"
    elif mc2["vips"]:
        user = "Вип🤵"
    else:
        user = "Юзер"
    G = checktable("economy","id", uid)["money"]
    return {"message": f"""Твой профиль:
👦| Роль: {user}
🔑| Префикс: {mc2['prefix']}
📃| Айди: id{uid}
✉ | Сообщения: {msg}
💰| G: {G}$ """}
def shellrun(text):
    text = " ".join(text[1:])
    try:
        result = subprocess.check_output(text, shell=True, encoding="utf-8")
    except:
        return {"message":"!error"}
    return {"message":result}
def text_to_bits(text):
    text = ' '.join(text[1:])
    bits = bin(int.from_bytes(text.encode('utf-8', 'surrogatepass'), 'big'))[2:]
    encode = bits.zfill(8 * ((len(bits) + 7) // 8))
    return {"message": str(encode)}
def text_from_bits(text):
    text = " ".join(text[1:])
    try:
        n = int(text, 2)
    except ValueError:
        return {"message": "Введи двоичный код!"}
    decode = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass') or '\0'
    return {"message": decode}
def forward(event, vk, session, upload):
    try:
        attachments = []
        image_url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
        image = session.get(image_url, stream=True)
        photo = upload.photo_messages(photos=image.raw)[0]
        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
        return {"message":"Держи!", "attachment": ','.join(attachments)}
    except IndexError:
        return {"message":"Мне нужно фото!"}
def anime(event):
    try:
        image_url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
        api = f'https://trace.moe/api/search'
        params = {
            'url': image_url
        }
        r = requests.get(api, params=params)
        encode = r.json()
        name = encode["docs"][0]["title_english"]
        episode = encode["docs"][0]["episode"]
        chance = round(encode['docs'][0]["similarity"] * 100)
        sec = round(encode["docs"][0]["from"])
        time = timedelta(seconds = sec)
        return {"message": f"""Я думаю это: {name}
        Серия: {episode}
        Точность: {chance}%
        Тайминг: {time}"""}
    except IndexError:
        return {"message":"Мне нужно фото!"}
def hello(chathello, event, vk, text):
    text = " ".join(text[1:])
    if event.object['attachments']:
        vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),  message="Никаких вложений! Только текст")
    elif len(text) > 500:
        vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),  message="Не больше 500 знаков!")
    else:
        response = hellosql(chathello, event.chat_id, text)
        return {"message": f"Вы установили приветствие: \"{text}\""}
def nametoid(vk, text):
    try:
        text = text[1]
        result = vk.utils.resolveScreenName(screen_name=text)
        if result["type"] == "group":
            result = "-" + str(result["object_id"])
        else:
            result = result["object_id"]
    except KeyboardInterrupt:
        return {"message":"!error"}
    return {"message":f"Айди: {result}"}
def tasks():
    ltasks = """🚫мать панель
    ✅рассылка
    🚫ооп
    🚫многопоток
    🚫работа с пикчами
    🚫экономика\рпг
    🚫кеш
    ✅несколько личных альбомов для випов
    ✅отношения с детоводством
    ✅автоконвентор айди в тех же альбомах
    ✅список идей
    ✅приветствие
    ✅личные альбомы
    ✅аниме на фото"""
    return {"message":ltasks}
def qrcode(text, vk, upload, session):
    try:
        attachments = []
        text = " ".join(text[1:])
        image_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={text}"
        image = session.get(image_url, stream=True)
        photo = upload.photo_messages(photos=image.raw)[0]
        attachments.append('photo{}_{}'.format(photo['owner_id'], photo['id']))
        return {"message":"Держи!", "attachment": ','.join(attachments)}
    except vk_api.exceptions.ApiError:
        return {"message":"Только текст!"}
def encodeqr(event):
    try:
        image_url = event.object['attachments'][0]['photo']['sizes'][-1]['url']
        api = "http://api.qrserver.com/v1/read-qr-code/"
        params = {
            'fileurl' : image_url
        }
        r = requests.get(api, params=params)
        encode = r.json()
        if encode[0]['symbol'][0]["data"] == None:
            return {"message":"Не вижу здесь qrcode"}
        else:
            return {"message":encode[0]['symbol'][0]["data"]}
    except:
        return {"message":"Мне нужно фото!"}
def lentomsg(text):
    text = " ".join(text[1:])
    length = len(text)
    return {"message": f"Символов в сообщение: {length}"}
def gethistorytols(vk, event):
    history = vk.messages.getHistory(count=0, user_id=event.user_id)["count"]
    return {"message":f"сообщений в лс: {history}"}
def genpass(text):
    try:
        length = int(text[1])
    except:
        length = 64
    text = f"openssl rand -base64 {length}"
    result = subprocess.check_output(text, shell=True, encoding="utf-8")
    url = pyPrivnote.create_note(result)
    return {"message": f"Пароль тута: {url} . Ссылка на сгорающую записку, которая удалится после просмотра кем либо"}
