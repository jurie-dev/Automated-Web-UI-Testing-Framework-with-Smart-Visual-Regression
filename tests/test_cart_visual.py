import os
import time
import pytest
import pytest_html
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.visual_compare import compare_images


def ensure_directories():
    os.makedirs("screenshots/baseline", exist_ok=True)
    os.makedirs("screenshots/current", exist_ok=True)
    os.makedirs("screenshots/diff", exist_ok=True)


def test_cart_visual_regression(driver):
    ensure_directories()

    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    time.sleep(2)

    screenshot_path = "screenshots/current/cart.png"
    baseline_path = "screenshots/baseline/cart.png"
    diff_path = "screenshots/diff/cart_diff.png"

    driver.save_screenshot(screenshot_path)

    assert compare_images(baseline_path, screenshot_path, diff_path), "Visual regression detected!"


@pytest.mark.parametrize("browser", ["chrome"])
def test_login_ui(driver, request, browser):
    ensure_directories()

    driver.get("https://www.saucedemo.com")

    baseline_path = "screenshots/baseline/login.png"
    current_path = "screenshots/current/login.png"
    diff_path = "screenshots/diff/login_diff.png"

    driver.save_screenshot(current_path)

    if not os.path.exists(baseline_path):
        driver.save_screenshot(baseline_path)

    assert compare_images(baseline_path, current_path, diff_path), "Login page UI mismatch!"

    if request.config.pluginmanager.hasplugin("html"):
        extra = getattr(request.node, 'extra', [])
        if os.path.exists(diff_path):
            extra.append(pytest_html.extras.image(diff_path))
        request.node.extra = extra
