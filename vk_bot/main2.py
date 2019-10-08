#!/usr/bin/python3.7
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from token2 import *
from util import *
from photo import *
from smeh import *
import vk_api, requests
from vksql import *
from botutil import *
from yourphoto import *
from yourgroup import *
from relation import *
import pylibmc
from sqlgame import *
session = requests.Session()
vk_session = vk_api.VkApi(token=token)
vk_session2 = vk_api.VkApi(token=token22)
vk = vk_session.get_api()
vk2 = vk_session2.get_api()
upload = VkUpload(vk)
longpoll = VkBotLongPoll(vk_session, group_idd)
msgcount = 0
mc = pylibmc.Client(["127.0.0.1"])
try:
    for event in longpoll.listen():
        botmain(vk, event)
        response = {"message":None}
        if event.object.text:
            text = event.object.text.split()
            uid = event.object.from_id
            mc2 = sqlcache(mc, uid)
            if mc2["ban"]:
                continue
            try:
                requests = text[0].lower()
                uberequests = " ".join(text[0:]).lower()
            except IndexError:
                continue
            if mc2["admins"]:
                if requests == "/бан":
                    ban(event.object.reply_message['from_id'])
                elif requests == "/разбан":
                    unban(event.object.reply_message['from_id'])
                elif requests == "/рассылка":
                    sendall(event, text, vk)
                elif requests == "/шелл":
                    response = shellrun(text)
                elif requests == "/вип":
                    tableadd("vips", "id", event.object.reply_message['from_id'])
                    del mc[str(event.object.from_id)]
            if requests == "/калькулятор":
                response = calc(text)
            elif requests == "/погода":
                response = weather(text)
            elif uberequests == "слава украине":
                response = {"message":"🇺🇦героям слава🇺🇦"}
            elif requests in ["привет", "ку", "зиг", "споки", "спокойной"]:
                response = answer(text)
            elif requests in helpspisok:
                response = {"message":help}
            elif requests == "/красилов":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                message="Krasyliv")
            elif requests == "/каты":
                response = cats(vk2, text)
            elif requests == "/переводчик":
                response = translit(text, vk)
            elif requests == "/юри":
                response = yuri(vk2, text)
            elif requests == "/геббельс":
                response = gebbels(vk2, text)
            elif requests == "/яой":
                response = yaoi(vk2, text)
            elif requests == "/трапы":
                response = trap(vk2, text)
            elif requests == "/лоли":
                response = loli(vk2,text)
            elif requests == "/оцени":
                response = doulikethis(text)
            elif requests == "/вики":
                response = wiki(text)
            elif requests == "/махно":
                response = mahno(vk2, text)
            elif requests == "/цитаты":
                response = citati(vk2, text)
            elif requests == "/калян":
                response = colyan(vk2, text)
            elif requests == "/видео":
                response = video(vk2, text)
            elif requests == "/вероятность" or requests == "/шансы":
                response = chance(text)
            elif requests == "/хентай":
                response = hentai(vk2, text)
            elif requests == "/выбери":
                response = oror(text)
            elif requests == "/смех":
                response = smex(text, uid)
            elif requests == "/смехк":
                response = smex(text, uid, db=True)
            elif requests == "/повтори":
                response = repeat(text)
            elif requests == "/док" or requests == "/гиф":
                response = rdocs(vk2, text)
            elif requests == "/ноги" or requests == "/ножки":
                response = legs(vk2, text)
            elif requests == "/мем":
                response = mem(vk2, text)
            elif requests == "/кто":
                response = who(vk, event, text)
            elif requests == "/курс":
                response = valute(text)
            elif requests == "/дата":
                response = date(text)
            elif requests == "/число":
                response = number(text)
            elif requests == "/онлайн" or requests == "/online":
                response = online(vk, event)
            elif requests == "/адольф" or requests == "/гитлер":
                response = adolf(vk2, text)
            elif requests == "/префикс":
                response = update(uid,text, mc)
                del mc[str(uid)]
                mc2 = sqlcache(mc, uid)
            elif requests == "/жив?":
                response = ping()
            elif requests == "/конвертер":
                response = convvalute(text)
            elif requests == "/новость":
                response = news()
            elif requests == "/зашифровать":
                    response = vkbase64(text, encode=True)
            elif requests == "/расшифровать":
                    response = vkbase64(text, decode=True)
            elif requests == "/профиль":
                response = profile(uid, mc2)
            elif requests == "/бинарный0":
                response = text_to_bits(text)
            elif requests == "/бинарный1":
                response = text_from_bits(text)
            elif requests == "/перешли":
                response = forward(event, vk, session, upload)
            elif requests == "/хес" or requests == "/хесус":
                response = hesus(vk2, text)
            elif uberequests == "/аниме на фото":
                response = anime(event)
            elif requests == "/айди":
                response = nametoid(vk2, text)
            elif requests == "/идеи":
                response = tasks()
            elif requests == "/приветствие":
                response = hello(chathello, event, vk, text)
            elif requests == "/encodeqr":
                response = qrcode(text, vk, upload, session)
            elif requests == "/decodeqr":
                response = encodeqr(event)
            elif requests == "/группы":
                response = groupadd(vk, uid, text)
            elif requests == "/отношения":
                response = relation(event, vk, text)
            elif requests == "/длина":
                response = lentomsg(text)
            elif requests == "/пароль":
                response = genpass(text)
            elif uberequests == "/чекни донат":
                response = checkdonate(uid)
            elif requests == getcommandpost(uid):
                response = sendyourpost(vk2, text, uid)
            elif requests == getcommand(uid, requests):
                response = sendyourphoto(vk2, text, uid, requests)
            elif "".join(text)[:8] == "/альбомы":
                response = photoadd(vk, uid, text, mc2, number=text)
                del mc[str(uid)]

        try:
            if response["message"]:
                prefix = mc2["prefix"]
                if "attachment" not in response:
                    response["attachment"] = None

                if event.chat_id:
                    vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),
                                    message=f"{prefix}, {response['message']}",
                                     attachment=response["attachment"])
                else:
                    vk.messages.send(user_id=event.object.from_id, random_id=get_random_id(),
                                    message=f"{prefix}, {response['message']}",
                                    attachment=response["attachment"])
                msgcount += 1
                status(vk2, msgcount)
            setmessages(uid)
        except TypeError:
            continue
        except NameError:
            None
except KeyboardInterrupt:
    exit(0)
