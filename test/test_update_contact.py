# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact

def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="Victor", middlename ="", lastname ="Kazankov", nickname ="",
                                   title = "", company = "", address = "", home = "",
                                   mobilephone="", workphone="", fax ="", email ="",
                                   email2 = "", email3 = "", homepage = "",
                                   bday = "1", bmonth = "March", byear = "", aday = "1", amonth = "March", ayear = "", address2 = "",
                                   secondaryphone="", notes =""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Victor_update", middlename="Ivanovic_update", lastname="Kazankov_update",
                      nickname="Six_update", title="MyTitle_update", company="MyCompany_update",
                      address="MyAddress_update", home="+380000000", mobilephone="800000000", workphone="900000000",
                      fax="200000000", email="myemail_update@mm.com", email2="tyhuor_update@ty.com",
                      email3="tgbyu_update@uu.com", homepage="myhomepage_update", bday="1", bmonth="April",
                      byear="1900", aday="16", amonth="-", ayear="2001", address2="MyAddress2_update",
                      secondaryphone="23000000", notes="MyNotes_update")
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)