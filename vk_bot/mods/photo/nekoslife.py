from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
from vk_bot.core.modules.othermethods import OtherMethod
import nekos
from boltons import iterutils


class Nekoslife(BasicPlug, Upload, OtherMethod):
    doc = "Рандом фотки с nekoslife"
    command = ("nekoslife", "некослайф", "некос", "nekos",)

    def main(self):
        a = self.args(self.text[2:])
        if a.count > 10 and self.mc2['vips'] == False:
            a.count = 10
        elif a.count > 30:
            a.count = 30
        image_url = []
        try:
            if a.count > 4:
                self.sendmsg("начинаю качать пикчи")
            for _ in range(a.count):
                image_url.append(nekos.img(self.text[1]))
            image = self.multithreadwoload(image_url)
            image = list(iterutils.chunked_iter(image.split(","), 10))
            for image in image:
                images = ",".join(image)
                self.sendmsg("Держи!", images)
        except:
            self.sendmsg("""Введи один из этих аргументов, с цифрой на конце или с -c 5 - скинет указанное количество пикч:
            feet, yuri, trap, futanari, hololewd, lewdkemo, solog, feetg, cum, erokemo, les, wallpaper, lewdk, ngif, tickle, lewd, feed, gecg, eroyuri, eron, cum_jpg, bj, nsfw_neko_gif, solo, kemonomimi, nsfw_avatar, gasm, poke, anal, slap, hentai, avatar, erofeet, holo, keta, blowjob, pussy, tits, holoero, lizard, pussy_jpg, pwankg, classic, kuni, waifu, pat, 8ball, kiss, femdom, neko, spank, cuddle, erok, fox_girl, boobs, random_hentai_gif, smallboobs, hug, ero, smug, goose, baka""")
