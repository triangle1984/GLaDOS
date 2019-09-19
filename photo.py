import vk_api, requests, random, argparse
from vk_api.utils import get_random_id
def args2():
    args = argparse.ArgumentParser(description="картинки")
    args.add_argument("-c", "--count", type=int, default=1)
    return args
def phootowallrandom(groups, vk, text, albid="wall"):
    try
        a = args2()
        a = a.parse_args(text[1:])
    except:
        return
    photo2 = []
    if a.count > 10:
        a.count = 10
    for _ in range(a.count):
        group_id = random.choice(groups)
        max_num = vk.photos.get(owner_id=group_id, album_id=albid, count=0)['count']
        num = random.randint(0, max_num)
        photo = vk.photos.get(owner_id=group_id, album_id=albid,
                            count=1, offset=num)['items'][0]['id']
        photo2.append(f"photo{group_id}_{photo}")
    photo2 = ",".join(photo2)
    return photo2
def yuri(vk, text):
    photo = phootowallrandom(["-170165000", "-63092480", "-153284406"], vk, text)
    return {"message":"Юрец~~🌚", "attachment":photo}
def gebbels(vk, text):
    photo = phootowallrandom(["-174482230"], vk, text)
    return {"message":"ХАЧЕШЬ ЛИ ТЫ ТОТАЛЬНОЙ ВАЙНЫ?", "attachment":photo}
def yaoi(vk, text):
    photo = phootowallrandom(["-98467405", "-113004231", "-57807542", "-38230251"], vk, text)
    return {"message":"Яойчег~~🌚", "attachment":photo}
def trap(vk , text):
    photo = phootowallrandom(["-171834188"], vk, text)
    return {"message":"Трапы~~🌚", "attachment":photo}
def cats(vk , text):
    photo = phootowallrandom(["-43228812", "-34137527", "-152424758"], vk, text)
    return {"message":"Шавухенция на заказ", "attachment":photo}
def loli(vk , text):
    photo = phootowallrandom(["-127518015", "-157516431", "-69721869"], vk, text)
    return {"message":"FBI OPEN UP", "attachment":photo}
def mahno(vk , text):
    photo = phootowallrandom(["367919273"],vk, text, albid=262361216)
    return {"message":"СВОБОДА АБО ИДИТЕ НАХУЙ", "attachment":photo}
def citati(vk , text):
    photo = phootowallrandom(["-173186389"], vk, text)
    return {"message":"Цитатки на заказ", "attachment":photo}
def colyan(vk , text):
    photo = phootowallrandom(["-183493220"],vk, text,  albid=266695546)
    return {"message":"БОЖЕЕЕЕЕЕЕ, ЦАРЯ ХРАНИ", "attachment":photo}
def hentai(vk , text):
    photo = phootowallrandom(["-161403814", "-170993976"], vk, text)
    return {"message":"Хентай~~🌚", "attachment":photo}
def legs(vk , text):
    photo = phootowallrandom(["-174842315", "-102853758", "-134982584", "-138265009", "-114279288"], vk, text)
    return {"message": "Ножки &#127773;", "attachment": photo}
def mem(vk  , text):
    photo = phootowallrandom(["-154306815", "-142918020", "-120254617", "-79805359", "-150550417"], vk, text)
    return {"message": "Держи мемас", "attachment": photo}
def adolf(vk , text):
    photo = phootowallrandom(["-183493220"],vk, text,  albid=266718794)
    return {"message":"Хай фюрер", "attachment":photo}
