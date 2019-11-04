from vk_bot.core.modules.basicplug import BasicPlug
import random
class Who(BasicPlug):
    doc = "Выбирает рандомного участника беседы под вашим предлогом"
    command = ["/кто"]
    def main(self):
        try:
            whotext = ' '.join(self.text[1:])
            whoid = random.choice(self.vk.messages.getConversationMembers(peer_id=self.event.object.peer_id)['profiles'])
            whofirstname = whoid['first_name']
            wholastname = whoid['last_name']
            whoidstr = whoid['id']
            self.sendmsg(f"Кто {whotext}? Я думаю, это @id{whoidstr} ({whofirstname} {wholastname})")
        except:
            self.sendmsg("Для работы этой команды боту нужна админка в беседе!")