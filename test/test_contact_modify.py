# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", middlename=u"Autotest", lastname=u"Autotest",
                                   nickname=u"Autotest", address=u"Autotest"))
    old_contacts = db.get_contact_list()
    id = random.choice(old_contacts).id
    contact = Contact(firstname="modufy_autotest", middlename=u"modufy_autotest", lastname=u"modufy_autotest",
                      nickname=u"modufy_autotest", address=u"modufy_autotest")
    app.contact.modify_contact_by_id(id, contact)
    for i in old_contacts:
        if i.id == id:
            old_contacts.remove(i)
            old_contacts.append(Contact(firstname="modufy_autotest", middlename=u"modufy_autotest", lastname=u"modufy_autotest",
                      nickname=u"modufy_autotest", address=u"modufy_autotest", id=i.id))
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
