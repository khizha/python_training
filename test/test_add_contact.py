# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
     old_contacts = app.contact.get_contacts_list()
     app.contact.open_new_contact_page()
     new_contact = Contact(firstname="Added firstname", middlename="Added", lastname="Added lastname", nickname="kkk", title="ttt",
                                                  company="ccc", address="aaa", homeaddress="hhh", mobilephone="5555555",
                                                  workphone="5555555", fax="5555555", email="f@tt.tt",
                                                  email2="f2@tt.tt", email3="f3@tt.tt", homepage="http://home.tt", birthday="12",
                                                  birthmonth="January", birthyear="1999",
                                                  address2="ffffffffffffffffffffffff",
                                                  phone2="5555555", notes="note")
     app.contact.fill_in_new_contact_data(new_contact)
     app.contact.submit_created_contact()

     new_contacts = app.contact.get_contacts_list()
     # check that the new contacts list is 1 element longer than the old list
     assert len(old_contacts) + 1 == len(new_contacts)

     max_ = new_contacts[0].id
     for i in new_contacts:
         if i.id > max_:
            max_ = i.id

     new_contact.id = max_
     old_contacts.append(new_contact)

     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
