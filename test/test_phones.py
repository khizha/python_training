import re

def test_phones_on_homepage(app):
    # compare the phone for the first contact on the homepage with the one from the contact edit page
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contacts_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert merge_phones_like_on_homepage(contact_from_view_page) == merge_phones_like_on_homepage(contact_from_edit_page)

def clear(s):
    # remove the following symbols from the s string: "()", " ", "-"
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.homephone, contact.workphone, contact.mobilephone, contact.phone2]))))
