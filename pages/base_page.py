# base_page.py

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from locators.locators import *

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def send_keys(self, locator, text: str):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element(self, locator):
        return self.wait_for_element(locator)

    def get_text(self, locator):
        return self.wait_for_element(locator).text

    def fill_input(self, locator, text: str):
        self.send_keys(locator, text)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False


    #@allure.step("Проверить, что модальное окно ингридиента закрыто")
    def is_close_modal_ingr(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(ConstructorPageLocators.CONSTRUCTOR_LINK)
            )
            return True
        except TimeoutException:
            return False
