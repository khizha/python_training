# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contacts_list()

    app.contact.open_new_contact_page()
    app.contact.fill_in_new_contact_data(contact)
    app.contact.submit_created_contact()

     # check that the new contacts list is 1 element longer than the old list
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()

    max_ = new_contacts[0].id
    for i in new_contacts:
        if i.id > max_:
            max_ = i.id

    contact.id = max_
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
