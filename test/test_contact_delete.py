# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", lastname=u"Autotest", address=u"Autotest"))
    old_contacts = app.contact.get_contact_list()
    index = randrange((len(old_contacts)))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
