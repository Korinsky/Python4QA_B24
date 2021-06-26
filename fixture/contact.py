class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.app.navigation.open_add_contact_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("submit").click()
        self.app.navigation.open_home_page()

    def modify_first(self, new_text):
        wd = self.app.wd
        wd.find_element_by_xpath("//tr[2]//img[@title='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").send_keys(new_text)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").send_keys(new_text)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").send_keys(new_text)
        wd.find_element_by_name("update").click()
        self.app.navigation.open_home_page()

    def delete_first(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//tr[3]//input[@name='selected[]']").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
