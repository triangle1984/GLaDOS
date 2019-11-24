from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot.core.sql.sqlgame import sendall


class Agitation(BasicPlug):
    types = "runalways"
    vktypes = "wall_post_new"

    def main(self):
        post = self.event.object["id"]
        owner_id = self.event.object["owner_id"]
        attachment = f"wall{owner_id}_{post}"
        text = "Новый пост в группе~"
        sendall(self.event, text, self.vk, attachment)
