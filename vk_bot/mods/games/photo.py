import vk_api, requests, random, argparse
from vk_api.utils import get_random_id
from vk_bot.modutil import BacisPlug
class Photo(BacisPlug):
    def phootowallrandom(self, groups, albid="wall"):
        try:
            a = self.args2()
            a = a.parse_args(self.text[1:])
        except:
            try:
                a.count = int(self.text[1])
            except:
                a.count = 1
        photo2 = []
        if a.count > 10:
            a.count = 10
        try:
            for _ in range(a.count):
                group_id = random.choice(groups)
                max_num = self.vk.photos.get(owner_id=group_id, album_id=albid, count=0)['count']
                num = random.randint(0, max_num)
                photo = self.vk.photos.get(owner_id=group_id, album_id=albid,
                                    count=1, offset=num)['items'][0]['id']

                photo2.append(f"photo{group_id}_{photo}")
        except vk_api.exceptions.ApiError:
            return {"message":"!error от вк"}
        photo2 = ",".join(photo2)
        return photo2
    def args2(self):
        args = argparse.ArgumentParser(description="картинки")
        args.add_argument("-с", "-c", "--count", type=int, default=1)
        return args
    def yuri(self):
        photo = self.phootowallrandom(["-170165000", "-63092480", "-153284406"])
        return {"message":"Юрец~~🌚", "attachment":photo}
    def gebbels(self):
        photo = self.phootowallrandom(["-174482230"])
        return {"message":"ХАЧЕШЬ ЛИ ТЫ ТОТАЛЬНОЙ ВАЙНЫ?", "attachment":photo}
    def yaoi(self):
        photo = self.phootowallrandom(["-98467405", "-113004231", "-57807542", "-38230251"], )
        return {"message":"Яойчег~~🌚", "attachment":photo}
    def trap(self):
        photo = self.phootowallrandom(["-171834188"])
        return {"message":"Трапы~~🌚", "attachment":photo}
    def cats(self):
        photo = self.phootowallrandom(["-43228812"])
        return {"message":"Шавухенция на заказ", "attachment":photo}
    def loli(self):
        photo = self.phootowallrandom(["-127518015", "-157516431", "-69721869"])
        return {"message":"FBI OPEN UP", "attachment":photo}
    def mahno(self):
        photo = self.phootowallrandom(["367919273"], albid=262361216)
        return {"message":"СВОБОДА АБО ИДИТЕ НАХУЙ", "attachment":photo}
    def citati(self):
        photo = self.phootowallrandom(["-173186389"])
        return {"message":"Цитатки на заказ", "attachment":photo}
    def colyan(self):
        photo = self.phootowallrandom(["-183493220"],albid=266695546)
        return {"message":"БОЖЕЕЕЕЕЕЕ, ЦАРЯ ХРАНИ", "attachment":photo}
    def hentai(self):
        photo = self.phootowallrandom(["-161403814", "-170993976"])
        return {"message":"Хентай~~🌚", "attachment":photo}
    def legs(self):
        photo = self.phootowallrandom(["-174842315", "-102853758", "-134982584", "-138265009", "-114279288"])
        return {"message": "Ножки &#127773;", "attachment": photo}
    def mem(self):
        photo = self.phootowallrandom(["-154306815"])
        return {"message": "Держи мемас", "attachment": photo}
    def adolf(self):
        photo = self.phootowallrandom(["-183493220"], albid=266718794)
        return {"message":"Хай фюрер", "attachment":photo}
    def hesus(self):
        photo = self.phootowallrandom(["-156059526"])
        return {"message": "Лови красавчика😎", "attachment": photo}
    def yourpic(self, public):
        photo = self.phootowallrandom(public)
        return {"message":"Пикча из личного альбома~", "attachment":photo}
