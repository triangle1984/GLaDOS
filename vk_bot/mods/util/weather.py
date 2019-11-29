from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.modules.othermethods import OtherMethod
import requests


class Weatherandtranslit(BasicPlug, OtherMethod):
    doc = "погода *город* - покажет погоду в городе"
    command = ("погода",)

    def main(self):
        try:
            qr = self.text[1]
        except IndexError:
            self.sendmsg("а город указать?")
            return
        q = self.translit(qr, "en").lower()
        apiurl = "http://api.openweathermap.org/data/2.5/find"
        # бот настолько опенсурс, що тут даже токен к погоде опенсурс
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
            self.sendmsg("!error")
            return
        self.sendmsg(f"""Город: {q}
            🌥Погода: {w}
            🌡Температура: {temp}°
            💧Влажность: {vlaga}
            💨Скорость ветра: {wind}м/с""")
