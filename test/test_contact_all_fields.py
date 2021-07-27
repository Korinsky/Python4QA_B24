from model.contact import Contact
from random import randrange
import re


def check_miss_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=u"Иван", lastname=u"Иванов", address=u"Город\nУлица\nДом",
                                   email="qwe@qq.com", email2="qwe22@qq.com", email3="qwe33@qq.com",
                                   homephone="+111111", mobilephone="22 22", workphone="3(33)33", secondaryphone="44-44-4"))


def test_firstname_home_vs_edit(app):
    check_miss_contact(app)
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    print("проверяем контакт id %s, firstname %s" % (contact_from_home_page.id, contact_from_home_page.firstname))
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname


def test_lastname_home_vs_edit(app):
    check_miss_contact(app)
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_address_home_vs_edit(app):
    check_miss_contact(app)
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_email_home_vs_edit(app):
    check_miss_contact(app)
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phone_home_vs_edit(app):
    check_miss_contact(app)
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
