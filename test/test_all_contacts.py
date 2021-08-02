from model.contact import Contact
import re


def check_miss_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=u"Иван", lastname=u"Иванов", address=u"Город\nУлица\nДом",
                                   email="qwe@qq.com", email2="qwe22@qq.com", email3="qwe33@qq.com",
                                   homephone="+111111", mobilephone="22 22", workphone="3(33)33", secondaryphone="44-44-4"))

def test_all_contacts(app, db):
    check_miss_contact(app)
    db_contacts_list = db.get_contacts_list()
    for db_contact in db_contacts_list:
        id = db_contact.id
        page_contact = app.contact.get_contact_data_by_id(id)
        db_contact.all_emails_from_home_page = merge_emails_like_on_home_page(db_contact)
        db_contact.all_phones_from_home_page = merge_phones_like_on_home_page(db_contact)
        assert db_contact == page_contact


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
