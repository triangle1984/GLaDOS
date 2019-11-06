#!/usr/bin/python3.7
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
from loadevn import *
from vk_bot.core.sql.vksql import *
from vk_bot.core.utils.botutil import *
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import pylibmc, vk_api, logging, datetime
from vk_bot.core.sql.sqlgame import *
from economy import *
import mods
class Main:
    """
    Инит главного класса, токен - токен группы
    токен22 - токен страницы, который нужен шоб кидать пикчи из пабликов
    при иницилизации класса, т.е t = Main(123, 123) - запускается усе добро
    типа авторизиации, настройки потоков и импорта модулей
    дальше можно запустить метод run(t.run()), щобы заставить бота работать
    """
    def __init__(self, token, token22):
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
        """
        Скинуть название исключения в потоке, ежели  такое произойдет
        """
        for x in as_completed(self.futures):
            if x.exception() != None:
                logging.error(x.exception())
                print(f"ошибОЧКА разраба: {x.exception()}")
            self.futures.remove(x)
            logging.info("Поток закрылся")
    def run(self):
        logging.info("Запуск бота")
        self.mc = pylibmc.Client(["127.0.0.1"])
        for event in self.longpoll.listen():
            self.futures.append(self.pool.submit(self.lobby, event))
            self.pool.submit(self.checkthread)
    def lobby(self, event):
        try:
            attachmentype = event.object.attachments[0]['type']
        except IndexError:
            attachmentype = False
        # какой ивент прислал вк. Например message_new
        events = event.type.value
        logging.info(f"Событие: {events}")
        # остатки прошлой цивилизации, скоро выкинем
        botmain(self.vk, event)
        try:
            text = event.object.text.split()
        except:
            text = []
        uid = event.object.from_id
        logging.info(f"Сообщение: {event.object.text}  От: {uid}  В: {event.object.peer_id}")
        """
        mc и mc2 = Кеш, щобы каждый раз не делать запросы в бд
        mc = сервер с мемкешем
        а mc2 = то чо он вернул на юзера, который тригернул бота
        подробнее о том, чо хранится в кеше -
        мона глянуть в core/utils/botutil.py
        """
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
        """
        Эта страшная хероборина снизу отвечает за проверку и запуск модулей
        щобы ее получше понять, читаните core/util/botutil.py
        """
        for module in self.modules:
            run = False
            if module.included and events in module.vktypes and mc2[module.available_for]:
                if module.types == "command":
                    if requests in module.command:
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
                    logging.info(f"Запуск модуля {module.__module__}")
                    module = module(self.vk, self.vk2, self.upload)
                    module.givedata(uid=uid, text=text, event=event, mc2=mc2,
                                    prefix=prefix, peer=event.object.peer_id, mc=self.mc)
                    then = datetime.datetime.now()
                    module.main()
                    now = datetime.datetime.now()
                    delta = now - then
                    logging.info(f"{module.__module__} завершил свою работу через {delta.total_seconds()} секунд")
# уровень логирования, в инфо ничего нет, а дебаг расскажет вам всю бренность
# жизни бота
logging.basicConfig(level=logging.INFO, filename="bot.log", format='%(asctime)s - %(message)s')
t = Main(token, token22)
t.run()
