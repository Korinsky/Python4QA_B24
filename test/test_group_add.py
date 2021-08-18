# -*- coding: utf-8 -*-
from model.group import Group
import pytest

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step("Given a group list"):
        old_groups = db.get_groups_list()
    with pytest.allure.step("When I add the group %s to the list" % group):
        app.group.create(group)
    with pytest.allure.step("Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_groups_list()
        old_groups.append(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
