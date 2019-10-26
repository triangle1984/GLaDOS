from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from sqlgame import *
from loadevn import *
from util import *
from photo import *
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import vk_api, requests, sys
from vksql import *
from yourphoto import *
import pylibmc
import logging
from botutil import sqlcache
from economy import *
import mods
def mainlobby(vk, mc, event):
    events = event.type.name.lower()
    try:
        response = {"message":None}
        if "text" in dir(event) and "user_id" in dir(event):
            if event.from_me:
                uid = recipient
            else:
                uid = event.user_id
            if str(uid) in allowuser and "chat_id" not in dir(event):
                text = event.text.split()
                try:
                    requests = text[0].lower()
                    uberequests = " ".join(text[0:]).lower()
                except IndexError:
                    return
                if event.from_me:
                    uid = recipient
                else:
                    uid = event.user_id
                mc2 = sqlcache(mc, uid)
                givemoney(uid,mc2)
                photos = Photo(vk, text)
                prefix = mc2["prefix"]
                for module in mods.modules:
                    if module.included:
                        if requests in module.command and events in module.types or module.types == "runalways":
                            module = module(vk, vk)
                            module.givedata(uid=uid, text=text, event=event, mc2=mc2,
                                            prefix=prefix, peer=event.peer_id)
                            module.main()
                if requests == "/калькулятор":
                    response = calc(text)
                elif requests == "/погода":
                    response = weather(text)
                elif requests == "/шелл" and uid == 367919273:
                    response = shellrun(text)
                elif requests == "слава":
                    response = {"message":"🇺🇦украине🇺🇦", "attachment":None}
                elif requests in ["привет", "ку", "зиг", "споки", "спокойной"]:
                    response = answer(text)
                elif requests == "/off" and event.user_id == 367919273:
                    sys.exit()
                elif requests == "/help" or requests == "/хелп":
                    response = {"message":help, "attachment":None}
                elif requests == "/красилов":
                    vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                    message="Krasyliv")
                elif requests == "/каты":
                    response = photos.cats()
                elif requests == "/переводчик":
                    response = translit(text, vk)
                elif requests == "/юри":
                    response = photos.yuri()
                elif requests == "/геббельс":
                    response = photos.gebbels()
                elif requests == "/яой":
                    response = photos.yaoi()
                elif requests == "/трапы":
                    response = photos.trap()
                elif requests == "/лоли":
                    response = photos.loli()
                elif requests == "/оцени":
                    response = doulikethis(text)
                elif requests == "/вики":
                    response = wiki(text)
                elif requests == "/махно":
                    response = photos.mahno()
                elif requests == "/цитаты":
                    response = photos.citati()
                elif requests == "/калян":
                    response = photos.colyan()
                elif requests == "/видео":
                    response = video(vk, text)
                elif requests == "/вероятность" or requests == "/шансы":
                    response = chance(text)
                elif requests == "/выбери":
                    response = oror(text)
                # elif requests == "/смех":
                #     response = smex(text, uid)
                # elif requests == "/смехк":
                #     response = smex(text, uid, db=True)
                elif requests == "/повтори":
                    response = repeat(text)
                elif requests == "/док" or requests == "/гиф":
                    response = rdocs(vk, text)
                elif requests == "/ноги" or requests == "/ножки":
                    response = photos.legs(vk,text)
                elif requests == "/мем":
                    response = photos.mem()
                elif requests == "/кто":
                    response = who(vk, event, text)
                elif requests == "/курс":
                    response = valute(text)
                elif requests == "/дата":
                    response = date(text)
                elif requests == "/число":
                    response = number(text)
                elif requests == "/адольф" or requests == "/гитлер":
                    response = photos.adolf()
                elif requests == "/префикс":
                    response = update(uid, text, mc)
                    mc2["prefix"] = " ".join(text[1:])
                elif requests == "/жив?":
                    response = ping()
                elif requests == "/конвертер":
                    response = convvalute(text)
                elif requests == "/зашифровать":
                    response = vkbase64(text, encode=True)
                elif requests == "/расшифровать":
                    response = vkbase64(text, decode=True)
                elif requests == "/айди":
                    response = nametoid(vk,  text)
                elif requests == "/идеи":
                    response = tasks()
                elif requests == "/бинарный0":
                    response = text_to_bits(text)
                elif requests == "/бинарный1":
                    response = text_from_bits(text)
                elif requests == "/длина":
                    response = lentomsg(text)
                elif requests == "/профиль":
                    response = profile(uid, mc2)
                elif requests == "/сообщений":
                    response = gethistorytols(vk, event)
                elif requests == "/пароль":
                    response = genpass(text)
                elif requests == "/капитализм":
                    response = economylobby(uid, mc2, text)
                elif uberequests == "/чекни донат":
                    response = checkdonate(uid)
                    del mc[str(uid)]
                elif requests == "/посты":
                    response = postsearch(vk, text)

                elif requests == getcommand(uid, requests):
                    response = sendyourphoto(vk, text, uid, requests)
                elif "".join(text)[:8] == "/альбомы":
                    response = photoadd(vk, uid, text,mc2, number=text)
                    del mc[str(uid)]

            try:
                if response["message"]:
                    if "attachment" not in response:
                        response["attachment"] = None
                    prefix = mc2["prefix"]
                    # if "chat_id" in dir(event):
                    #     vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),
                    #                     message="от бота: " + response["message"], attachment=response["attachment"])
                    vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                        message=f"от бота: {prefix}, {response['message']}",
                                        attachment=response["attachment"])
            except TypeError:
                return
    except KeyboardInterrupt:
        sys.exit()
def checkthread():
    global futures
    for x in as_completed(futures):
        if x.exception() != None:
            logging.error(x.exception())
        futures.remove(x)
vk_session = vk_api.VkApi(token=token22)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
mc = pylibmc.Client(["127.0.0.1"])
pool = ThreadPoolExecutor(8)
logging.basicConfig(level=logging.INFO)
futures = []
for event in longpoll.listen():
    futures.append(pool.submit(mainlobby, vk, mc, event))
    pool.submit(checkthread)
