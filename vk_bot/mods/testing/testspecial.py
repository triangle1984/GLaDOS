from vk_bot.core.modules.basicplug import BasicPlug
class Test2(BasicPlug):
    doc = "первый модуль, тест"
    types = 'commandb'
    @staticmethod
    def getcommand(uid, text):
        return "/тест"
    def main(self):
        self.sendmsg(self.text[0])
