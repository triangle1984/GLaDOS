from token2 import recipient, group_idd
from vk_api.utils import get_random_id
from vksql import *
from vk_api.bot_longpoll import VkBotEventType
import vk_api
from sqlgame import *
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
def botmain(vk, event):
        if event.type == VkBotEventType.GROUP_JOIN:
            groupjoin(vk, event)
        if event.type == VkBotEventType.WALL_POST_NEW:
            sendpost(vk, event)
        try:
            vk.groups.enableOnline(group_id=group_idd)
        except vk_api.exceptions.ApiError:
            None
        try:
            if event.object.action['type'] == 'chat_invite_user':
                vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(), message=checktable(chathello, 'id', event.chat_id)['hello'])
        except TypeError:
            None
        except vk_api.exceptions.ApiError:
            vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(), message="Приветствие настроено не правильно!")
        if "chat_id" in dir(event):
            checkchat(event)
def sqlcache(mc, uid):
    uid = str(uid)
    if uid in mc:
        None
    else:
        saveload(uid)
        prefix = checktable("prefix", "id", uid)["name"]
        vips = bool(checktable("vips", "id", uid))
        admins = bool(checktable("admins", "id", uid))
        count = tablecount("yourphoto", "id", uid)
        ban = bool(checktable("ban", "id", uid))
        mc.set(uid, {"vips":vips,
                     "prefix": prefix,
                     "admins":admins,
                     "count":count,
                     "ban":ban})
    return mc.get(uid)
