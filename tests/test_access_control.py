from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.users_page import UsersPage
from config.config import BASE_URL


def test_admin_users_page(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login("admin@example.com", "Admin@123")

    # wait until dashboard loads
    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()

    # now go to users page
    driver.get(BASE_URL + "/users")

    users_page = UsersPage(driver)

    assert users_page.is_users_table_visible()
    
# This test verifies that a non-admin user cannot access the users page 
# is either redirected or blocked from accessing it.
def test_non_admin_access_restriction(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    # login as normal user
    login_page.login("john@example.com", "Admin@123")

    # try opening admin page
    driver.get(BASE_URL + "/users")

    # check if redirected or access blocked
    assert "users" not in driver.current_url