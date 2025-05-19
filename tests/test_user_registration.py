from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from tests.parameters import test_password, incorrect_login
from tests.helpers import create_user
from locators import EMAIL_INPUT, PASSWORD_INPUT, REPEAT_PASSWORD_INPUT, CREATE_ACCOUNT_BUTTON, ACCOUNT_PHOTO, ACCOUNT_NAME, HIGHLIGHT_RED_ERRORS, ERROR


class TestRegistration:

    def test_user_registration_positive_scenario(self, driver_for_registration, random_email):
        driver_for_registration.find_element(*EMAIL_INPUT).send_keys(random_email)
        driver_for_registration.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver_for_registration.find_element(*REPEAT_PASSWORD_INPUT).send_keys(test_password)
        driver_for_registration.find_element(*CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_for_registration, 3).until(visibility_of_element_located((ACCOUNT_PHOTO)))
        assert driver_for_registration.find_element(*ACCOUNT_PHOTO).is_displayed()
        assert driver_for_registration.find_element(*ACCOUNT_NAME).is_displayed()


    def test_user_registration_incorrect_email(self, driver_for_registration):
        driver_for_registration.find_element(*EMAIL_INPUT).send_keys(incorrect_login)
        driver_for_registration.find_element(*CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_for_registration, 3).until(visibility_of_element_located((HIGHLIGHT_RED_ERRORS)))
        assert len(driver_for_registration.find_elements(*HIGHLIGHT_RED_ERRORS)) == 3
        assert driver_for_registration.find_element(*ERROR).is_displayed()


    def test_registration_existing_user(self,driver_for_registration, random_email):
        create_user(random_email)
        driver_for_registration.find_element(*EMAIL_INPUT).send_keys(random_email)
        driver_for_registration.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver_for_registration.find_element(*REPEAT_PASSWORD_INPUT).send_keys(test_password)
        driver_for_registration.find_element(*CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_for_registration, 3).until(visibility_of_element_located((HIGHLIGHT_RED_ERRORS)))
        assert len(driver_for_registration.find_elements(*HIGHLIGHT_RED_ERRORS)) == 3
        assert driver_for_registration.find_element(*ERROR).is_displayed()
