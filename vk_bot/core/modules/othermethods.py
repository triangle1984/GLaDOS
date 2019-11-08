import argparse
import random
import requests
import os
import time


class OtherMethod:
    def phootowallrandom(self, groups, albid="wall"):
        args = argparse.ArgumentParser(description="пикчи")
        args.add_argument("-с", "-c", "--count", type=int, default=1)
        try:
            a = args
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
                max_num = self.vk2.photos.get(
                    owner_id=group_id, album_id=albid, count=0)['count']
                num = random.randint(0, max_num)
                photo = self.vk2.photos.get(owner_id=group_id, album_id=albid,
                                            count=1, offset=num)['items'][0]['id']

                photo2.append(f"photo{group_id}_{photo}")
        except KeyboardInterrupt:
            self.sendmsg("!error от вк")
            return
        photo2 = ",".join(photo2)
        return photo2

    def nametoid(self, names):
        uid = []
        for convert in names:
            r = self.vk.utils.resolveScreenName(screen_name=convert)
            if r:
                if r["type"] == "group":
                    uid.append(f"-{r['object_id']}")
                else:
                    uid.append(str(r["object_id"]))
            else:
                uid.append(convert)
        return uid

    def uploadphoto(self, photo):
        response = self.upload.photo_messages(photos=photo)[0]
        return f"photo{response['owner_id']}_{response['id']}"

    def uploaddoc(self, document, peer_id):
        response = self.upload.document_message(
            doc=document, peer_id=peer_id)['doc']
        return f"doc{response['owner_id']}_{response['id']}"

    def dowloadfile(self, url, name):
        gif = False
        with open(name, "wb") as files:
            response = requests.get(url).content
            files.write(response)
        if url[-3:] == "gif":
            gif = True
        return gif

    def dowloadupload(self, url):
        name = f"photo{time.time()}.png"
        try:
            files = self.dowloadfile(url, name)
            if files == False:
                response = self.uploadphoto(name)
            else:
                response = self.uploaddoc(name, self.peer_id)
        finally:
            os.remove(name)
        return response
