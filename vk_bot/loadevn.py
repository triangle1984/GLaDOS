from dotenv import dotenv_values
parsed = dotenv_values(stream="config.env")
token = parsed["token"]
token22 = parsed["token22"]
group_idd = parsed["group_idd"]
recipient = parsed["recipient"]
try:
    allowuser = parsed["allowuser"].split(",")
except KeyError:
    pass
ip = parsed["ip"]
tablechat = parsed["tablechat"]
apinews = parsed["apinews"]
chathello = parsed["chathello"]
password = parsed["password"]
user = parsed["user"]
db = parsed["db"]
donatetoken = parsed["donatetoken"]
fontc = parsed["font"]
speechtotext = parsed["speechtotext"]
permban = parsed["permban"]