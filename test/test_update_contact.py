# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_update_contact(app):
    if app.contact.count() != 0:
         old_contacts = app.contact.get_contacts_list()
         index = randrange(len(old_contacts))

         updated_contact = Contact(firstname="Name Updated", middlename="mmm_upd", lastname="Lastname Updated", nickname="kkk_upd", title="ttt_upd",
                                                      company="ccc_upd", address="aaa_upd", homeaddress="hhh_upd", mobilephone="7777777",
                                                      workphone="7777777", fax="7777777", email="f_upd@tt.tt",
                                                      email2="f2_upd@tt.tt", email3="f3_upd@tt.tt", homepage="http://home_upd.tt", birthday="22",
                                                      birthmonth="January", birthyear="1990", address2="ffffffffffffffffffffffff_upd",
                                                      phone2="7777777", notes="note_upd")

         updated_contact.id = old_contacts[index].id
         app.contact.open_contact_for_modification_by_index(index)
         app.contact.fill_in_new_contact_data(updated_contact)
         app.contact.submit_updated_contact()

         assert len(old_contacts) == app.contact.count()
         new_contacts = app.contact.get_contacts_list()

         old_contacts[index] = updated_contact

         print("  ")
         print("********* old_contacts[index] ************")
         print(old_contacts[index])


         print("  ")
         print("********* OLD ************")
         for el in old_contacts:
             print(el)

         print("  ")
         print("********* NEW ************")
         for el in new_contacts:
             print(el)

         assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
