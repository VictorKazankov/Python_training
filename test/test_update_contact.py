# -*- coding: utf-8 -*-
import random
import string
import pytest
from data.contacts import testdata_simple

from model.contact import Contact


@pytest.mark.parametrize("contact", testdata_simple, ids=[repr(x) for x in testdata_simple])
def test_update_contact(app, contact):
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    index = random.randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)