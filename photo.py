import vk_api, requests, random
from vk_api.utils import get_random_id
def phootowallrandom(groups, vk, upload, albid="wall"):
    group_id = random.choice(groups)
    max_num = vk.photos.get(owner_id=group_id, album_id=albid, count=0)['count']
    num = random.randint(0, max_num)
    photo = vk.photos.get(owner_id=group_id, album_id='wall',
                          count=1, offset=num)['items'][0]['id']
    return f"photo{group_id}_{photo}"
def yuri(vk, upload):
    photo = phootowallrandom(["-170165000", "-63092480", "-153284406"], vk, upload)
    return {"message":"бот: Юрец~~🌚", "attachment":photo}
def gebbels(vk, upload):
    photo = phootowallrandom(["-174482230"], vk, upload)
    return {"message":"ХАЧЕШЬ ЛИ ТЫ ТОТАЛЬНОЙ ВАЙНЫ?", "attachment":photo}
def yaoi(vk, upload):
    photo = phootowallrandom(["-98467405", "-113004231", "-57807542"], vk, upload)
    return {"message":"Яойчег~~🌚", "attachment":photo}
def trap(vk, upload):
    photo = phootowallrandom(["-171834188"], vk, upload)
    return {"message":"Трапы~~🌚", "attachment":photo}
def cats(vk, upload):
    photo = phootowallrandom(["-43228812", "-34137527", "-152424758"], vk, upload)
    return {"message":"Шавухенция на заказ", "attachment":photo}

