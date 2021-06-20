# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname=u"Иван", middlename=u"Иванович", lastname=u"Иванов", nickname=u"Ива", address=u"дом", home="+7111111", email="qq@qq.com"))
    app.logout()