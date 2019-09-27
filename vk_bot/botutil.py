from token2 import recipient
from vk_api.utils import get_random_id
def groupjoin(vk, event):
    idjoin = f"*id{event.object['user_id']}"
    vk.messages.send(user_id=recipient, random_id=get_random_id(), attachment="photo271595905_457261640"
                        message=f'В группу вступил новый пользователь! {idjoin}')

