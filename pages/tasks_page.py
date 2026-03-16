from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_visible, wait_for_element_clickable


class TasksPage(BasePage):

    # ---------------- Page Elements ----------------

    tasks_table = (By.XPATH, "//table")

    new_task_button = (
        By.XPATH,
        "//button[contains(@class,'btn-primary') and contains(.,'New Task')]"
    )

    title_input = (By.XPATH, "//label[text()='Title']/following::input[1]")

    description_textarea = (
        By.XPATH,
        "//label[text()='Description']/following::textarea[1]"
    )

    status_dropdown = (
        By.XPATH,
        "//label[text()='Status']/following::select[1]"
    )

    save_task_button = (
        By.XPATH,
        "//button[contains(@class,'btn-primary') and contains(.,'Save Task')]"
    )

    # Edit button for blocked task
    edit_blocked_task_button = (
        By.XPATH,
        "//tr[.//span[contains(text(),'blocked')]]//button[contains(text(),'Edit')]"
    )

    # Done status indicator in table
    done_status_label = (
        By.XPATH,
        "//span[contains(text(),'done')]"
    )

    # ---------------- Page Checks ----------------

    def is_tasks_table_visible(self):
        table = wait_for_element_visible(self.driver, self.tasks_table)
        return table.is_displayed()

    # ---------------- Create Task ----------------

    def click_new_task(self):
        wait_for_element_clickable(self.driver, self.new_task_button).click()

    def enter_title(self, title):
        wait_for_element_visible(self.driver, self.title_input).send_keys(title)

    def enter_description(self, description):
        wait_for_element_visible(self.driver, self.description_textarea).send_keys(description)

    def select_status(self, status):
        dropdown = wait_for_element_visible(self.driver, self.status_dropdown)

        options = dropdown.find_elements(By.TAG_NAME, "option")

        for option in options:
            if option.text.lower() == status.lower():
                option.click()
                break

    def click_save_task(self):
        wait_for_element_clickable(self.driver, self.save_task_button).click()

    def create_task(self, title, description, status="todo"):

        self.click_new_task()

        self.enter_title(title)

        self.enter_description(description)

        self.select_status(status)

        self.click_save_task()

    # ---------------- Update Task Status ----------------

    def open_blocked_task_edit(self):

        wait_for_element_clickable(
            self.driver,
            self.edit_blocked_task_button
        ).click()

    def update_status_to_done(self):

        dropdown = wait_for_element_visible(self.driver, self.status_dropdown)

        options = dropdown.find_elements(By.TAG_NAME, "option")

        for option in options:
            if option.text.lower() == "done":
                option.click()
                break

        self.click_save_task()

    def is_task_marked_done(self):

        status = wait_for_element_visible(self.driver, self.done_status_label)

        return status.is_displayed()