from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
from pydub import AudioSegment
import os
import random
class MusicBoost(BasicPlug, Upload):
    doc = "басуха прям пиздец"
    command = ["/басуха"]

    def main(self):
        try:
            link = self.event.object["attachments"][0]["audio"]["url"]
            title = self.event.object["attachments"][0]["audio"]["title"]
        except:
            self.sendmsg("Ты забыл скинуть что надо разъебать")
        os.system(f'wget {link} -O {title}.mp3')
        sound = AudioSegment.from_mp3(f"{title}.mp3")
        soundname = f"title-{title}.wav"
        sound.export(soundname, format="wav")

        sound = AudioSegment.from_file(soundname)
        #make bassboost track
        bassboost = sound + 20
        bass = f"boost-{title}.wav"
        bassboost.export(bass, format="wav")

        #Transfer wav to OGG
        sound = AudioSegment.from_file(bass)
        ogg = f"boost-{title}.ogg"
        sound.export(ogg, format="ogg")
        try:
            self.sendmsg(f"делаю бах-бах")
            self.sendmsg(self.upload.audio_message(ogg))
        except:
            return
        finally:
            os.remove(ogg)
            os.remove(bass)
            os.remove(soundname)
            os.remove(f"{title}.mp3")