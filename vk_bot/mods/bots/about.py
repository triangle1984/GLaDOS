from vk_bot.core.modules.basicplug import BasicPlug


class AboutBot(BasicPlug):
    doc = "Инфа о боте"
    command = ("оботе",)

    def main(self):
        info = """
        бот написан на python, двумя прогерами
        первый прогер: *slava_a_i_r
        второй прогер: *pythonoglot
        третий прогер(запаска): *feelan03
        Также, он опенсурс, репа: github.com/triangle1984/GLaDOS
        Приятного пользования~
        Узнать команды: /хелп
        """
        self.sendmsg(info)
