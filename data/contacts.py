import random
import string

from model.contact import Contact


def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_only_digits(maxlen):
    digits_ = string.digits
    return "".join([random.choice(digits_) for i in range(random.randrange(maxlen))])


testdata_simple = [
    Contact(firstname="Victor", middlename="Ivanovich", lastname="Kazankov", nickname="Six",
            title = "MyTitle", company = "MyCompany", address = "MyAddress", homephone = "+380555555",
            mobilephone = "8099258789", workphone = "9874444444", fax = "285999999", email = "myemail@mm.com",
            email2 = "tyhuor@ty.com", email3 = "tgbyu@uu.com", homepage = "myhomepage",
            bday = "8", bmonth = "March", byear = "1909", aday = "15", amonth = "December", ayear = "2010", address2 = "MyAddress2",
            secondaryphone = "2345678", notes = "MyNotes"),
    Contact(firstname="Victor2", middlename="Ivanovich2", lastname="Kazankov2", nickname="Six",
            title = "MyTitle", company = "MyCompany", address = "MyAddress", homephone = "+380555555",
            mobilephone = "8099258789", workphone = "9874444444", fax = "285999999", email = "myemail@mm.com",
            email2 = "tyhuor@ty.com", email3 = "tgbyu@uu.com", homepage = "myhomepage",
            bday = "8", bmonth = "March", byear = "1909", aday = "15", amonth = "December", ayear = "2010", address2 = "MyAddress2",
            secondaryphone = "2345678", notes = "MyNotes")
]