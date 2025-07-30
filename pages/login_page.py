from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH,"//input[@id=':r0:' and @type = 'text']")
    PASSWORD_INPUT = (By.XPATH,"//input[@id=':r1:']")
    SIGN_IN_BUTTON = (By.XPATH,"//button[@class='primary-btn sign-in-pad']")
    PROFILE_ICON_BUTTON = (By.XPATH,"//div[@class='profile-click-icon-div']")
    LOGOUT_BUTTON = (By.XPATH,"//div[contains(text(),'Log out')]")
    

    def login(self, email, password):
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.SIGN_IN_BUTTON)
        self.driver.implicitly_wait(10)  # Wait for the page to load after login
    

    def is_login_button_present(self):
        return self.is_element_present(self.SIGN_IN_BUTTON)
    
    def is_login_page_loaded(self):
        # Check if the email input field is present
        email_present = self.is_email_input_present()
        # Check if the password input field is present
        password_present = self.is_password_input_present()
        # Check if the sign-in button is present
        sign_in_button_present = self.is_element_present(self.SIGN_IN_BUTTON)
        
        return email_present and password_present and sign_in_button_present
    
    def is_email_input_present(self):
        return self.is_element_present(self.EMAIL_INPUT)
    
    def is_password_input_present(self):
        return self.is_element_present(self.PASSWORD_INPUT)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def is_profile_icon_present(self):
        return self.is_element_present(self.PROFILE_ICON_BUTTON)
    
    def is_logout_button_present(self):
        return self.is_element_present(self.LOGOUT_BUTTON)
    
    def get_current_logout_url(self):
        return self.driver.current_url
    
    def logout(self):
        # Click on the profile icon
        self.click_element((By.XPATH, "//div[@class='profile-click-icon-div']"))
        # Click on the logout option
        self.click_element((By.XPATH, "//div[contains(text(),'Log out')]"))
        current_url = self.get_current_url()
        # Verify that the URL is correct after logout
        assert current_url == "https://v2.zenclass.in/login", "Logout failed or URL mismatch after logout"
        print("Logout successful, redirected to login page.")
        return current_url


