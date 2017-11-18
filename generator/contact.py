# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import json
import getopt # чтение опций командной строки
import sys # для получения доступа к опциям командной строки

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number og groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# генерация случайных строк не превышаюших длину maxlen
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), address=(random_string("adress", 10)),
            home=random_string("home", 10), mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
            phone2=random_string("phone", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), middlename="", nickname="", title="", company="", fax="", homepage="",
            address2="", notes="", date="", byear="", ayear="")
            for i in range(n)
]

# сохранение сгенерированных данных в файл
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f) # путь к файлу

with open(file, "w") as out: # открываем файл на запись
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))