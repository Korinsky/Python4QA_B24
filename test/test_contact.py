# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=u"Иван", middlename=u"Иванович", lastname=u"Иванов", nickname=u"Ива", address=u"дом", home="+7111111", email="qq@qq.com")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", address="", home="", email="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", middlename=u"Autotest", lastname=u"Autotest", nickname=u"Autotest", address=u"Autotest", home="Autotest", email="autotest@qq.com"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", middlename=u"Autotest", lastname=u"Autotest", nickname=u"Autotest", address=u"Autotest", home="Autotest", email="autotest@qq.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="modufy_autotest", middlename=u"modufy_autotest", lastname=u"modufy_autotest", nickname=u"modufy_autotest", address=u"modufy_autotest", home="modufy_autotest", email="modufy_autotest@qq.com")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
