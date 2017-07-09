import random
import string
import os.path
import jsonpickle
import getopt
import sys

from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o =="-f":
        f = a

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_only_digits(maxlen):
    digits_ = string.digits
    return "".join([random.choice(digits_) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 20), company=random_string("company", 10),
            address=random_string("address", 50), homephone=random_string_only_digits(12), mobilephone=random_string_only_digits(12),
            workphone=random_string_only_digits(12), fax=random_string_only_digits(10), email="myemail@mm.com",
            email2="tyhuor@ty.com", email3="tgbyu@uu.com", homepage=random_string("firstname", 10), bday="8", bmonth="March",
            byear="1909", aday="15", amonth="December", ayear="2010", address2=random_string("address2", 50),
            secondaryphone=random_string_only_digits(12), notes=random_string("notes", 50))
    for i in range(n)
]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))