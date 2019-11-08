from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.upload import Upload
from vk_bot.core.modules.othermethods import OtherMethod
import requests
import nekos


class Nekoslife(BasicPlug, Upload, OtherMethod):
    doc = "Рандом фотки с nekoslife"
    command = ["/nekoslife", "/некослайф", "/некос", "/nekos"]

    def main(self):
        a = self.args(self.text[2:])
        if a.count > 10:
            a.count = 10
        image_url = []
        try:
            for _ in range(a.count):
                image_url.append(nekos.img(self.text[1]))
            self.sendmsg("начинаю качать пикчи")
            image = self.multithreadwoload(image_url)
            self.sendmsg("Держи!", image)
        except:
            self.sendmsg("""Введи один из этих аргументов:
            feet, yuri, trap, futanari, hololewd, lewdkemo, solog, feetg, cum, erokemo, les, wallpaper, lewdk, ngif, tickle, lewd, feed, gecg, eroyuri, eron, cum_jpg, bj, nsfw_neko_gif, solo, kemonomimi, nsfw_avatar, gasm, poke, anal, slap, hentai, avatar, erofeet, holo, keta, blowjob, pussy, tits, holoero, lizard, pussy_jpg, pwankg, classic, kuni, waifu, pat, 8ball, kiss, femdom, neko, spank, cuddle, erok, fox_girl, boobs, random_hentai_gif, smallboobs, hug, ero, smug, goose, baka""")
