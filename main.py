from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from token2 import token
from util import *
from photo import *
import vk_api, requests, sys
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
upload = vk_api.VkUpload(vk_session)
otvet = None
for event in longpoll.listen():
    otvet = None
    if "text" in dir(event):
        text = event.text.split()
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
            otvet = cats(vk, upload)
        # elif zapros == "/переводчик":
        #     otvet = translit(text, vk)
        elif zapros == "/юри":
            otvet = yuri(vk, upload)
        elif zapros == "/геббельс":
            otvet = gebbels(vk, upload)
        elif zapros == "/яой":
            otvet = yaoi(vk, upload)
        elif zapros == "/трапы":
            otvet = trap(vk, upload)
        elif zapros == "/лоли":
            otvet = loli(vk, upload)
        elif zapros == "/оцени":
            otvet = doulikethis(text)
    if otvet:
        if "chat_id" in dir(event):
            vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),
                             message="от бота: " + otvet["message"], attachment=otvet["attachment"])
        else:
            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                             message="от бота: " + otvet["message"], attachment=otvet["attachment"])


