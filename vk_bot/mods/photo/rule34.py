from vk_bot.core.modules.basicplug import BasicPlug
import os, rule34
class Rule34(BasicPlug):
    doc = "Скора ето буит руле34"
    command = ["/руле34"]
    def main(self):
        rule34 = rule34.Sync()
        images = rule34.getImages("mettaton")
