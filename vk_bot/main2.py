#!/usr/bin/python3.7
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from loadevn import *
from util import *
from photo import Photo
from vk_bot.core.sql.vksql import *
from vk_bot.core.utils.botutil import *
from yourphoto import *
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from yourgroup import *
import pylibmc, vk_api, logging, datetime
from vk_bot.core.sql.sqlgame import *
from economy import *
import mods
class Main:
    def __init__(self, token, tokn22):
        self.token = token
        self.token22 = token22
        self.authorization()
        self.thread()
        self.modules = mods.modules
    def authorization(self):
        vk_session = vk_api.VkApi(token=token, api_version=5.102)
        vk_session2 = vk_api.VkApi(token=token22)
        self.vk = vk_session.get_api()
        self.vk2 = vk_session2.get_api()
        self.upload = VkUpload(vk_session)
        self.longpoll = VkBotLongPoll(vk_session, group_idd)
        self.message = 0
    def thread(self):
        self.pool = ThreadPoolExecutor(8)
        self.futures = []
    def checkthread(self):
        then = datetime.datetime.now()
        for x in as_completed(self.futures):
            if x.exception() != None:
                logging.error(x.exception())
            self.futures.remove(x)
        now = datetime.datetime.now()
        delta = now - then
        logging.debug(f"Поток закрылся через {delta.total_seconds()}")
    def run(self):
        self.mc = pylibmc.Client(["127.0.0.1"])
        for event in self.longpoll.listen():
            self.futures.append(self.pool.submit(self.lobby, event))
            self.pool.submit(self.checkthread)
    def lobby(self, event):
        events = event.type.value
        logging.debug(f"Событие: {events}")
        botmain(self.vk, event)
        response = {"message":None}
        try:
            text = event.object.text.split()
        except:
            text = []
        uid = event.object.from_id
        mc2 = sqlcache(self.mc, uid)
        prefix = mc2["prefix"]
        if mc2["ban"]:
            return
        try:
            requests = text[0].lower()
            uberequests = " ".join(text[0:]).lower()
        except IndexError:
            requests = [None]
            uberequests = [None]
        photos = Photo(self.vk2, text)
        for module in self.modules:
            run = False
            if module.included and events in module.vktypes and mc2[module.available_for]:
                if module.types == "command":
                    if requests in module.command:
                        run = True
                elif module.types == "runalways":
                    run = True
                if run:
                    module = module(self.vk, self.vk2, self.upload)
                    module.givedata(uid=uid, text=text, event=event, mc2=mc2,
                                    prefix=prefix, peer=event.object.peer_id)
                    module.main()
        if event.object.text:
            if requests in helpspisok:
                response = {"message":help}
            elif requests == "/красилов":
                self.vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                message="Krasyliv")
            elif requests == "/префикс":
                response = update(uid,text, self.mc)
                del self.mc[str(uid)]
                mc2 = sqlcache(self.mc, uid)
                prefix = mc2["prefix"]
            elif "".join(text)[:7] == "/группы":
                response = groupadd(self.vk, uid, text, mc2, number=text)
                del self.mc[str(uid)]
            elif requests == getcommand(uid, requests):
                response = sendyourphoto(self.vk2, text, uid, requests)
            elif requests == "/казино":
                response = economygame1(uid, text)
            elif requests == "/экономика":
                response = economylobby(uid, mc2, text)
            elif "".join(text)[:8] == "/альбомы":
                response = photoadd(self.vk, uid, text, mc2, number=text)
                del self.mc[str(uid)]

        try:
            if response["message"]:
                if "attachment" not in response:
                    response["attachment"] = None
                self.vk.messages.send(peer_id=event.object.peer_id, random_id=get_random_id(),
                                message=f"{prefix}, {response['message']}",
                                attachment=response["attachment"])
                self.message += 1
            setmessages(uid)
            givemoney(uid,mc2)
        except TypeError:
            return
        except NameError:
            None
logging.basicConfig(level=logging.INFO)
t = Main(token, token22)
t.run()
