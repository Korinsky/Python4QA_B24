# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname=u"Иван", middlename=u"Иванович", lastname=u"Иванов", nickname=u"Ива", address=u"дом", home="+7111111", email="qq@qq.com"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", address="", home="", email=""))
    app.session.logout()


def test_del_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first()
    app.session.logout()


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(" (обновлено)")
    app.session.logout()
