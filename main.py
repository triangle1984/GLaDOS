import requests
import vk_api
import math
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from token2 import token
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        text = event.text.split()[0:]
        if text[0].lower() == "калькулятор":
            try:
                x = text[1]; x = int(x)
                encalc = text[2]; encalc = encalc.lower()
                y = text[3]; y = int(y)
            except:
                continue
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

