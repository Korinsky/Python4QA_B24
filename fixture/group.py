class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_pages(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_pages()

    def delete_first(self):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        # select first group
        self.select_first_group(wd)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_pages()

    def select_first_group(self, wd):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first(self, group):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        # select first group
        self.select_first_group(wd)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_groups_pages()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
