from vk_bot.core.modules.basicplug import BasicPlug


class CheckPermban(BasicPlug):
    types = "runalways"
    action = "chat_invite_user"

    def main(self):
        print(self.event.object.action['member_id'])
        print(self.peer_id)
