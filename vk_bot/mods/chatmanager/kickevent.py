from vk_bot.core.modules.basicplug import BasicPlug


class Test(BasicPlug):
    types = "runalways"
    action = "chat_kick_user"

    def main(self):
        pass
