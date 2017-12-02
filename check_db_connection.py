import pymysql.cursors
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact


#db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_contacts_email_list()
    #for item in l:
     #   print(item)
    #print(len(l))
    m = len(l)
    print(m)
    print(l)
finally:
    pass #db.destroy()

