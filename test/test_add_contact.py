# -*- coding: utf-8 -*-
import pytest
import random
import string

from model.contact import Contact

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_only_digits(maxlen):
    digits_ = string.digits
    return "".join([random.choice(digits_) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", homephone="",
                      mobilephone="", workphone="", fax="", email="", email2="", email3="", homepage="", bday="1", bmonth="March",
                      byear="", aday="1", amonth="March", ayear="", address2="", secondaryphone="", notes="")]\
           + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 20), company=random_string("company", 10),
            address=random_string("address", 50), homephone=random_string_only_digits(12), mobilephone=random_string_only_digits(12),
            workphone=random_string_only_digits(12), fax=random_string_only_digits(10), email="myemail@mm.com",
            email2="tyhuor@ty.com", email3="tgbyu@uu.com", homepage=random_string("firstname", 10), bday="8", bmonth="March",
            byear="1909", aday="15", amonth="December", ayear="2010", address2=random_string("address2", 50),
            secondaryphone=random_string_only_digits(12), notes=random_string("notes", 50))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app,contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

