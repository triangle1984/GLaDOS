class BacisPlug:
    included = True
    types = "msg"
    doc = "Заполните справку в модуле"
    def __init__(self, vk, vk2):
        self.vk = vk
        self.vk2 = vk2
    def givedata(self, **args):
        for items in args.items():
            exec(f"self.{items[0]} = '{items[1]}'")
