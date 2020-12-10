import re

def test_phones_on_homepage(app):
    # compare the phone for the first contact on the homepage with the one from the contact edit page
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_homepage.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_homepage.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_homepage.phone2 == clear(contact_from_edit_page.phone2)

def clear(s):
    # remove the following symbols from the s string: "()", " ", "-"
    return re.sub("[() -]", "", s)
