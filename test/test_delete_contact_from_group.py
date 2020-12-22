from model.contact import Contact
from model.group import Group
from model.relations import Relations

# remove a random contact from a random group from the groups with contacts list via UI
def test_delete_contact_from_group(app, db):
    # check if any group<->contact relations exist in DB
    if (len(db.get_group_contact_relations_list()) !=0):

        removed_relation = Relations()

        # remove random contact from a random group in UI
        removed_relation = app.group.remove_random_contact_from_random_group()

        # check if the relation is not empty, i.e. some random contact was removed from a random group
        if removed_relation.cid is not None and removed_relation.gid is not None:

            # check that the removed contact<->group relation does not exist in the DB
            relations_list = db.get_group_contact_relations_list()
            assert removed_relation not in relations_list
        else:
            print("")
            print("------------ NOTHING REMOVED -----------------")


    else:
        print("")
        print("------------ RELATIONS TABLE EMPTY -----------------")

