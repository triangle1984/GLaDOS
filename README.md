# vk-bot
## Гайд по запуску
для начала ```  pip install -r requirments.txt```, чтобы установить зависимости.
Дальше нужно заполнить недо-конфигурционный файл, с токенами и прочем: token2.py
Создаете его в vk_bot и заполняете
### Пример token2.py
token = "токен группы(main2.py)  
token22 = "Токен юзера, если надо страничного бота(main.py)"  
group_idd = "айди группы"  
recipient = айди, на который будут приходить уведомления о новом юзере в группе  
allowuser = [Список разрешенных юзеров, которым будет отвечать страничный бот(через запятую)]  
ip = "Айпи к бд  
tablechat = "Название таблицы, в которой будут хранится айдишники чатов для рассылки"  
apinews = "a8443b51a5544447a5a919bcbca46b8a" для /новость   

## Бд (mysql)

### Данные для подключения
Кроме указания айпишника, возможно вам еще понадобится немного подправить данные для подключения  
Сделать вы можете это в *репа/vk_bot/vksql.py
В самом начале будет ```python conn = pymysql.connect(host=ip,
                             user="root",  
                             password="123",  
                             db="mydb",  
                             cursorclass=DictCursor) ```
### Нужные таблицы
admins с (id int)
ban, с (id int)
то, что вы указали в tablechat, так же с (id int)
prefix с (id int, name varchar)
smehgen с (id int, count int, smeh varchar, smehslova varchar)
