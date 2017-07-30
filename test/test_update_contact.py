# -*- coding: utf-8 -*-
import random
from model.contact import Contact

def test_update_contact(app, db, json_contacts, check_ui):
    contact_data = json_contacts
    if app.contact.count() == 0:
        app.contact.create(contact_data)
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_data.id = contact.id
    app.contact.update_contact_by_id(contact.id, contact_data)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)