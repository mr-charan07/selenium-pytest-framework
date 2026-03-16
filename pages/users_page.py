# This file defines the UsersPage class, 
# which represents the users page of the application. 
# It contains a method to check if the users table is visible on the page.

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_visible


class UsersPage(BasePage):

    users_table = (By.XPATH, "//table[contains(@class,'table-hover')]")

    def is_users_table_visible(self):

        wait_for_element_visible(self.driver, self.users_table)

        return True