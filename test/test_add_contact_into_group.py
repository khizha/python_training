from model.contact import Contact
from model.group import Group
from model.relations import Relations
import random

# add a random contact into a random group via UI
def test_add_contact_into_group(app, db):
    # if the contacts list is not empty
    if app.contact.count() != 0:

        # get the old list of contacts from the DB
        old_contacts = db.get_contact_list()

        # get the old list of groups from the DB
        old_groups = db.get_group_list()

        # get a random contact from the contacts list
        target_contact = random.choice(old_contacts)

        # get a random group from the groups list
        target_group = random.choice(old_groups)

        # the selected contact ID is target_contact.id
        # get the selected contact index in the homepage
        ui_contacts_list = app.contact.get_contacts_list()
        target_contact_ui_index = ui_contacts_list.index(target_contact)

        # the selected group ID is target_group.id

        # add the selected contact to the selected group
        app.contact.add_contact_to_group(target_contact.id, target_contact_ui_index, target_group.name, target_group.id)

        # check that the selected group contains the selected contact
        relations_list = db.get_group_contact_relations_list()
        target_relation = Relations(cid=target_contact.id, gid=target_group.id)
        #print(target_relation in relations_list)
        assert target_relation in relations_list

