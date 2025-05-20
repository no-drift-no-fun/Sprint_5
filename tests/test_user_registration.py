from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from tests.parameters import test_password, incorrect_login, test_login
from tests.helpers import random_email
from locators import ENTER_AND_REGISTRATION_BUTTON, NO_ACCOUNT_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, REPEAT_PASSWORD_INPUT, CREATE_ACCOUNT_BUTTON, ACCOUNT_PHOTO, ACCOUNT_NAME, HIGHLIGHT_RED_ERRORS, ERROR


class TestRegistration:

    def test_user_registration_positive_scenario(self, driver):
        email = random_email()
        driver.find_element(*ENTER_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*REPEAT_PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(visibility_of_element_located((ACCOUNT_PHOTO)))
        assert driver.find_element(*ACCOUNT_PHOTO).is_displayed()
        assert driver.find_element(*ACCOUNT_NAME).is_displayed()


    def test_user_registration_incorrect_email(self, driver):
        driver.find_element(*ENTER_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(incorrect_login)
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(visibility_of_element_located((HIGHLIGHT_RED_ERRORS)))
        assert len(driver.find_elements(*HIGHLIGHT_RED_ERRORS)) == 3
        assert driver.find_element(*ERROR).is_displayed()


    def test_registration_existing_user(self, driver):
        driver.find_element(*ENTER_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(visibility_of_element_located((EMAIL_INPUT)))
        driver.find_element(*EMAIL_INPUT).send_keys(test_login)
        driver.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*REPEAT_PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(visibility_of_element_located((HIGHLIGHT_RED_ERRORS)))
        assert len(driver.find_elements(*HIGHLIGHT_RED_ERRORS)) == 3
        assert driver.find_element(*ERROR).is_displayed()
