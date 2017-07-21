# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_update_group_name(app, db, json_groups):
    group_data = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #group_data.id = old_groups.id
    app.group.update_group_by_id(group.id, group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    # old_groups.clear()
    # old_groups.append(group_data)
    old_groups[group] = group_data
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
