import vk_api, requests, os, random
from vk_api.utils import get_random_id
def cats(upload):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    r = r.json()
    command = "wget {} -O test.jpg".format(r[0]["url"])
    os.system(command)
    photo = upload.photo(
        '/home/archie/vk-bot/test.jpg',
        album_id=268910446
        )
    vk_photo_url = 'photo{}_{}'.format(
            photo[0]['owner_id'], photo[0]['id'])
    return {"message":"шавуха по заказу", "attachment":vk_photo_url}
def yuri(vk, upload):
    group_id = "-170165000"
    max_num = vk.photos.get(owner_id=group_id, album_id='wall', count=0)['count']
    num = random.randint(0, max_num)
    photo = vk.photos.get(owner_id=group_id, album_id='wall',
                          count=1, offset=num)['items'][0]['id']
    photo = f"photo{group_id}_{photo}"
    return {"message":"Юрец~~🌚", "attachment":photo}
