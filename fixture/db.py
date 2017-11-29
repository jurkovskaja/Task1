import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)


    def get_group_list(self): # загружает список групп из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self): # загружает список контактов из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address))
        finally:
            cursor.close()
        return list


    def get_contacts_phones_list(self): # загружает список телефонов у контактов из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, home, mobile, work, phone2 from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, home, mobile, work, phone2 ) = row
                list.append(Contact(id=str(id),home=home, mobile_phone=mobile, work_phone=work, phone2=phone2))
        finally:
            cursor.close()
        return list


    def get_contacts_email_list(self): # загружает список email у контактов из БД
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, email, email2, email3  from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, email, email2, email3 ) = row
                list.append(Contact(id=str(id), email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()