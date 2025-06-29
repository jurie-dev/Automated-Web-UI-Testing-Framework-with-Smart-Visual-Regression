from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")

    def add_item_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()
