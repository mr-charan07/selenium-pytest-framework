from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_visible, wait_for_element_clickable
from utils.logger import get_logger


class LoginPage(BasePage):

    logger = get_logger()

    email_input = (By.XPATH, "//input[@placeholder='Enter email']")
    password_input = (By.XPATH, "//input[@placeholder='Enter password']")
    login_button = (By.XPATH, "//button[@type='submit']")

    def enter_email(self, email):
        self.logger.info("Entering email")
        wait_for_element_visible(self.driver, self.email_input).send_keys(email)

    def enter_password(self, password):
        self.logger.info("Entering password")
        wait_for_element_visible(self.driver, self.password_input).send_keys(password)

    def click_login(self):
        self.logger.info("Clicking login button")
        wait_for_element_clickable(self.driver, self.login_button).click()

    def login(self, email, password):
        self.logger.info("Starting login process")
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        self.logger.info("Login action completed")