# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_del_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(name="modify", header="modify", footer="modify"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)