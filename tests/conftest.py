 
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Launch in incognito mode

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://v2.zenclass.in/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

