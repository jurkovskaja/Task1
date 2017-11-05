from model.contact import Contact


class ContactHelper:

    def __init__(self,app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init add address book
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        self.submit_add_contact()
        self.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        # enter birthday

        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//%s" % contact.date).is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[1]//%s" % contact.date).click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//%s" % contact.month).is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[2]//%s" % contact.month).click()
        # enter anniversary
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//%s" % contact.aday).is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[3]//%s" % contact.aday).click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//%s" % contact.amonth).is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[4]//%s" % contact.amonth).click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        self.click_on_delete_button()
        # submit deletion
        wd.switch_to_alert().accept()
        self.click_on_home_link()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def click_on_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()

    def select_change_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def click_on_home_link(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def submit_add_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def count(self):
        wd = self.app.wd
        # number of contact in the list
        return len(wd.find_elements_by_name("selected[]"))

    def select_firstname(self):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()

    def submit_modify_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def modify_contact_firstname(self, contact):
        wd = self.app.wd
        self.select_change_contact()
        self.select_firstname()
        self.fill_contact_form(contact)
        self.submit_modify_contact()
        self.return_to_home_page()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=text, id=id))
        return list(self.contact_cache)
