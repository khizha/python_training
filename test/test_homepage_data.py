from model.contact import Contact

# compare all the contacts data in UI with the corresponding data in DB
def test_homepage_data(app, db):

    # if contacts list is not empty
    if app.contact.count() != 0:

        # check that UI and DB contacts lists are of the same length
        assert len(db.get_contact_list()) == app.contact.count()

        # sort DB contacts list by id
        db_contacts_sorted = sorted(db.get_contact_list(), key=Contact.id_or_max)

        # sort UI contacts list by id
        ui_contacts_sorted = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)

        for i in range (len(ui_contacts_sorted)):
            # for now not all the contact parameters are retrieved by get_contact methods of DB and UI objects, so
            # check that at least first names an last names of the current contact are equal
            are_equal = (ui_contacts_sorted[i].firstname == db_contacts_sorted[i].firstname) and (ui_contacts_sorted[i].lastname == db_contacts_sorted[i].lastname)
            assert are_equal


