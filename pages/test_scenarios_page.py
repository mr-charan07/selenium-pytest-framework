from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_clickable, wait_for_element_visible


class TestScenariosPage(BasePage):

    # -------- Alerts --------

    alert_button = (By.ID, "btn-simple-alert")
    confirm_button = (By.ID, "btn-confirm")
    prompt_button = (By.ID, "btn-prompt")

    confirm_result = (By.ID, "confirm-result")
    prompt_result = (By.ID, "prompt-result")

    # -------- Tabs / Windows --------

    new_tab_button = (By.XPATH, "//button[contains(text(),'Open New Tab')]")
    popup_button = (By.XPATH, "//button[contains(text(),'Open Popup Window')]")

    # -------- Iframe --------

    iframe_element = (By.XPATH, "//iframe")

    # ---------------- ALERT ----------------

    def handle_alert(self):

        wait_for_element_clickable(self.driver, self.alert_button).click()

        alert = self.driver.switch_to.alert
        alert.accept()

        return True

    # ---------------- CONFIRM ----------------

    def handle_confirm(self):

        wait_for_element_clickable(self.driver, self.confirm_button).click()

        alert = self.driver.switch_to.alert
        alert.accept()

        result = wait_for_element_visible(self.driver, self.confirm_result)

        return result.text

    # ---------------- PROMPT ----------------

    def handle_prompt(self, text):

        wait_for_element_clickable(self.driver, self.prompt_button).click()

        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

        result = wait_for_element_visible(self.driver, self.prompt_result)

        return result.text

    # ---------------- IFRAME ----------------

    def switch_to_iframe_and_verify(self):

        iframe = wait_for_element_visible(self.driver, self.iframe_element)

        self.driver.switch_to.frame(iframe)

        content_present = "Example Domain" in self.driver.page_source

        self.driver.switch_to.default_content()

        return content_present

    # ---------------- NEW TAB ----------------

    def open_new_tab_and_validate(self):

        original_window = self.driver.current_window_handle

        wait_for_element_clickable(self.driver, self.new_tab_button).click()

        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)

        url = self.driver.current_url
        title = self.driver.title

        self.driver.close()

        self.driver.switch_to.window(original_window)

        return ("example.com" in url) and ("Example Domain" in title)

    # ---------------- POPUP ----------------

    def open_popup_and_switch_back(self):

        original_window = self.driver.current_window_handle

        wait_for_element_clickable(self.driver, self.popup_button).click()

        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)

        popup_title = self.driver.title

        self.driver.close()

        self.driver.switch_to.window(original_window)

        return "Example Domain" in popup_title