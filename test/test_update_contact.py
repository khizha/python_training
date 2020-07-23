# -*- coding: utf-8 -*-
from model.contact import Contact

def test_update_contact(app):
     app.contact.open_first_contact_for_modification()
     app.contact.fill_in_new_contact_data(Contact(firstname="fff_upd", middlename="mmm_upd", lastname="lll_upd", nickname="kkk_upd", title="ttt_upd",
                                                  company="ccc_upd", address="aaa_upd", homeaddress="hhh_upd", mobilephone="7777777",
                                                  workphone="7777777", fax="7777777", email="f_upd@tt.tt",
                                                  email2="f2_upd@tt.tt", email3="f3_upd@tt.tt", homepage="http://home_upd.tt", birthday="22",
                                                  birthmonth="January", birthyear="1990", aday="24", amonth="February", ayear="1997", address2="ffffffffffffffffffffffff_upd",
                                                  phone2="7777777", notes="note_upd"))
     app.contact.submit_updated_contact()
