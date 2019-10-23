from vk_bot.modutil import BacisPlug
import speech_recognition as sr
from pydub import AudioSegment
import os
import random
class Autdiototext(BacisPlug):
    doc = "гс в текст"
    types = "runalways"
    command = [None]
    def main(self):
        try:
            link = self.event.object["attachments"][0]["audio_message"]["link_mp3"]
        except:
            return
        randomnumber = random.randint(0, 10000)
        name = f"audio{randomnumber}.mp3"
        os.system(f"wget -O {name} {link}")
        sound = AudioSegment.from_mp3(name)
        sound.export(f"audio2{randomnumber}.wav", format="wav")

        audio_file = f"audio2{randomnumber}.wav" # путь до файла
        r  = sr.Recognizer() # Использование файла как источник
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source) # Считывает весь файл
        try:
            result = r.recognize_google(audio, language = "ru_RU")
            self.sendmsg(f"*id{self.uid} сказал: {result}")
        except sr.UnknownValueError:
            self.sendmsg(f"Блять, говори четьче, не хуя ")
        except sr.RequestError:
            self.sendmsg(f"Ошибка при отправки запроса")
        finally:
            os.remove(name)
            os.remove(f"audio2{randomnumber}.wav")
