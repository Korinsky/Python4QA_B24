# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=u"Иван", lastname=u"Иванов", address=u"Город\nУлица\nДом", email="qwe@qq.com",
                      homephone="+111111", mobilephone="22 22", workphone="3(33)33", secondaryphone="44-44-4")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
