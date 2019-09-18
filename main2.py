#!/usr/bin/python3.7
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from token2 import *
from util import *
from photo import *
from smeh import *
import vk_api, requests, sys
vk_session = vk_api.VkApi(token=token)
vk_session2 = vk_api.VkApi(token=token22)
vk = vk_session.get_api()
vk2 = vk_session2.get_api()
longpoll = VkBotLongPoll(vk_session, 183493220)
try:
    for event in longpoll.listen():
        otvet = None
        if event.object.text:
            text = event.object.text.split()
            try:
                zapros = text[0].lower()
            except IndexError:
                continue
            if zapros == "/калькулятор":
                otvet = calc(text)
            elif zapros == "/погода":
                otvet = weather(text)
            elif zapros == "слава":
                otvet = {"message":"🇺🇦украине🇺🇦", "attachment":None}
            elif zapros in ["привет", "ку", "зиг", "споки", "спокойной"]:
                otvet = answer(text)
            elif zapros == "/off" and event.user_id == 367919273:
                sys.exit()
            elif zapros == "/help" or zapros == "/хелп":
                otvet = {"message":help, "attachment":None}
            elif zapros == "/красилов":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                message="Krasyliv")
            elif zapros == "/каты":
                otvet = cats(vk2)
            elif zapros == "/переводчик":
                otvet = translit(text, vk)
            elif zapros == "/юри":
                otvet = yuri(vk2)
            elif zapros == "/геббельс":
                otvet = gebbels(vk2)
            elif zapros == "/яой":
                otvet = yaoi(vk2)
            elif zapros == "/трапы":
                otvet = trap(vk2)
            elif zapros == "/лоли":
                otvet = loli(vk2)
            elif zapros == "/оцени":
                otvet = doulikethis(text)
            elif zapros == "/вики":
                otvet = wiki(text)
            elif zapros == "/махно":
                otvet = mahno(vk2)
            elif zapros == "/цитаты":
                otvet = citati(vk2)
            elif zapros == "/калян":
                otvet = colyan(vk2)
            elif zapros == "/видео":
                otvet = video(vk2, text)
            elif zapros == "/вероятность" or zapros == "/шансы":
                otvet = chance(text)
            elif zapros == "/хентай":
                otvet = hentai(vk2)
            elif zapros == "/выбери":
                otvet = oror(text)
            elif zapros == "/смех":
                otvet = smex(text)
            elif zapros == "/повтори":
                otvet = repeat(text)
        if otvet:
            if event.chat_id:
                vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),
                                message=otvet["message"], attachment=otvet["attachment"])
            else:
                vk.messages.send(user_id=event.object.from_id, random_id=get_random_id(),
                                message=otvet["message"], attachment=otvet["attachment"])
except KeyboardInterrupt:
    sys.exit()
