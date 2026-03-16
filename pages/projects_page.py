from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_visible


class ProjectsPage(BasePage):

    projects_table = (By.XPATH, "//table[contains(@class,'table')]")

    def is_projects_table_visible(self):
        table = wait_for_element_visible(self.driver, self.projects_table)
        return table.is_displayed()

    def is_project_present(self, project_name):
        project_locator = (
            By.XPATH,
            f"//div[contains(@class,'fw-semibold') and contains(text(),'{project_name}')]"
        )

        project = wait_for_element_visible(self.driver, project_locator)
        return project.is_displayed()