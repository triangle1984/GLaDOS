from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_bot.core.sql.sqlgame import *
from loadevn import *
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import vk_api
import requests
import sys
from vk_bot.core.sql.vksql import *
import pylibmc
import logging
from vk_bot.core.utils.botutil import sqlcache
import mods
"""
main.py - страничный бот и почти заброшен
в него прилетают только самые важные обновы
за кодом тут не слежу,  можете не засирать
и так знаю всю его бренность)0)
"""


def mainlobby(vk, mc, event, upload):
    events = event.type.name.lower()
    action = False
    attachmentype = False
    try:
        response = {"message": None}
        if "text" in dir(event) and "user_id" in dir(event):
            if event.from_me:
                uid = recipient
            else:
                uid = event.user_id
            if str(uid) in allowuser and "chat_id" not in dir(event):
                text = event.text.split()
                requests = [None]
                uberequests = [None]
                requests2 = [None]
                uberequests2 = [None]
                preixcommand = ("/", "!")
                try:
                    requests = text[0].lower()
                    if requests[0] in preixcommand:
                        requests2 = requests[1:]
                    uberequests2 = event.text[1:].lower()
                    uberequests = event.text.lower()
                except IndexError:
                    pass

                if event.from_me:
                    uid = recipient
                else:
                    uid = event.user_id
                mc2 = sqlcache(mc, uid)
                prefix = mc2["prefix"]
                for module in mods.modules:
                    run = False
                    if module.included and events in module.vktypes and mc2[module.available_for] and action == module.action:
                        if module.types == "command":
                            if requests2 in module.command or uberequests2 in module.uberequests:
                                run = True
                        elif module.types == "runalways":
                            run = True
                        elif module.types == "commandb":
                            command = module.getcommand(uid, requests)
                            if requests == command:
                                run = True
                        elif module.types == "specialcommand":
                            rlen = len(module.command[0])
                            if requests[:rlen] == module.command[0]:
                                run = True
                        if module.attachment:
                            if attachmentype != module.attachment:
                                run = False
                        if run:
                            module = module(vk, vk, upload)
                            module.givedata(uid=uid, text=text, event=event, mc2=mc2,
                                            prefix=prefix, peer=event.peer_id, mc=mc)
                            module.makeothervariables()
                            module.main()

    except KeyboardInterrupt:
        sys.exit()


def checkthread(futures):
    for x in as_completed(futures):
        if x.exception() != None:
            logging.error(x.exception())
        futures.remove(x)


def run():
    vk_session = vk_api.VkApi(token=token22)
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)
    longpoll = VkLongPoll(vk_session)
    mc = pylibmc.Client(["127.0.0.1"])
    pool = ThreadPoolExecutor(8)
    logging.basicConfig(level=logging.INFO)
    futures = []
    for event in longpoll.listen():
        # mainlobby(vk, mc, event, upload)
        futures.append(pool.submit(mainlobby, vk, mc, event, upload))
        pool.submit(checkthread, futures)


run()
