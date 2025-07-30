
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

# Explicitly wait for an element to be present in the DOM and return it, or raise an exception if not found within the timeout
    def find_element(self, locator, timeout=10):
        print("Finding element:", locator)
        if not isinstance(locator, tuple):
            raise ValueError("Locator must be a tuple (By, value)")
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))

# Check if an element is present in the DOM and return True or False
    def is_element_present(self, locator, timeout=10):
        try:
            self.find_element(locator, timeout)
            print("Element found:", locator)
            return True
        except (NoSuchElementException, ElementNotVisibleException, TimeoutException):
            return False
        
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        if not element.is_displayed():
            raise ElementNotVisibleException(f"Element {locator} is not visible")
        if not element.is_enabled():
            raise ElementNotVisibleException(f"Element {locator} is not enabled")
        print("Clicking on element:", locator)
        if not element.is_selected():
            print("Element is not selected, clicking now.")
        else:
            print("Element is already selected, no need to click.")
        element.click()

    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        if not element.is_displayed():
            raise ElementNotVisibleException(f"Element {locator} is not visible")
        if not element.is_enabled():
            raise ElementNotVisibleException(f"Element {locator} is not enabled")
        print("Entering text in element:", locator)
        if not isinstance(text, str):
            raise ValueError("Text must be a string")
        element.clear()
        element.send_keys(text)
   
    def get_current_url(self):
        return self.driver.current_url
