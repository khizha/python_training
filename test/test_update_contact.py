# -*- coding: utf-8 -*-
from model.contact import Contact

def test_update_contact(app):
    if app.contact.count() != 0:
         old_contacts = app.contact.get_contacts_list()

         updated_contact = Contact(firstname="Name Updated", middlename="mmm_upd", lastname="Lastname Updated", nickname="kkk_upd", title="ttt_upd",
                                                      company="ccc_upd", address="aaa_upd", homeaddress="hhh_upd", mobilephone="7777777",
                                                      workphone="7777777", fax="7777777", email="f_upd@tt.tt",
                                                      email2="f2_upd@tt.tt", email3="f3_upd@tt.tt", homepage="http://home_upd.tt", birthday="22",
                                                      birthmonth="January", birthyear="1990", address2="ffffffffffffffffffffffff_upd",
                                                      phone2="7777777", notes="note_upd")

         updated_contact.id = old_contacts[0].id
         app.contact.open_first_contact_for_modification()
         app.contact.fill_in_new_contact_data(updated_contact)
         app.contact.submit_updated_contact()
         new_contacts = app.contact.get_contacts_list()

         assert len(old_contacts) == len(new_contacts)
         old_contacts[0] = updated_contact
         assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
