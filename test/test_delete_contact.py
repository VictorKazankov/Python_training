from random import randrange
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname ="", middlename ="", lastname ="", nickname ="",
                               title = "", company = "", address = "", home = "",
                               mobile = "", work = "", fax = "", email = "",
                               email2 = "", email3 = "", homepage = "",
                               bday = "1", bmonth = "March", byear = "", aday = "1", amonth = "March", ayear = "", address2 = "",
                               phone2 = "", notes = ""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)