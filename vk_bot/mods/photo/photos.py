from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod
import vk_api
import random
from vk_api.utils import get_random_id


class Photos(BasicPlug, OtherMethod):
    doc = "Фотачки"
    command = ["/юри", "/каты", "/геббельс", "/яой", "/трапы", "/лоли", "/махно",
               "/калян", "/хентай", "/ноги", "/ножки", "/мем", "/адольф"]

    def main(self):
        requests = self.text[0]
        if requests == "/каты":
            self.sendmsg("Шавухенция на заказ",
                         self.phootowallrandom(["-43228812"]))
        elif requests == "/юри":
            self.sendmsg("Юрец~~🌚", self.phootowallrandom(
                ["-170165000", "-63092480", "-153284406"]))
        elif requests == "/геббельс":
            self.sendmsg("ХАЧЕШЬ ЛИ ТЫ ТОТАЛЬНОЙ ВАЙНЫ",
                         self.phootowallrandom(["-174482230"]))
        elif requests == "/яой":
            self.sendmsg("Яойчег~~🌚", self.phootowallrandom(
                ["-98467405", "-113004231", "-57807542", "-38230251"]))
        elif requests == "/трапы":
            self.sendmsg("Трапы~~🌚", self.phootowallrandom(["-171834188"]))
        elif requests == "/лоли":
            self.sendmsg("FBI OPEN UP", self.phootowallrandom(
                ["-127518015", "-157516431", "-69721869"]))
        elif requests == "/махно":
            self.sendmsg("СВОБОДА АБО ИДИТЕ НАХУЙ", self.phootowallrandom(
                ["367919273"], albid=262361216))
        elif requests == "/калян":
            self.sendmsg("БОЖЕЕЕЕЕЕЕ ЦАРЯ ХРАНИ", self.phootowallrandom(
                ["-183493220"], albid=266695546))
        elif requests == "/хентай":
            self.sendmsg("Хентай~~🌚", self.phootowallrandom(
                ["-161403814", "-170993976"]))
        elif requests == "/ноги" or requests == "/ножки":
            self.sendmsg("Ножки &#127773;", self.phootowallrandom(
                ["-174842315", "-102853758", "-134982584", "-138265009", "-114279288"]))
        elif requests == "/мем":
            self.sendmsg("Держи мемас", self.phootowallrandom(["-154306815"]))
        elif requests == "/адольф" or requests == "/гитлер":
            self.sendmsg("Хай фюрер", self.phootowallrandom(
                ["-183493220"], albid=266718794))
