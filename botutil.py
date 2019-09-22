from vk_api.utils import get_random_id
def groupjoin(vk, event):
    idjoin = f"*id{event.object['user_id']}"
    vk.messages.send(user_id=recipient, random_id=get_random_id(),
                        message=f'В группу вступил новый пользователь! {idjoin}')

