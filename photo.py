import vk_api, requests, os
from vk_api.utils import get_random_id
def cats(vk, text, event, upload):
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

    if "chat_id" in dir(event):
        vk.messages.send(chat_id=event.chat_id, random_id=get_random_id()
                        , message="шавуха по заказу",
                        attachment=vk_photo_url)
    else:
        vk.messages.send(user_id=event.user_id, random_id=get_random_id()
                        , message="шавуха по заказу",
                        attachment=vk_photo_url)
