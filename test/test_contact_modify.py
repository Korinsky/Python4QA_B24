# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", middlename=u"Autotest", lastname=u"Autotest",
                                   nickname=u"Autotest", address=u"Autotest", home="Autotest"))
    old_contacts = app.contact.get_contact_list()
    index = randrange((len(old_contacts)))
    contact = Contact(firstname="modufy_autotest", middlename=u"modufy_autotest", lastname=u"modufy_autotest",
                      nickname=u"modufy_autotest", address=u"modufy_autotest", home="modufy_autotest")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
