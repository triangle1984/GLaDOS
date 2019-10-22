#!/usr/bin/python3.7
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from loadevn import *
from util import *
from photo import Photo
from vksql import *
from botutil import *
from yourphoto import *
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from yourgroup import *
from relation import *
import pylibmc, vk_api, logging, datetime
from sqlgame import *
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
        vk_session = vk_api.VkApi(token=token)
        vk_session2 = vk_api.VkApi(token=token22)
        self.vk = vk_session.get_api()
        self.vk2 = vk_session2.get_api()
        self.upload = VkUpload(self.vk)
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
        logging.info(f"Поток закрылся через {delta.total_seconds()}")
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
        if event.object.text:
            text = event.object.text.split()
            uid = event.object.from_id
            mc2 = sqlcache(self.mc, uid)
            prefix = mc2["prefix"]
            if mc2["ban"]:
                return
            try:
                requests = text[0].lower()
                uberequests = " ".join(text[0:]).lower()
            except IndexError:
                return
            photos = Photo(self.vk2, text)
            if mc2["admins"]:
                setxp(uid, random.randint(75, 100))
                if requests == "/бан":
                    response = ban(event.object.reply_message['from_id'])
                    del mc[str(event.object.reply_message['from_id'])]
                elif requests == "/разбан":
                    unban(event.object.reply_message['from_id'])
                    del mc[str(event.object.reply_message['from_id'])]
                elif requests == "/рассылка":
                    sendall(event, text, self.vk)
                elif requests == "/шелл":
                    response = shellrun(text)
                elif requests == "/вип":
                    tableadd("vips", "id", event.object.reply_message['from_id'])
                    del mc[str(event.object.from_id)]
            for module in self.modules:
                if module.included:
                    if requests in module.command and events in module.types or module.types == "runalways":
                        module = module(self.vk, self.vk2)
                        module.givedata(uid=uid, text=text, event=event, mc2=mc2,
                                        prefix=prefix, peer=event.object.peer_id)
                        module.main()
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
                self.vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                message="Krasyliv")
            elif requests == "/каты":
                response = photos.cats()
            elif requests == "/переводчик":
                response = translit(text, self.vk)
            elif requests == "/юри":
                response = photos.yuri()
            elif requests == "/геббельс":
                response = photos.gebbels()
            elif requests == "/яой":
                response = photos.yaoi()
            elif requests == "/трапы":
                response = photos.trap()
            elif requests == "/лоли":
                response = photos.loli(self.vk2,text)
            elif requests == "/оцени":
                response = doulikethis(text)
            elif requests == "/вики":
                response = wiki(text)
            elif requests == "/махно":
                response = photos.mahno()
            elif requests == "/цитаты":
                response = citati()
            elif requests == "/калян":
                response = photos.colyan()
            elif requests == "/видео":
                response = video(self.vk2, text)
            elif requests == "/вероятность" or requests == "/шансы":
                response = chance(text)
            elif requests == "/хентай":
                response = photos.hentai()
            elif requests == "/выбери":
                response = oror(text)
            elif requests == "/повтори":
                response = repeat(text)
            elif requests == "/док" or requests == "/гиф":
                response = rdocs(self.vk, text)
            elif requests == "/ноги" or requests == "/ножки":
                response = photos.legs()
            elif requests == "/мем":
                response = photos.mem()
            elif requests == "/кто":
                response = who(self.vk, event, text)
            elif requests == "/курс":
                response = valute(text)
            elif requests == "/дата":
                response = date(text)
            elif requests == "/число":
                response = number(text)
            elif requests == "/онлайн" or requests == "/online":
                response = online(self.vk, event)
            elif requests == "/адольф" or requests == "/гитлер":
                response = photos.adolf()
            elif requests == "/префикс":
                response = update(uid,text, self.mc)
                del self.mc[str(uid)]
                mc2 = sqlcache(self.mc, uid)
            elif requests == "/жив?" or " ".join(text[0:]) == "/ ping":
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
                response = forward(event, self.vk, session, upload)
            elif requests == "/хес" or requests == "/хесус":
                response = photos.hesus()
            elif uberequests == "/аниме на фото":
                response = anime(event)
            elif requests == "/айди":
                response = nametoid()
            elif requests == "/идеи":
                response = tasks()
            elif requests == "/приветствие":
                response = hello(chathello, event, self.vk, text)
            elif requests == "/encodeqr":
                response = qrcode(text, self.vk, upload, session)
            elif requests == "/decodeqr":
                response = encodeqr(event)
            elif "".join(text)[:7] == "/группы":
                response = groupadd(self.vk, uid, text, mc2, number=text)
                del self.mc[str(uid)]
            elif requests == "/отношения":
                response = relation(event, self.vk, text)
            elif requests == "/длина":
                response = lentomsg(text)
            elif requests == "/пароль":
                response = genpass(text)
            elif requests == "/посты":
                response = postsearch(self.vk2, text)
            elif uberequests == "/чекни донат":
                response = checkdonate(uid)
            elif requests == getcommand(uid, requests):
                response = sendyourphoto(self.vk2, text, uid, requests)
            elif requests == "/казино":
                response = economygame1(uid, text)
            elif requests == "/экономика":
                response = economylobby(uid, mc2, text)
            elif uberequests == "/холодная война":
                response = nuke()
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
                status(self.vk2, self.message)
            setmessages(uid)
            givemoney(uid,mc2)
        except TypeError:
            return
        except NameError:
            None
logging.basicConfig(level=logging.INFO)
t = Main(token, token22)
t.run()
