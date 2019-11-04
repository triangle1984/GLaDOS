from vk_bot.core.modules.basicplug import BasicPlug
class Test(BasicPlug):
    command = ["/hello"]
    doc = "первый модуль, тест"
    def main(self):
        self.sendmsg("Хелоу ворлдддд")
