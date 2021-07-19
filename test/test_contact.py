# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname=u"Иван", middlename=u"Иванович", lastname=u"Иванов", nickname=u"Ива", address=u"дом", home="+7111111", email="qq@qq.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", address="", home="", email=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", middlename=u"Autotest", lastname=u"Autotest", nickname=u"Autotest", address=u"Autotest", home="Autotest", email="autotest@qq.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", middlename=u"Autotest", lastname=u"Autotest", nickname=u"Autotest", address=u"Autotest", home="Autotest", email="autotest@qq.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first(Contact(firstname="modufy_autotest", middlename=u"modufy_autotest", lastname=u"modufy_autotest", nickname=u"modufy_autotest", address=u"modufy_autotest", home="modufy_autotest", email="modufy_autotest@qq.com"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
