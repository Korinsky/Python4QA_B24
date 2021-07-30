# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modify", header="modify", footer="modify")
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
