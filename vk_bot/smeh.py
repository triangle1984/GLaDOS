#!/usr/bin/env python
import random, sys, argparse
from vksql import smehdb
def args():
    args = argparse.ArgumentParser(description="генератор смеха")
    args.add_argument("-c","-с", "--count", type=int, default=random.randint(5, 50))
    args.add_argument("-s", "--smex", default='None')
    args.add_argument("-s2", "--smexslova", default='None')
    return args
def smex(text, uid, db=False):
    helps = """а це посложнее. Для этой хуйни я проработал целую систему аргументов:
    /смех -c (число) = количество символов в смехе
    /смех -s (буквы) = символы для генерации смеха
    /смех -s2 (слово) = слово для генерации смеха
    -c и -s/s2 можно использовать одновременно
    примеры:
    /смех -s2 .exe -c 69
    /смех -s хпх -c 50
    /смех -s хпхп
    /смех -c 69
    А так же, все тоже самое, но со /смехк - запишет ваши настройки для генератора
    То есть: после /смехк -s2 .exe -c 69 , в /смех без аргументов - будет
    использоваться то, что вы передали в /смехк
    """
    ss = args()
    try:
        ss = ss.parse_args(text[1:])
        proverka = text[1]
    except IndexError:
        ss2 =  smehdb(ss, uid, db)
        if ss2:
            ss = ss2
    except:
        return {"message":helps}
    if db:
        smehdb(ss, uid, db)
    if ss.count > 9999:
        return
    test = 0
    main = ["Х", "Ы", "Ъ"]
    if ss.smex != 'None':
        main = list(ss.smex)
    if ss.smexslova != 'None':
        main = ss.smexslova.split()
    mainsmex = []
    for _ in range(ss.count):
        mainsmex.append(random.choice(main))
    mainsmex = "".join(mainsmex)
    return {"message":mainsmex, "attachment": 'None'}
