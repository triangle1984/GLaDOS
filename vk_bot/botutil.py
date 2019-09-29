from token2 import recipient
from vk_api.utils import get_random_id
from vksql import sendall
def groupjoin(vk, event):
    idjoin = f"*id{event.object['user_id']}"
    vk.messages.send(user_id=recipient, random_id=get_random_id(), attachment="photo271595905_457261640",
                        message=f'В группу вступил новый пользователь! {idjoin}')
def sendpost(vk, event):
    post = event.object["id"]
    owner_id = event.object["owner_id"]
    attachment = f"wall{owner_id}_{post}"
    text = "Новый пост в группе~"
    sendall(vk, text, attachment)
