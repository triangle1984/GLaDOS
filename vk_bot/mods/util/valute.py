from vk_bot.core.modules.basicplug import BasicPlug
import requests
class Valute(BasicPlug):
    doc = "Курс валют"
    command = ["/курс"]
    def main(self):
            api = "https://www.cbr-xml-daily.ru/daily_json.js"
            r = requests.get(api)
            encode = r.json()
            usd = encode["Valute"]["USD"]["Value"]
            eur = encode["Valute"]["EUR"]["Value"]
            self.sendmsg("Доллар: {}₽\nЕвро: {}₽".format(usd, eur))