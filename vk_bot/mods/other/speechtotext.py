"""
Модуль написал https://vk.com/feelan03
"""
from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
import speech_recognition as sr
from pydub import AudioSegment
import os
import time
import random


class AutdiotoText(BasicPlug, Upload):
    doc = "гс в текст"
    types = "runalways"
    attachment = 'audio_message'

    def main(self):
        try:
            link = self.event.object["attachments"][0]["audio_message"]["link_mp3"]
        except:
            return
        name = self.dowloadfile(link)['name']
        sound = AudioSegment.from_mp3(name)
        soundname = f"audio2{time.time_ns()}.wav"
        sound.export(soundname, format="wav")

        r = sr.Recognizer()  # Использование файла как источник
        with sr.AudioFile(soundname) as source:
            audio = r.record(source)  # Считывает весь файл
        try:
            result = r.recognize_google(audio, language="ru_RU")
            self.sendmsg(f"сказал: {result}")
        except sr.UnknownValueError:
            self.sendmsg(
                f"НИХУЯ НЕ ПОНИМАЮ НИ ОДНОГО СЛОВА БЛЯТЬ, КАРТАВАЯ СУКА")
        except sr.RequestError:
            self.sendmsg(f"Ошибка при отправки запроса")
        finally:
            os.remove(name)
            os.remove(soundname)
