# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Autotest", middlename=u"Autotest", lastname=u"Autotest", nickname=u"Autotest", address=u"Autotest", home="Autotest", email="autotest@qq.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="modufy_autotest", middlename=u"modufy_autotest", lastname=u"modufy_autotest", nickname=u"modufy_autotest", address=u"modufy_autotest", home="modufy_autotest", email="modufy_autotest@qq.com")
    contact.id = old_contacts[0].id
    app.contact.modify_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
