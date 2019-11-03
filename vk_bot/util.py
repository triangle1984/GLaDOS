import vk_api, math, random, requests, base64, wikipedia, subprocess
from vk_api.utils import get_random_id
from loadevn import group_idd, apinews
from vk_bot.core.sql.vksql import *
from vk_bot.core.sql.sqlgame import hellosql
from vk_api import VkUpload
from datetime import timedelta
import pyPrivnote
wikipedia.set_lang("ru")
def callall(vk, event):
    calllist = []
    callid = vk.messages.getConversationMembers(peer_id=event.object.peer_id)
    for a in callid:
        calllist.append(f"@id{str(a['id'])} ({a['first_name']} {a['last_name']})")
    calljoin = ", ".join(calllist)
    return {"message":f"Я ПРИЗЫВАЮ ВАС:\n{calljoin}"}
def getusername(vk, uid):
    try:
        requests = vk.users.get(user_ids=uid, fields="first_name")
    except vk_api.exceptions.ApiError:
        return
    response = requests[0]["first_name"]
    return response
