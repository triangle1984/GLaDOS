from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.sql.sqlgame import checkchat


class CheckChat(BasicPlug):
    types = "runalways"
    thread = True

    def main(self):
        if "chat_id" in dir(self.event):
            checkchat(event)
