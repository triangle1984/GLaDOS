from vk_bot.core.modules.basicplug import BasicPlug
import requests
class Weatherandtranslit(BasicPlug):
    doc = "позже придумаю"
    command = ["/переводчик", "/погода"]
    def main(self):
            com = self.text[0].lower()
            if com == "/переводчик":
                self.sendmsg(translit(self.text, self.vk))
            if com == "/погода":
                weather(self)

def translit(text, vk=False, english=False):
        apikey = "trnsl.1.1.20190508T201810Z.385ebfa1e596baa0.90672cf8655555b1b51ced31b03c2e8bb9bde46c"
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        url2 = "https://translate.yandex.net/api/v1.5/tr.json/detect"
        params = {"key": apikey,
                    "text":text[1:]}
        r = requests.get(url2, params=params)
        encode = r.json()
        lang = f"{encode['lang']}-ru"
        if english:
            lang = "ru-en"
        params = {"key": apikey,
                "text":text[0:],
                "lang":lang}
        r = requests.get(url, params=params)
        encode = r.json()
        try:
            if vk:
                encode = " ".join(encode["text"][1:])
                return "Перевод: {}".format(encode)
        except:
            return
        return encode["text"][0]

def weather(self):
        try:
            qr = self.text[1]
        except:
            return
        q = translit(text=qr, english=True); q.lower()
        apiurl = "http://api.openweathermap.org/data/2.5/find"
        appid = '22c7bf8e593c47b0cf88f390e8e5376a'
        params = {
                    'q': q,
                    'appid': appid,
                    'units': 'metric',
                    'lang': 'ru'
                    }
        try:
            r = requests.get(apiurl, params=params, timeout=5)
            encode = r.json()
            w = encode['list'][0]['weather'][0]['description']
            temp = encode["list"][0]["main"]["temp"]
            vlaga = encode["list"][0]["main"]["humidity"]
            wind = encode["list"][0]["wind"]["speed"]
        except:
            return
        self.sendmsg(f"""Город: {q}
        🌥Погода: {w}
        🌡Температура: {temp}°
        💧Влажность: {vlaga}
        💨Скорость ветра: {wind}м/с""")