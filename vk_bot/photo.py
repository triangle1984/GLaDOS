import vk_api, requests, random, argparse
from vk_api.utils import get_random_id
class Photo:
    def __init__(self, vk,text):
        self.vk = vk
        self.text = text
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
        except KeyboardInterrupt:
            self.sendmsg("!error от вк");return
        photo2 = ",".join(photo2)
        return photo2
    def args2(self):
        args = argparse.ArgumentParser(description="картинки")
        args.add_argument("-с", "-c", "--count", type=int, default=1)
        return args
    def yourpic(self, public):
        photo = self.phootowallrandom(public)
        return photo
