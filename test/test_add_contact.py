# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
     app.contact.open_new_contact_page()
     app.contact.fill_in_new_contact_data(Contact(firstname="fff", middlename="mmm", lastname="lll", nickname="kkk", title="ttt",
                                                  company="ccc", address="aaa", homeaddress="hhh", mobilephone="5555555",
                                                  workphone="5555555", fax="5555555", email="f@tt.tt",
                                                  email2="f2@tt.tt", email3="f3@tt.tt", homepage="http://home.tt", birthday="12",
                                                  birthmonth="January", birthyear="1999", aday="14", amonth="February", ayear="1987", address2="ffffffffffffffffffffffff",
                                                  phone2="5555555", notes="note"))
     app.contact.submit_created_contact()
