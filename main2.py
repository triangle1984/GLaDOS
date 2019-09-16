from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from token2 import *
from util import *
from botutil import *
from photo import *
import vk_api, requests, sys
vk_session = vk_api.VkApi(token=token)
vk_session2 = vk_api.VkApi(token=token22)
vk = vk_session.get_api()
vk2 = vk_session2.get_api()
longpoll = VkBotLongPoll(vk_session, 183493220)
menu(vk2, longpoll, vk)
