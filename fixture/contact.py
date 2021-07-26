from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.navigation.open_add_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.app.navigation.open_home_page()

    def modify_first(self, contact):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_xpath("//tr[2]//img[@title='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.navigation.open_home_page()

    def delete_first(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_xpath("//tr[2]//input[@name='selected[]']").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_contact_list(self):
        wd = self.app.wd
        self.app.navigation.open_add_contact_page()
        self.app.navigation.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("td.center input"):
            email = element.get_attribute("accept")
            id = element.get_attribute("id")
            contacts.append(Contact(email=email, id=id))
        return contacts
