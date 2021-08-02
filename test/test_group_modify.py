# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    old_groups = db.get_groups_list()
    id = random.choice(old_groups).id
    group = Group(name="modify", header="modify", footer="modify")
    app.group.modify_group_by_id(id, group)
    for i in old_groups:
        if i.id == id:
            old_groups.remove(i)
            old_groups.append(Group(name="modify", header="modify", footer="modify", id=id))
    new_groups = db.get_groups_list()
    assert sorted(old_groups, key=Group.id_or_max) ==  sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
