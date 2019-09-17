#!/usr/bin/env python
import random, sys, argparse
def args():
    args = argparse.ArgumentParser(description="генератор смеха")
    args.add_argument("-c", "--count", type=int, default=25)
    args.add_argument("-s", "--smex", default=None)
    args.add_argument("-s2", "--smexslova", default=None)
    return args
def smex(text):
    ss = args()
    try:
        ss = ss.parse_args(text[1:])
    except:
        return
    test = 0
    main = ["Х", "Ы", "Ъ"]
    if ss.smex != None:
        main = list(ss.smex)
    if ss.smexslova != None:
        main = ss.smexslova.split()
    mainsmex = []
    for _ in range(ss.count):
        mainsmex.append(random.choice(main))
    mainsmex = "".join(mainsmex)
    return {"message":mainsmex, "attachment": None}
