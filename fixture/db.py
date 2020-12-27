import pymysql.cursors
from model.group import Group
from model.contact import Contact
from model.relations import Relations

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # autocommit=True parameter cleans up database cache after each db request
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
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

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, email=email, email2=email2, email3=email3, homephone=home, mobilephone=mobile, workphone=work, phone2=phone2))
        finally:
            cursor.close()
        return list

    def get_group_contact_relations_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(Relations(cid=str(id), gid=str(group_id)))
        finally:
            cursor.close()
        return list

    def get_contacts_for_current_group(self, groupid):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                if str(group_id) == groupid:
                    list.append(str(id))
        finally:
            cursor.close()
        return list

    def contact_is_in_group(self, targetcontactid, targetgrid):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                if str(group_id) == targetgrid:
                    if str(id) == targetcontactid:
                        return True
        finally:
            cursor.close()
        return False