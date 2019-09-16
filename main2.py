from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from token2 import *
from util import *
from photo import *
import vk_api, requests, sys
vk_session = vk_api.VkApi(token=token)
vk_session2 = vk_api.VkApi(token=token22)
vk = vk_session.get_api()
vk2 = vk_session2.get_api()
longpoll = VkBotLongPoll(vk_session, 183493220)
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
        # elif zapros == "/переводчик":
        #     otvet = translit(text, vk)
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
    if otvet:
        if event.chat_id:
            vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),
                             message="от бота: " + otvet["message"], attachment=otvet["attachment"])
        else:
            vk.messages.send(user_id=event.object.from_id, random_id=get_random_id(),
                            message="от бота: " + otvet["message"], attachment=otvet["attachment"])
