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
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts