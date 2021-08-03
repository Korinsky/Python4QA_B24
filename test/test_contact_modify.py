# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="modufy_autotest", middlename=u"modufy_autotest", lastname=u"modufy_autotest",
                      nickname=u"modufy_autotest", address=u"modufy_autotest"))
    old_contacts = db.get_contacts_list()
    id = random.choice(old_contacts).id
    contact = Contact(firstname="modufy_autotest", middlename=u"modufy_autotest", lastname=u"modufy_autotest",
                      nickname=u"modufy_autotest", address=u"modufy_autotest")
    app.contact.modify_contact_by_id(id, contact)
    modify_contact_in_old_list(old_contacts, contact, id)
    new_contacts = db.get_contacts_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)


def modify_contact_in_old_list(old_contacts, contact, id):
    for i in old_contacts:
        if i.id == id:
            old_contacts.remove(i)
            contact.id = id
            old_contacts.append(contact)
