# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname=u"Иван", middlename=u"Иванович", lastname=u"Иванов", nickname=u"Ива", address=u"дом", home="+7111111", email="qq@qq.com"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", address="", home="", email=""))


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", middlename=u"Autotest", lastname=u"Autotest", nickname=u"Autotest", address=u"Autotest", home="Autotest", email="autotest@qq.com"))
    app.contact.delete_first()


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", middlename=u"Autotest", lastname=u"Autotest", nickname=u"Autotest", address=u"Autotest", home="Autotest", email="autotest@qq.com"))
    app.contact.modify_first(" (обновлено)")
