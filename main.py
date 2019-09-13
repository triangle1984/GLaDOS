import vk_api, requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from token2 import token
from util import *
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        text = event.text.split()[0:]
        if text[0].lower() == "калькулятор":
            calc(vk, text, event)
