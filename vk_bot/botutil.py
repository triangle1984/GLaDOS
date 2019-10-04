from token2 import recipient
from vk_api.utils import get_random_id
from vksql import sendall, checktable
def groupjoin(vk, event):
    idjoin = f"*id{event.object['user_id']}"
    vk.messages.send(user_id=recipient, random_id=get_random_id(), attachment="photo271595905_457261640",
                        message=f'В группу вступил новый пользователь! {idjoin}')
def sendpost(vk, event):
    post = event.object["id"]
    owner_id = event.object["owner_id"]
    attachment = f"wall{owner_id}_{post}"
    text = "Новый пост в группе~"
    sendall(event, text, vk, attachment)
def sqlcache(mc, uid):
    uid = str(uid)
    if uid in mc:
        return mc.get(uid)
    else:
        prefix = checktable("prefix", "id", uid)["name"]
        vips = bool(checktable("vips", "id", uid))
        admins = bool(checktable("admins", "id", uid))
        mc.set(uid, {"vips":vips, "prefix": prefix, "admins":admins})
        return mc.get(uid)
