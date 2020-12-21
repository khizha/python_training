# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_update_contact(app, db, check_ui):
    if app.contact.count() != 0:
        old_contacts = db.get_contact_list()

        # get a random contact from the contacts list
        target_contact = random.choice(old_contacts)

        updated_contact = Contact(firstname="Name Updated", middlename="mmm_upd", lastname="Lastname Updated", nickname="kkk_upd", title="ttt_upd",
                                   company="ccc_upd", address="aaa_upd", homephone="hhh_upd", mobilephone="7777777",
                                   workphone="7777777", fax="7777777", email="f_upd@tt.tt",
                                   email2="f2_upd@tt.tt", email3="f3_upd@tt.tt", homepage="http://home_upd.tt", birthday="22",
                                   birthmonth="January", birthyear="1990", address2="ffffffffffffffffffffffff_upd",
                                   phone2="7777777", notes="note_upd")

        updated_contact.id = target_contact.id

        # get the index of the selected random contact in the UI
        ui_contacts_list = app.contact.get_contacts_list()
        index = ui_contacts_list.index(target_contact)

        app.contact.open_contact_for_modification_by_id(updated_contact.id, index)
        app.contact.fill_in_new_contact_data(updated_contact)
        app.contact.submit_updated_contact()

        assert len(old_contacts) == app.contact.count()
        new_contacts = db.get_contact_list()

        # substitute old contacts list element with given id with the updated contact
        for i in range(len(old_contacts)):
            if old_contacts[i].id == target_contact.id:
                old_contacts[i] = updated_contact

        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)