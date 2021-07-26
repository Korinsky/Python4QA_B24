from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, address=None, email=None, home=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.home = home
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.email == other.email

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
