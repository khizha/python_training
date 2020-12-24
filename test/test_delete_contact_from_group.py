from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

# remove a random contact from a random group from the groups with contacts list via UI
def test_delete_contact_from_group(app, db):
    # if the groups list is empty
    if app.group.count() == 0:
        app.group.create(Group(name="TestGroup"))

    # if the contacts list is empty
    if app.contact.count() == 0:
        contact = Contact(firstname="nnnn", lastname="mmmm", address="", homephone="", mobilephone="", workphone="", email="", email2="", email3="", phone2="")

    # get the old list of contacts from the DB
    contacts_list = db.get_contact_list()

    # get the old list of groups from the DB
    groups_list = db.get_group_list()
    db2 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    for gr in groups_list:
        contacts_2_delete = db2.get_contacts_in_group(gr)
        if len(contacts_2_delete)>0:
            # delete random contact from contacts_2_delete list from gr group
            random_contact = random.choice(contacts_2_delete)
            app.contact.delete_contact_from_group(random_contact.id, gr.name, gr.id)
            break

    #if contacts_2_delete is null then add contact to group and delete the contact from the group;
    if len(contacts_2_delete) == 0:
        # i.e. there are no groups with added contacts
        # add a random contact from the available contacts into the current group gr
        random_contact = random.choice(contacts_list)
        app.contact.add_contact_to_group(random_contact.id, gr.name, gr.id)

        # and now delete the added contact from the group
        app.contact.delete_contact_from_group(random_contact.id, gr.name, gr.id)
