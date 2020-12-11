from sys import maxsize

class Contact:

    #def __init__(self, firstname, middlename, lastname, nickname, title, company, address, homeaddress, mobilephone,
    #                 workphone, fax, email, email2, email3, homepage, birthday, birthmonth, birthyear, address2, phone2, notes, id=None):
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, all_phones_from_homepage=None, fax=None, email=None, email2=None, email3=None, all_emails_from_homepage=None, homepage=None, birthday=None, birthmonth=None, birthyear=None, address2=None, phone2=None,
                 notes=None, id=None):

        self.firstname=firstname
        self.middlename=middlename
        self.lastname=lastname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.homephone=homephone
        self.mobilephone=mobilephone
        self.workphone=workphone
        self.all_phones_from_homepage=all_phones_from_homepage
        self.fax=fax
        self.email=email
        self.email2=email2
        self.email3=email3
        self.all_emails_from_homepage=all_emails_from_homepage
        self.homepage=homepage
        self.birthday=birthday
        self.birthmonth=birthmonth
        self.birthyear=birthyear
        self.address2=address2
        self.phone2=phone2
        self.notes=notes
        self.id = id

    def __repr__(self):
        # representation of the object in Console
        return "id: %s FN: %s LN: %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        # comparison of two objects
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname  and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize