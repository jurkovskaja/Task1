# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.firefox.webdriver import WebDriver

from model.contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Task1_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_contact(self, wd, contact):
        # init add address book
        wd.find_element_by_link_text("add new").click()
        # fill address book form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("%s" % contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("%s" % contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % contact.home)
        # enter phone numbers
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("%s" % contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("%s" % contact.fax)
        # enter email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("%s" % contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("%s" % contact.email3)
        # enter homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("%s" % contact.homepage)
        # enter birthday
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//%s" % contact.date).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//%s" % contact.date).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//%s" % contact.month).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//%s" % contact.month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % contact.byear)
        # enter anniversary
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//%s" % contact.aday).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//%s" % contact.aday).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//%s" % contact.amonth).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//%s" % contact.amonth).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("%s" % contact.ayear)
        # secondary
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("%s" % contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("%s" % contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("%s" % contact.notes)

    def save_change(self, wd):
        # save change, clicked 'Enter'
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self, wd):
        # return to home page, clicked 'home page'
        wd.find_element_by_xpath("//div/div[4]/div/i/a[2]").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_Task1_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="qwee", middlename="qwere", lastname="qwerqwetqe", nickname="dfgfdg",
                            title="dfgnhgf", company="sdfsdfsdf", address="qwerwreqer", home="11", mobile_phone="22",
                            work_phone="33", fax="444", email="5555", email2="666", email3="777", homepage="sadffasd",
                            address2="1wrtrewer", phone2="phone2", notes="sdfgnvbxfgsdf", date="option[18]",
                            month="option[12]", byear="123", aday="option[31]", amonth="option[2]", ayear="1231"))
        self.save_change(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()