from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod
import vk_api, requests, random
from vk_api.utils import get_random_id
class Photos(BasicPlug, OtherMethod):
    doc = "Фотачки"
    command = ["/юри", "/каты", "/геббельс", "/яой", "/трапы", "/лоли", "/махно",
               "/калян", "/хентай", "/ноги", "/ножки", "/мем", "/адольф", "/гитлер",
               ""]
    def main(self):
        requests = self.text[0]
        if requests == "/каты":
            self.cats()
        elif requests == "/юри":
            self.yuri()
        elif requests == "/геббельс":
            self.gebbels()
        elif requests == "/яой":
            self.yaoi()
        elif requests == "/трапы":
            self.trap()
        elif requests == "/лоли":
            self.loli(self.vk2,text)
        elif requests == "/махно":
            self.mahno()
        elif requests == "/калян":
            self.colyan()
        elif requests == "/хентай":
            self.hentai()
        elif requests == "/ноги" or requests == "/ножки":
            self.legs()
        elif requests == "/мем":
            self.mem()
        elif requests == "/адольф" or requests == "/гитлер":
            self.adolf()
    def yuri(self):
        photo = self.phootowallrandom(["-170165000", "-63092480", "-153284406"])
        self.sendmsg("Юрец~~🌚", photo)
    def gebbels(self):
        photo = self.phootowallrandom(["-174482230"])
        self.sendmsg("ХАЧЕШЬ ЛИ ТЫ ТОТАЛЬНОЙ ВАЙНЫ?", photo)
    def yaoi(self):
        photo = self.phootowallrandom(["-98467405", "-113004231", "-57807542", "-38230251"], )
        self.sendmsg("Яойчег~~🌚", photo)
    def trap(self):
        photo = self.phootowallrandom(["-171834188"])
        self.sendmsg("Трапы~~🌚", photo)
    def cats(self):
        photo = self.phootowallrandom(["-43228812"])
        self.sendmsg("Шавухенция на заказ", photo)
    def loli(self):
        photo = self.phootowallrandom(["-127518015", "-157516431", "-69721869"])
        self.sendmsg("FBI OPEN UP", photo)
    def mahno(self):
        photo = self.phootowallrandom(["367919273"], albid=262361216)
        self.sendmsg("СВОБОДА АБО ИДИТЕ НАХУЙ", photo)
    def colyan(self):
        photo = self.phootowallrandom(["-183493220"],albid=266695546)
        self.sendmsg("БОЖЕЕЕЕЕЕЕ, ЦАРЯ ХРАНИ", photo)
    def hentai(self):
        photo = self.phootowallrandom(["-161403814", "-170993976"])
        self.sendmsg("Хентай~~🌚", photo)
    def legs(self):
        photo = self.phootowallrandom(["-174842315", "-102853758", "-134982584", "-138265009", "-114279288"])
        self.sendmsg( "Ножки &#127773;",  photo)
    def mem(self):
        photo = self.phootowallrandom(["-154306815"])
        self.sendmsg( "Держи мемас",  photo)
    def adolf(self):
        photo = self.phootowallrandom(["-183493220"], albid=266718794)
        self.sendmsg("Хай фюрер", photo)
    def yourpic(self, public):
        photo = self.phootowallrandom(public)
        self.sendmsg("Пикча из личного альбома~", photo)
