import vk_api, requests, random
from vk_api.utils import get_random_id
def phootowallrandom(groups, vk, albid="wall"):
    group_id = random.choice(groups)
    max_num = vk.photos.get(owner_id=group_id, album_id=albid, count=0)['count']
    num = random.randint(0, max_num)
    photo = vk.photos.get(owner_id=group_id, album_id=albid,
                          count=1, offset=num)['items'][0]['id']
    return f"photo{group_id}_{photo}"
def yuri(vk):
    photo = phootowallrandom(["-170165000", "-63092480", "-153284406"], vk)
    return {"message":"Юрец~~🌚", "attachment":photo}
def gebbels(vk):
    photo = phootowallrandom(["-174482230"], vk)
    return {"message":"ХАЧЕШЬ ЛИ ТЫ ТОТАЛЬНОЙ ВАЙНЫ?", "attachment":photo}
def yaoi(vk):
    photo = phootowallrandom(["-98467405", "-113004231", "-57807542"], vk)
    return {"message":"Яойчег~~🌚", "attachment":photo}
def trap(vk):
    photo = phootowallrandom(["-171834188"], vk)
    return {"message":"Трапы~~🌚", "attachment":photo}
def cats(vk):
    photo = phootowallrandom(["-43228812", "-34137527", "-152424758"], vk)
    return {"message":"Шавухенция на заказ", "attachment":photo}
def loli(vk):
    photo = phootowallrandom(["-127518015", "-157516431", "-69721869"], vk)
    return {"message":"FBI OPEN UP", "attachment":photo}
def mahno(vk):
    photo = phootowallrandom(["367919273"],vk,  albid=262361216)
    return {"message":"СВОБОДА АБО ИДИТЕ НАХУЙ", "attachment":photo}

