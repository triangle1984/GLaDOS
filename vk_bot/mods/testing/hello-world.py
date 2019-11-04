from vk_bot.core.modules.basicplug import BacisPlug
class Test(BacisPlug):
    command = ["/hello"]
    doc = "первый модуль, тест"
    def main(self):
        self.sendmsg("Хелоу ворлдддд")
