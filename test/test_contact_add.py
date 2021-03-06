# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contact, db, check_ui):
    contact = json_contact
    old_contacts = db.get_contacts_list()
    app.contact.create(contact)
    new_contacts = db.get_contacts_list()
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
