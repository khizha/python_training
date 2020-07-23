# -*- coding: utf-8 -*-

def test_delete_first_contact(app):
    # if contacts list is empty
    if app.contact.count() != 0:
        app.contact.delete_first_contact()