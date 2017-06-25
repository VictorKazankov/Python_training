# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()

    contact = Contact(firstname="Victor", middlename="Ivanovich", lastname="Kazankov", nickname="Six", title="MyTitle",
                      company="MyCompany", address="MyAddress", homephone="380555555", mobilephone="8099258789",
                      workphone="9874444444", fax="285999999", email="myemail@mm.com", email2="tyhuor@ty.com",
                      email3="tgbyu@uu.com", homepage="myhomepage", bday="8", bmonth="March", byear="1909", aday="15",
                      amonth="December", ayear="2010", address2="MyAddress2", secondaryphone="2345678", notes="MyNotes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
#                       mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="1", bmonth="March",
#                       byear="", aday="1", amonth="March", ayear="", address2="", phone2="", notes="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
