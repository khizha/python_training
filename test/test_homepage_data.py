from model.contact import Contact
import re

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

        # iterate through all the contacts
        for i in range(len(ui_contacts_sorted)):
            #print("")
            #print("---------------- i ---------------")
            #print(i)

            # validate the first name for the selected contact
            assert ui_contacts_sorted[i].firstname == db_contacts_sorted[i].firstname

            # validate the last name for the selected contact
            assert ui_contacts_sorted[i].lastname == db_contacts_sorted[i].lastname

            # validate the address for the selected contact
            assert ui_contacts_sorted[i].address == db_contacts_sorted[i].address

            # validate the e-mails for the selected contact
            assert ui_contacts_sorted[i].all_emails_from_homepage == merge_emails_like_on_homepage(db_contacts_sorted[i])

            # validate the phones for the selected contact
            assert ui_contacts_sorted[i].all_phones_from_homepage == merge_phones_like_on_homepage(db_contacts_sorted[i])

def clear(s):
    # remove the following symbols from the s string: "()", " ", "-"
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))

def merge_emails_like_on_homepage(contact):
    #strip()
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: str(x).strip(),
                                filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3]))))
