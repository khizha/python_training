
def test_phones_on_homepage(app):
    # compare the phone for the first contact on the homepage with the one from the contact edit page
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.homephone == contact_from_edit_page.homephone
    assert contact_from_homepage.workphone == contact_from_edit_page.workphone
    assert contact_from_homepage.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_homepage.phone2 == contact_from_edit_page.phone2
