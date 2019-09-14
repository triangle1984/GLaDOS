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
    if "text" in dir(event):
        text = event.text.split()
        try:
            zapros = text[0].lower()
        except IndexError:
            continue
        if zapros == "калькулятор":
            otvet = calc(text)
        elif zapros == "погода":
            otvet = weather(text)
        elif zapros == "слава":
            otvet = "украине"
        elif zapros in ["привет", "ку", "зиг", "споки", "спокойной"]:
            otvet = answer(text)
        elif zapros == "off" and event.user_id == 367919273:
            sys.exit()
        elif zapros == "help" or zapros == "хелп":
            otvet = help
        elif zapros == "красилов":
            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                             message="Krasyliv")
        elif zapros == "каты":
            cats(vk, text, event, upload)
        elif zapros == "переводчик":
            otvet = translit(text, vk)
    if otvet:
        if "chat_id" in dir(event):
            vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),
                            message=otvet)
            otvet = None
        else:
            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                            message=otvet)
            otvet = None


