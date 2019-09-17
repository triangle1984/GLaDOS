#!/usr/bin/env python
import random, sys, argparse
def args():
    args = argparse.ArgumentParser(description="генератор смеха")
    args.add_argument("-c", "--count", type=int, default=25)
    args.add_argument("-s", "--smex", default=None)
    args.add_argument("-s2", "--smexslova", default=None)
    return args
def smex(text):
    helps = """а це посложнее. Для этой хуйни я проработал целую систему аргументов:
    /смех -c (число) = количество символов в смехе
    /смех -s (буквы) = символы для генерации смеха
    /смех -s2 (слово) = слово для генерации смеха
    -c и -s/s2 можно использовать одновременно
    /смех -s2 .exe -c 69
    /смех -s хпх -c 50"""
    ss = args()
    try:
        ss = ss.parse_args(text[1:])
        proverta = text[1]
    except:
        return {"message":helps, "attachment": None}
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
