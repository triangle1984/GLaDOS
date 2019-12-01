from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
from gtts import gTTS
import time


class TextToAudio(BasicPlug, Upload):
    doc = "гс в текст"
    command = ("озвучить", "гуглбаба", "озвучь", "скажи")

    def main(self):
        name = f"{time.time_ns()}.mp3"
        tts = gTTS("".join(self.text[1:]), lang='ru')
        tts.save(name)
        self.sendmsg("Дэржите", self.audiomessage(name))
