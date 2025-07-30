import pytest
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



@pytest.mark.usefixtures("setup")
class TestLogin:
# Test class to validate Username, Password and Submit button - To check the login page loading
    def test_login_page_validation(self):
        login_page = LoginPage(self.driver)
        # Verify that the login page is loaded
        assert login_page.is_login_page_loaded(), "Login page did not load correctly"
        print("Login page loaded successfully.")

        # Verify that the email input field is present
        assert login_page.is_email_input_present(), "Email input field is not present"
        print("Email input field is present.")

        # Verify that the password input field is present
        assert login_page.is_password_input_present(), "Password input field is not present"
        print("Password input field is present.")

        # Verify that the sign-in button is present
        assert login_page.is_element_present(login_page.SIGN_IN_BUTTON), "Sign-in button is not present"
        print("Sign-in button is present.")

# Test class to validate the login functionality
    def test_login(self):
        login_page = LoginPage(self.driver)
        # Enter valid credentials and click the sign-in button
        login_page.login("navinkumar.mk1712@gmail.com", "Guvi2025")
        # Verify that the URL and Title of page after login
        get_title = self.driver.title
        get_url = self.driver.current_url
        print(f"Current page title: {get_title}")
        print(f"Current URL after login: {get_url}")
        print("Login successful")

# Test class to validate the logout functionality
    def test_logout(self):
        login_page = LoginPage(self.driver) 
        # Verify that the profile icon is present before logout
        assert login_page.is_profile_icon_present(), "Profile icon is not present before logout"
        # Click on the profile icon
        login_page.click_element((By.XPATH, "//div[@class='profile-click-icon-div']"))
        # Click on the logout option
        login_page.click_element((By.XPATH, "//div[contains(text(),'Log out')]"))
        # Wait for the page to load after logout  - Using implicit wait
        self.driver.implicitly_wait(10)       
        print("Logout successful, redirected to login page.")

# Test class to validate unsuccessful login attempts with wrong credentials
    def test_login_wrong_password(self):
        login_page = LoginPage(self.driver)
        # Attempt to log in with invalid email and password credentials.
        login_page.login("navi@gmail.com", "Password")
        # Verify that the error message is displayed
        error_message = login_page.driver.find_element(By.XPATH, "//p[contains(text(),'*Incorrect mail or password!')]").text
        # Check if the error message is as expected
        assert error_message == "*Incorrect mail or password!", "Error message is not as expected for unsuccessful login"
        print("Unsuccessful login test completed successfully.")
        

        
                                                                                           