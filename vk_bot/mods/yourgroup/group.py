import vk_api, requests, random, argparse
from vk_api.utils import get_random_id
class Group:
    def __init__(self, vk,text):
        self.vk = vk
        self.text = text
    def groupwallrandom(self, groups, albid="wall"):
        post2 = []
        try:
            group_id = random.choice(groups)
            max_num = self.vk.wall.get(owner_id=group_id, album_id=albid, count=0)['count']
            num = random.randint(0, max_num)
            post = self.vk.wall.get(owner_id=group_id, count=1, offset=num)['items'][0]['id']
            post2.append(f"wall{group_id}_{post}")
        except KeyboardInterrupt:
            self.sendmsg("!error от вк");return
        photo2 = ",".join(post2)
        return photo2
    def yourpost(self, public):
        post = self.groupwallrandom(public)
        return post
