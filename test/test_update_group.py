# -*- coding: utf-8 -*-
from model.group import Group


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.update_first_group(Group(name ="New group"))

def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    app.group.update_first_group(Group(header ="New header"))