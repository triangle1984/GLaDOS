from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.sql.sqlgame import sendall
from loadevn import *


class GroupJoin(BasicPlug):
    types = "runalways"
    vktypes = "group_join"

    def main(self):
        self.sendmsg(
            f"В группе новый пользователь! *id{self.uid}", peer_id=recipient, prefix=False)
