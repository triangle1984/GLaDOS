from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload


class Test2(BasicPlug, Upload):
    doc = "тест"
    command = "/етотест"

    def main(self):
        self.multithreadwoload(
            ['https://sun9-66.userapi.com/c543101/v543101670/6ed2b/wkoWj6GITj4.jpg'])
