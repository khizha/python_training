from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

# add a random contact into a random group via UI
def test_add_contact_into_group(app, db):
    # if the groups list is empty
    #if len(db.get_group_list()) == 0:
    if app.group.count() == 0:
        app.group.create(Group(name="TestGroup"))

    # if the contacts list is empty
    if app.contact.count() == 0:
        contact = Contact(firstname="nnnn", lastname="mmmm", address="", homephone="", mobilephone="", workphone="", email="", email2="", email3="", phone2="")

        app.contact.open_new_contact_page()
        app.contact.fill_in_new_contact_data(contact)
        app.contact.submit_created_contact()

    # get the old list of contacts from the DB
    contacts_list = db.get_contact_list()

    # get the old list of groups from the DB
    groups_list = db.get_group_list()
    db2 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

    contacts_2_add = []

    # before the contact is added: number of contacts in the group where the new contact will be added
    old_contacts_in_group_list = []

    for gr in groups_list:
        old_contacts_in_group_list = db.get_contacts_for_current_group(gr.id)
        contacts_2_add = db2.get_contacts_not_in_group(gr)
        if len(contacts_2_add) > 0:
            # add random contact from contacts_2_add list into gr group
            random_contact = random.choice(contacts_2_add)
            #add_rand_contact_to_group(app, contacts_2_add, gr)
            app.contact.add_contact_to_group(random_contact.id, gr.name, gr.id)
            #new_contacts_in_group_list = db.get_contacts_for_current_group(gr.id)
            break

    if len(contacts_2_add) == 0:
        # create a group
        app.group.create(Group(name="TestGroup"))

        #find the created group id
        new_groups = db.get_group_list()
        gr = sorted(new_groups, key=Group.id_or_max)[-1]

        # add random contact from contacts_list list into gr group

        random_contact = random.choice(contacts_list)
        # add_rand_contact_to_group(app, contacts_2_add, gr)
        app.contact.add_contact_to_group(random_contact.id, gr.name, gr.id)

        #add_rand_contact_to_group(app, contacts_list, gr)

    # after the contact is added: number of contacts in the group where the new contact is added
    new_contacts_in_group_list = db.get_contacts_for_current_group(gr.id)

    assert len(new_contacts_in_group_list) == len(old_contacts_in_group_list) + 1

    # check that the selected contact is in the selected group
    assert db.contact_is_in_group(random_contact.id, gr.id)