from data import Data
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructor:
    def test_constructor(self, driver):
        login_account_button = driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON)
        login_account_button.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(Data.EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(Data.PASSWORD)

        login_button = driver.find_element(*Locators.LOGIN_BUTTON)
        login_button.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        profile_button = driver.find_element(*Locators.PROFILE_BUTTON)
        profile_button.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_EMAIL))

        logo_button = driver.find_element(*Locators.LOGO_BUTTON)
        logo_button.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        profile_button = driver.find_element(*Locators.PROFILE_BUTTON)
        profile_button.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_EMAIL))

        constructor_button = driver.find_element(*Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))

        sauces_button = driver.find_element(*Locators.SAUCES_BUTTON)
        sauces_button.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SAUCES_TITLE))

        fillings_button = driver.find_element(*Locators.FILLINGS_BUTTON)
        fillings_button.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.FILLINGS_TITLE))

        buns_button = driver.find_element(*Locators.BUNS_BUTTON)
        buns_button.click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUNS_TITLE))