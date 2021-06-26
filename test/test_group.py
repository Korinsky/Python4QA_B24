# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="qwe", header="qwe", footer="qwe"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


def test_del_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first()
    app.session.logout()


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="modify", header="modify", footer="modify"))
    app.session.logout()
