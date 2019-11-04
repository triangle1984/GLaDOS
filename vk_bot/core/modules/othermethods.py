import argparse, random
class OtherMethod:
    def phootowallrandom(self, groups, albid="wall"):
        args = argparse.ArgumentParser(description="пикчи")
        args.add_argument("-с", "-c", "--count", type=int, default=1)
        try:
            a = args.parse_args(self.text[1:])
        except KeyboardInterrupt:
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
                max_num = self.vk2.photos.get(owner_id=group_id, album_id=albid, count=0)['count']
                num = random.randint(0, max_num)
                photo = self.vk2.photos.get(owner_id=group_id, album_id=albid,
                                    count=1, offset=num)['items'][0]['id']

                photo2.append(f"photo{group_id}_{photo}")
        except KeyboardInterrupt:
            self.sendmsg("!error от вк");return
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
