# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


def test_del_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    app.group.delete_first()


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    app.group.modify_first(Group(name="modify", header="modify", footer="modify"))
