from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.test_scenarios_page import TestScenariosPage
from config.config import BASE_URL


# ---------------- TC07 ----------------
# Alerts Handling
def test_alerts_handling(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login("admin@example.com", "Admin@123")

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()

    dashboard.open_test_scenarios()

    scenarios_page = TestScenariosPage(driver)

    # Alert
    assert scenarios_page.handle_alert()

    # Confirm
    confirm_text = scenarios_page.handle_confirm()
    assert "Accepted" in confirm_text

    # Prompt
    prompt_text = scenarios_page.handle_prompt("Automation Test")
    assert "Automation Test" in prompt_text


# ---------------- TC08 ----------------
# Frames + Tabs + Popup Windows
def test_frames_tabs_and_windows(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login("admin@example.com", "Admin@123")

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()

    dashboard.open_test_scenarios()

    scenarios_page = TestScenariosPage(driver)

    # Step 1: Switch to iframe
    assert scenarios_page.switch_to_iframe_and_verify()

    # Step 2: Open new tab
    assert scenarios_page.open_new_tab_and_validate()

    # Step 3: Open popup window
    assert scenarios_page.open_popup_and_switch_back()