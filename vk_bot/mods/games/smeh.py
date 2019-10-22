#!/usr/bin/env python
import random, sys, argparse
from vk_bot.sqlgame import smehdb
from vk_bot.modutil import BacisPlug
class Smeh(BacisPlug):
    command = ["/смех", "/смехк"]
    doc = "генератор смеха. С -h вызовет справку"
    def args(self):
        args = argparse.ArgumentParser(description="генератор смеха")
        args.add_argument("-c","-с", "--count", type=int, default=random.randint(5, 50))
        args.add_argument("-s", "--smex", default='None')
        args.add_argument("-s2", "--smexslova", default='None')
        args.add_argument("-sc", "--smehcount", default=1, type=int)
        return args
    def main(self):
        helps = """а це посложнее. Для этой хуйни я проработал целую систему аргументов:
        /смех -c (число) = количество символов в смехе
        /смех -s (буквы) = символы для генерации смеха
        /смех -s2 (слово) = слово для генерации смеха
        -c и -s/s2 можно использовать одновременно
        примеры:
        /смех -s2 .exe -c 69
        /смех -s хпх -c 50
        /смех -s хпхп
        /смех -c 69
        А так же, все тоже самое, но со /смехк - запишет ваши настройки для генератора
        То есть: после /смехк -s2 .exe -c 69 , в /смех без аргументов - будет
        использоваться то, что вы передали в /смехк
        """
        scmax = 3
        if self.mc2["vips"]:
            scmax = 8
        db = False
        try:
            if "".join(self.text)[5].lower() == "к":
                db = True
        except IndexError:
            None
        ss = self.args()
        try:
            ss = ss.parse_args(self.text[1:])
            proverka = self.text[1]
        except IndexError:
            ss2 =  smehdb(ss, self.uid, db)
            if ss2:
                ss = ss2
        except:
            self.sendmsg(helps)
        if db:
            smehdb(ss, self.uid, db)
        if ss.count > 9999:
            return
        main = ["Х", "Ы", "Ъ"]
        if ss.smex != 'None':
            main = list(ss.smex)
        if ss.smexslova != 'None':
            main = ss.smexslova.split()
        if ss.smehcount > scmax:
            self.sendmsg(f"Ваш лимит sc - {scmax}")
            return
        for _ in range(ss.smehcount):
            mainsmex = "".join(random.choice(main) for _ in range(ss.count))
            self.sendmsg(mainsmex)
            ss.count = random.randint(5, 69)
