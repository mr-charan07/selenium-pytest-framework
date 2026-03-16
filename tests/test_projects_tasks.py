from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.tasks_page import TasksPage
from config.config import BASE_URL


# Test: Verify tasks table loads successfully
def test_task_status_update(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login("admin@example.com", "Admin@123")

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()

    dashboard.open_tasks()

    tasks_page = TasksPage(driver)

    assert tasks_page.is_tasks_table_visible()

    # open blocked task
    tasks_page.open_blocked_task_edit()

    # change status → done
    tasks_page.update_status_to_done()

    # verify status updated
    assert tasks_page.is_task_marked_done()


# Test: Verify user can create a new task
def test_create_task(driver):

    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login("admin@example.com", "Admin@123")

    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_loaded()

    dashboard.open_tasks()

    tasks_page = TasksPage(driver)
    assert tasks_page.is_tasks_table_visible()

    # Create new task
    tasks_page.create_task(
        "Automation Task",
        "Testing task creation through automation",
        "todo"
    )

    # Verify tasks table still visible after creation
    assert tasks_page.is_tasks_table_visible()