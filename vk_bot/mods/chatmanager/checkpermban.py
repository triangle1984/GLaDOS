from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.chatmager import ChatManager
from loadevn import permban
from vk_bot.core.sql.vksql import *


class CheckPermban(BasicPlug, ChatManager):
    types = "runalways"
    action = "chat_invite_user"
    included = False

    def main(self):
        uid = self.event.object.action['member_id']
        chat_id = self.event.chat_id
        if checktable(f"{permban}", "chat_id", f"{chat_id}", andd=f"uid = {uid}"):
            self.kick(uid)
