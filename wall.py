import time
from vk_api.utils import get_random_id
def post(vk, vk2):
    test2 = None
    test3 = None
    while 1:
        time.sleep(1)
        test = vk2.wall.get(owner_id="-59215051",count=2)
        if test["items"][1]['text'] == test3:
            continue
        else:
            test2 = test["items"][1]
            test3 = test2["text"]
            owner_id = test2["owner_id"]
            postid = test2["id"]
            post = f"wall{owner_id}_{postid}"
            vk.messages.send(user_id=367919273, random_id=get_random_id(),
                                message=f"Милорд, в риме пост:",
                                attachment=post)

