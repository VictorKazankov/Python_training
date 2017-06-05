# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname = "Victor", middlename = "Ivanovich", lastname = "Kazankov", nickname = "Six",
                                    title = "MyTitle", company = "MyCompany", address = "MyAddress", home = "+380555555",
                                    mobile = "8099258789", work = "9874444444", fax = "285999999", email = "myemail@mm.com",
                                    email2 = "tyhuor@ty.com", email3 = "tgbyu@uu.com", homepage = "myhomepage",
                                    bday = "8", bmonth = "March", byear = "1909", aday = "15", amonth = "December", ayear = "2010", address2 = "MyAddress2",
                                    phone2 = "2345678", notes = "MyNotes"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname = "", middlename = "", lastname = "", nickname = "",
                                    title = "", company = "", address = "", home = "",
                                    mobile = "", work = "", fax = "", email = "",
                                    email2 = "", email3 = "", homepage = "",
                                    bday = "1", bmonth = "March", byear = "", aday = "1", amonth = "March", ayear = "", address2 = "",
                                    phone2 = "", notes = ""))
    app.logout()

