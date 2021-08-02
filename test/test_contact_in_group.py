from model.group import Group
from model.contact import Contact


def test_add_contact_in_group(app, db):
    # создаём записи, если нет контактов или групп
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="Autotest", lastname=u"Autotest", address=u"Autotest"))

    # сохраняем в словарь данные из таблицы БД "address_in_groups"
    contact_in_group = db.get_contact_in_group()

    # выбираем контакт и группу и выполняем привязку
    contact_id, group_id = search_contact_without_group(app, db, contact_in_group)
    app.contact.add_contact_in_group(contact_id, group_id)

    # обновляем данные из БД и провеяем, что привязка состоялась
    new_contact_in_group = db.get_contact_in_group()
    assert contact_id in new_contact_in_group and group_id in new_contact_in_group[contact_id]


def test_remove_contact_in_group(app, db):
    # создаём записи, если нет контактов или групп
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="Autotest", lastname=u"Autotest", address=u"Autotest"))

    # получаем исходные данные из БД
    contact_in_group = db.get_contact_in_group()
    groups = [int(g.id) for g in db.get_groups_list()]
    contacts = [int(c.id) for c in db.get_contacts_list()]

    # проверяем наличие привязки контакт-группа и создаём, если отсутствует
    if contact_in_group == {}:
        app.contact.add_contact_in_group(contacts[0], groups[0])
        contact_in_group = db.get_contact_in_group()

    # выбираем контакт и группу для удалния привязки и удаляем привязку
    contact_id, group_id = search_contact_in_group(contact_in_group)
    app.contact.remove_contact_from_group(contact_id, group_id)

    # обновляем данные из БД и провеяем, что привязки в таблице нет
    new_contact_in_group = db.get_contact_in_group()
    assert contact_id not in new_contact_in_group or group_id not in new_contact_in_group[contact_id]


def search_contact_without_group(app, db, dict):
    groups = [int(g.id) for g in db.get_groups_list()]
    contacts = [int(c.id) for c in db.get_contacts_list()]
    # ищем свободную связь контакт-группа
    for id in contacts:
        if int(id) not in dict:
            return id, groups[0]
        elif len(dict[int(id)]) < len(groups):
            return id, list(set(groups) - set(dict[int(id)]))[0]

    # создаём новую группу, так как все имеющиеся контакты находятся во всех группах
    app.group.create(Group(name="Autotest", header="Autotest", footer="Autotest"))
    new_groups = [int(g.id) for g in db.get_groups_list()]
    return contacts[0], list(set(new_groups) - set(groups))[0]


def search_contact_in_group(dict):
    for key in dict:
        return key, dict[key][0]
