# base_page.py

from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage(ABC):
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @abstractmethod
    def path(self) -> str:
        """URL страницы — переопределяется в дочерних классах"""
        pass

    def open(self):
        """Открытие страницы по self.path()"""
        self.driver.get(self.path())

    def find_element(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible_element(self, locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator: tuple, text: str):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator: tuple) -> str:
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator: tuple) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_for_url(self, url_part: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))
            return True
        except:
            return False

    def is_opened(self) -> bool:
        """Проверяет, открыт ли путь, описанный в path()"""
        return self.driver.current_url.startswith(self.path())


    def wait_for_element(self, locator: tuple, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def is_element_visible(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
