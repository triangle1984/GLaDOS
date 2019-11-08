from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod
import requests, nekos
class Nekoslife(BasicPlug, OtherMethod):
    doc = "Рандом фотки с nekoslife"
    command = ["/nekoslife", "/некослайф", "/некос"]
    def main(self):
        try:
            image_url = nekos.img(self.text[1])
            image = self.dowloadupload(image_url)
            self.sendmsg("Держи!", image)
        except:
            self.sendmsg("""Введи один из этих аргументов:
            feet, yuri, trap, futanari, hololewd, lewdkemo, solog, feetg, cum, erokemo, les, wallpaper, lewdk, ngif, tickle, lewd, feed, gecg, eroyuri, eron, cum_jpg, bj, nsfw_neko_gif, solo, kemonomimi, nsfw_avatar, gasm, poke, anal, slap, hentai, avatar, erofeet, holo, keta, blowjob, pussy, tits, holoero, lizard, pussy_jpg, pwankg, classic, kuni, waifu, pat, 8ball, kiss, femdom, neko, spank, cuddle, erok, fox_girl, boobs, random_hentai_gif, smallboobs, hug, ero, smug, goose, baka""")
