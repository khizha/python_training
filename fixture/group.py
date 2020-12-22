from selenium.webdriver.support.ui import Select
from model.group import Group
from model.relations import Relations
import random

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        # check that we are not already on groups page
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit created group
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # find Edit button and click it to edit the selected group
        wd.find_element_by_name("edit").click()
        # fill in the group form
        self.fill_group_form(group)
        # submit the updated group information
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        # select the first group in the list
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        # select the target (index) group in the list
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        # select the target (index) group in the list
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        # find Edit button and click it to edit the selected group
        wd.find_element_by_name("edit").click()
        # fill in the group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def modify_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        # find Edit button and click it to edit the selected group
        wd.find_element_by_name("edit").click()
        # fill in the group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def open_groups_page(self):
        wd = self.app.wd
        # if the current page address ends with "\group.php" and there is a button with name "new" on this page then
        # this is a correct page
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        # check if group cache is empty
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                # get attribute value from checkbox element residing inside span element
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def remove_random_contact_from_random_group(self):
    # from the homepage get the list of groups that contain contacts
        groups_list = []
        contact_ids_list = []
        removed_relation = Relations()

        wd = self.app.wd
        # go to the homepage
        self.app.open_home_page()

        # open the "groups" drop-down list and get all the groups from there
        dropdown_elements = wd.find_elements_by_xpath("//select[@name='group']/option")
        for element in dropdown_elements:
            if element.text != "[all]" and element.text != "[none]":
                groups_list.append(Group(name=element.text, id=element.get_attribute("value")))

        # if the list is not empty
        if (len(groups_list)!= 0):
            # get a random group from the list above
            selected_group = random.choice(groups_list)

            # select the chosen group from the drop-down list and click it
            Select(wd.find_element_by_name("group")).select_by_visible_text(selected_group.name)
            wd.find_element_by_xpath("//option[@value='%s']" % selected_group.id).click()

            # get all the contact names from the opened list
            for contacts_table_row in wd.find_elements_by_name("entry"):
                # get the list of cells in the current table row
                row_contents = contacts_table_row.find_elements_by_tag_name("td")
                # get the contact id:
                # id = row_contents[0].find_element_by_name("selected[]").get_attribute("value")
                contact_ids_list.append(row_contents[0].find_element_by_name("selected[]").get_attribute("value"))

            # if the list of contact ids is not empty
            if (len(contact_ids_list) != 0):
                # get a random contact if from the list above
                selected_contact_id = random.choice(contact_ids_list)

                # click the selected group and remove it by clicking the Remove button
                wd.find_element_by_id(selected_contact_id).click()
                wd.find_element_by_name("remove").click()

                removed_relation = Relations(cid=selected_contact_id, gid=selected_group.id)

        return removed_relation
