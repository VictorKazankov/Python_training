# -*- coding: utf-8 -*-
from model.group import Group


def test_update_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.update_first_group(Group(name ="qwert_update", header ="werty_update", footer ="yuiop_update"))
    app.session.logout()