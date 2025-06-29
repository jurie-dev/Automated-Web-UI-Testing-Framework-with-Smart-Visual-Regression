from pages.login_page import LoginPage


def test_successful_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Verify successful login by checking URL or presence of element
    assert "inventory.html" in driver.current_url
