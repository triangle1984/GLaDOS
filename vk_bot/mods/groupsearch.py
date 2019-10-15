import random
__doc__ = "Найти паблики по названию  и скинуть айди"
__command__ = "/паблики"
def main(**args):
    vk = args["vk2"]
    result = vk.groups.search(q=" ".join(args["text"][1:]), count=15)["items"]
    gid = []
    for _ in range(10):
        idd = str(random.choice(result)["id"])
        if idd not in gid:
            gid.append("-" + idd)
    gid = ",".join(gid)
    return {"message":f"Паблики: {gid}"}
