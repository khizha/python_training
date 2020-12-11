from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit_created_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def fill_in_new_contact_data(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        #wd.find_element_by_name("theform").click()
        #wd.find_element_by_name("middlename").click()
        #wd.find_element_by_name("middlename").clear()
        #wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        #wd.find_element_by_name("nickname").click()
        #wd.find_element_by_name("nickname").clear()
        #wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # driver.find_element_by_name("photo").click()
        # driver.find_element_by_name("photo").clear()
        # driver.find_element_by_name("photo").send_keys("C:\\Users\\Alexe\\OneDrive\\Picture\\no_avatar-a59d170622fa19bc16aae3756b1e8db1.png")
        #wd.find_element_by_name("title").click()
        #wd.find_element_by_name("title").clear()
        #wd.find_element_by_name("title").send_keys(contact.title)
        #wd.find_element_by_name("company").click()
        #wd.find_element_by_name("company").clear()
        #wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        #wd.find_element_by_name("fax").click()
        #wd.find_element_by_name("fax").clear()
        #wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        #wd.find_element_by_name("homepage").click()
        #wd.find_element_by_name("homepage").clear()
        #wd.find_element_by_name("homepage").send_keys(contact.homepage)
        #wd.find_element_by_name("bday").click()
        #Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthday)
        #wd.find_element_by_xpath("//option[@value=" + contact.birthday + "]").click()
        #wd.find_element_by_name("bmonth").click()
        #Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthmonth)
        #wd.find_element_by_xpath("//option[@value='" + contact.birthmonth + "']").click()
        #wd.find_element_by_name("byear").click()
        #wd.find_element_by_name("byear").clear()
        #wd.find_element_by_name("byear").send_keys(contact.birthyear)
        #wd.find_element_by_name("address2").click()
        #wd.find_element_by_name("address2").clear()
        #wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        #wd.find_element_by_name("notes").click()
        #wd.find_element_by_name("notes").clear()
        #wd.find_element_by_name("notes").send_keys(contact.notes)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact
        # find first contact in the table by name and click (check) the checkbox
        wd.find_elements_by_name("selected[]")[index].click()
        # deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept the contact deletion in the appeared dialog box
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def open_first_contact_for_modification(self):
        self.open_contact_for_modification_by_index(0)

    def open_contact_for_modification_by_index(self, index):
        wd = self.app.wd
        # if we are not already on a edit contact page
        if not ('addressbook/edit.php' in wd.current_url and len(wd.find_elements_by_name("update")) == 2):
            # select the index contact
            # find index contact in the table by name and click (check) the checkbox
            wd.find_elements_by_name("selected[]")[index].click()
            # find and click Edit icon to start contact modification
            wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def submit_updated_contact(self):
        wd = self.app.wd
        # find by name and click "Update" button
        wd.find_element_by_name("update").click()
        # return to homepage
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def open_new_contact_page(self):
        wd = self.app.wd
        # if we are not already on a new contact page
        if not (wd.current_url.endswith("addressbook/edit.php") and len(wd.find_elements_by_name("submit")) == 2):
            wd.find_element_by_id("header").click()
            wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        # open contacts, i.e. home page
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        # check if contacts cache is empty
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []

            # scan the table rows
            for contacts_table_row in wd.find_elements_by_name("entry"):
                # get the list of cells in the current table row
                row_contents = contacts_table_row.find_elements_by_tag_name("td")

                # read the phones, but do not split them
                all_phones = row_contents[5].text

                # read the e-mails, but do not split them
                all_emails = row_contents[4].text

                extracted_contact = Contact(firstname=row_contents[2].text,
                                            lastname=row_contents[1].text,
                                            id=row_contents[0].find_element_by_name("selected[]").get_attribute("value"),
                                            all_phones_from_homepage=all_phones,
                                            all_emails_from_homepage=all_emails,
                                            address=row_contents[3].text)
                self.contact_cache.append(extracted_contact)

        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_for_modification_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")

        id = wd.find_element_by_name("id").get_attribute("value")

        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")

        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        address = wd.find_element_by_name("address").get_attribute("value")

        # return to homepage
        wd.find_element_by_link_text("home").click()

        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, phone2=phone2,
                       email=email, email2=email2, email3=email3,
                       address=address)

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        # get full text from the contact page
        text = wd.find_element_by_id("content").text
        # get phones from the full text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        # return to homepage
        wd.find_element_by_link_text("home").click()
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, phone2=phone2)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        # select the index contact
        # find index contact in the table by name and click (check) the checkbox
        wd.find_elements_by_name("selected[]")[index].click()
        # find and click Edit icon to start contact modification
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()