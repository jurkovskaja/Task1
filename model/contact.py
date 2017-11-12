from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None, mobile_phone=None,
                       work_phone=None, fax=None, email=None, email2=None, email3=None, homepage=None, address2=None, phone2=None, notes=None, date=None, month=None, byear=None,
                       aday=None, amonth=None, ayear=None, id=None, all_phones_from_home_page=None, all_email_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        #self.date = date
        #self.month = month
        self.byear = byear
        #self.aday = aday
        #self.amonth = amonth
        self.ayear = ayear
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
