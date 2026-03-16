import pytest
from pages.login_page import LoginPage
from config.config import BASE_URL
from pages.dashboard_page import DashboardPage
from utils.data_loader import get_test_data


def test_valid_login(driver):

    driver.get(BASE_URL)

    data = get_test_data("valid_login")

    login_page = LoginPage(driver)

    login_page.login(data["email"], data["password"])

    print(driver.current_url)

    dashboard = DashboardPage(driver)

    assert dashboard.is_dashboard_loaded()


@pytest.mark.parametrize("data", get_test_data("invalid_login"))
def test_invalid_login(driver, data):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(data["email"], data["password"])

    assert "login" in driver.current_url