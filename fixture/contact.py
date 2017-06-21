from model.contact import Contact


class ContactHelper:
    def __init__(self,app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)

        # contact submit
        wd.find_element_by_xpath("//input[@name='submit']").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd

        # add primary contact parameters
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)

        # add contact phones
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)

        # add emails
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

        # add home page
        self.change_field_value("homepage", contact.homepage)

        # add data of born
        # self.change_field_value("//select[@name = 'bday']//option[@value = %s]" % contact.bday, contact.bday)
        # self.change_field_value("//select[@name = 'bmonth']//option[@value = '%s']" % contact.bmonth, contact.bmonth)

        wd.find_element_by_xpath("//select[@name = 'bday']//option[@value = %s]" % contact.bday).click()
        wd.find_element_by_xpath("//select[@name = 'bmonth']//option[@value = '%s']" % contact.bmonth).click()

        self.change_field_value("byear", contact.byear)

        # add dare of anniversary
        # self.change_field_value("//select[@name = 'aday']//option[@value = %s]" % contact.aday, contact.aday)
        # self.change_field_value("//select[@name = 'amonth']//option[@value = '%s']" % contact.amonth, contact.amonth)

        wd.find_element_by_xpath("//select[@name = 'aday']//option[@value = %s]" % contact.aday).click()
        wd.find_element_by_xpath("//select[@name = 'amonth']//option[@value = '%s']" % contact.amonth).click()

        self.change_field_value("ayear", contact.ayear)

        # add secondary parameters
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(text)

    def update_first_contact(self, new_contact_data):
        wd = self.app.wd
        # переход на страницу home page
        self.open_home_page()
        self.open_edit_contact_page()
        self.fill_contact_form(new_contact_data)

        # contact update
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("searchstring")) > 0):
           wd.find_element_by_xpath("//div[@id='nav']//a[.='home']").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
           wd.find_element_by_link_text("add new").click()

    def open_edit_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title = 'Edit']").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath(".//tbody/tr[@name='entry']"):
                first_name = element.find_element_by_xpath(".//td[3]").text
                second_name = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_xpath(".//td[@class='center']/input").get_attribute("value")
                self.contact_cache.append(Contact(firstname=first_name,lastname=second_name,id=id))
        return list(self.contact_cache)