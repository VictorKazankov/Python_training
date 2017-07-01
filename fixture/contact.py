from model.contact import Contact
import re

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
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
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
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("notes", contact.notes)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(text)


    def update_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        # переход на страницу home page
        self.open_home_page()
        self.select_contact_edit_by_index(index)
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

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

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
                cells = element.find_elements_by_tag_name("td")
                firstname = element.find_element_by_xpath(".//td[3]").text
                #firstname = cells[1].text
                lastname = element.find_element_by_xpath(".//td[2]").text
                #lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                #id = element.find_element_by_xpath(".//td[@class='center']/input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page = all_phones))
        return list(self.contact_cache)

    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.open_home_page()
    #         self.contact_cache = []
    #         for element in wd.find_elements_by_name("entry"):
    #             cells = element.find_elements_by_tag_name("td")
    #             first_name = cells[1].text
    #             second_name = cells[2].text
    #             id = cells[0].find_element_by_tag_name("input").get_attribute("value")
    #             all_phones = cells[5].text
    #             self.contact_cache.append(Contact(firstname=first_name, lastname=second_name, id=id,
    #                                               all_phones_from_home_page = all_phones))
    #     return list(self.contact_cache)


    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.select_contact_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname = firstname, lastname=lastname, id = id,
                       homephone = homephone, mobilephone = mobilephone,
                       workphone = workphone, secondaryphone = secondaryphone)


    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)
