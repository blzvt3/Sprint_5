from data import Data
from locators import Locators
from generator import Generator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestSignup:
    def test_signup(self, driver):
        login_account_button = driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SIGNUP_HYPERLINK))

        signup_hyperlink = driver.find_element(*Locators.SIGNUP_HYPERLINK)
        signup_hyperlink.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SIGNUP_BUTTON))

        name_input = driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(Data.NAME)

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(Generator.generate_email())

        invalid_password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        invalid_password_input.send_keys(Generator.generate_invalid_password())
        invalid_signup = driver.find_element(*Locators.SIGNUP_BUTTON)
        invalid_signup.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PASSWORD_ERROR))

        valid_password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        valid_password_input.clear()
        valid_password_input.send_keys(Generator.generate_valid_password())
        valid_signup = driver.find_element(*Locators.SIGNUP_BUTTON)
        valid_signup.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))