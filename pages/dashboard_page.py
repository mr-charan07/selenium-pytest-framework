from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_visible, wait_for_element_clickable


class DashboardPage(BasePage):

    # sidebar dashboard link
    dashboard_link = (By.XPATH, "//a[contains(@href,'/dashboard')]")

    projects_menu = (By.XPATH, "//a[contains(@href,'/projects')]")

    tasks_menu = (By.XPATH, "//a[contains(@href,'/tasks')]")
    
    test_scenarios_menu = (By.XPATH, "//a[contains(.,'Test Scenarios')]")

    def open_test_scenarios(self):
        wait_for_element_clickable(self.driver, self.test_scenarios_menu).click()
        
    def is_dashboard_loaded(self):

        dashboard = wait_for_element_visible(self.driver, self.dashboard_link)

        return dashboard.is_displayed()

    def open_projects(self):

        wait_for_element_clickable(self.driver, self.projects_menu).click()

    def open_tasks(self):

        wait_for_element_clickable(self.driver, self.tasks_menu).click()