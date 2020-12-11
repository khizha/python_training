import re
from random import randrange

def test_contact_page_data(app):
    #validate contact first name, last name, address, phones and e-mails on the homepage against the corresponding data on the edit page

    # select random contact for validation
    index = randrange(len(app.contact.get_contacts_list()))

    # get contact data from home page
    contact_from_homepage = app.contact.get_contacts_list()[index]

    # get contact data from edit page
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    # validate the phones for the selected contact
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

    # validate the e-mails for the selected contact
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)

    # validate the address for the selected contact
    assert contact_from_homepage.address == contact_from_edit_page.address

    # validate the first name for the selected contact
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname

    # validate the last name for the selected contact
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname

def test_names_on_homepage(app, index):
    # compare the phone for the contact defined by index in the contacts list on the homepage with the one from the contact edit page
    contact_from_homepage = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

def clear(s):
    # remove the following symbols from the s string: "()", " ", "-"
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.homephone, contact.workphone, contact.mobilephone, contact.phone2]))))

def merge_emails_like_on_homepage(contact):
    #strip()
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: str(x).strip(),
                                filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3]))))
