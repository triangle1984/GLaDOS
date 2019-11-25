from vk_bot.core.modules.basicplug import BasicPlug


class Ping(BasicPlug):
    doc = "Проверить, жив ли бот"
    command = ("жив?", "ping",)

    def main(self):
        self.sendmsg("JA JA Führer")
