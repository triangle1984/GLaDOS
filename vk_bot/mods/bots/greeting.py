from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.loadevn import chathello


class Greeting(BasicPlug):
    types = "runalways"
    action = "chat_invite_user"

    def main(self):
        message = checktable(chathello, 'id', event.chat_id)['hello']
        self.sendmsg(message)
