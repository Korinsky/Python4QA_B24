from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, address=None, email=None, email2=None, email3=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone= secondaryphone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s" % (self.id, self.firstname, self.lastname, self.address, self.all_emails_from_home_page, self.all_phones_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname and self.address == other.address and self.all_emails_from_home_page == other.all_emails_from_home_page and self.all_phones_from_home_page == other.all_phones_from_home_page


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
