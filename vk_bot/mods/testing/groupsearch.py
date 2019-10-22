from vk_bot.modutil import BacisPlug
import random
class Groupsearch(BacisPlug):
    doc = "Найти паблики по названию  и скинуть айди"
    command = ["/паблики"]
    def main(self):
        result = self.vk2.groups.search(q=" ".join(self.text[1:]), count=15)["items"]
        gid = []
        for _ in range(10):
            rresult = random.choice(result)
            idd = str(rresult["id"])
            closed = bool(rresult["is_closed"])
            if idd not in gid and closed == False:
                gid.append("-" + idd)
        gid = ",".join(gid)
        self.sendmsg(f"Паблики: {gid}")
