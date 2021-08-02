import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, homephone, mobilephone, workphone, secondaryphone) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, email=email, email2=email2, email3=email3,
                                    homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_in_group(self):
        dict = {}
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                if id in dict.keys():
                    value = dict.get(id)
                    value.append(group_id)
                else:
                    value = []
                    value.append(group_id)
                    dict[id] = value
        finally:
            cursor.close()
        return dict