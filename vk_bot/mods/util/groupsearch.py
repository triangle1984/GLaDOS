from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod


class Groupsearch(BasicPlug, OtherMethod):
    doc = "Найти паблики по названию  и скинуть айди"
    command = ["/паблики"]

    def main(self):
        self.sendmsg(",".join(self.groupsearch(15, " ".join(self.text[1:]))))
