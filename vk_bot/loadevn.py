from dotenv import dotenv_values
parsed = dotenv_values(stream="config.env")
token = parsed["token"]
token22 = parsed["token22"]
group_idd = parsed["group_idd"]
recipient = parsed["recipient"]
allowuser = parsed["allowuser"].split(",")
ip = parsed["ip"]
tablechat = parsed["tablechat"]
apinews = parsed["apinews"]
chathello = parsed["chathello"]
password = parsed["password"]
user = parsed["user"]
