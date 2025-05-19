from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from tests.parameters import test_password
from tests.helpers import create_user
from locators import EMAIL_INPUT, PASSWORD_INPUT, ENTER_BUTTON, EXIT_BUTTON, ENTER_AND_REGISTRATION_BUTTON, ACCOUNT_PHOTO, ACCOUNT_NAME


class TestLoginLogout:

    def test_login_positive_scenario(self, driver_for_login, random_email):
        create_user(random_email)
        driver_for_login.find_element(*EMAIL_INPUT).send_keys(random_email)
        driver_for_login.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver_for_login.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver_for_login, 5).until(visibility_of_element_located((ACCOUNT_PHOTO)))
        assert driver_for_login.find_element(*ACCOUNT_PHOTO).is_displayed()
        assert driver_for_login.find_element(*ACCOUNT_NAME).is_displayed()

    def test_logout_positive_scenario(self, driver_for_login, random_email):
        create_user(random_email)
        driver_for_login.find_element(*EMAIL_INPUT).send_keys(random_email)
        driver_for_login.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver_for_login.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver_for_login, 5).until(visibility_of_element_located((ACCOUNT_PHOTO)))
        driver_for_login.find_element(*EXIT_BUTTON).click()
        WebDriverWait(driver_for_login, 5).until(visibility_of_element_located((ENTER_AND_REGISTRATION_BUTTON)))
        assert len(driver_for_login.find_elements(*ACCOUNT_PHOTO)) == 0
        assert len(driver_for_login.find_elements(*ACCOUNT_NAME)) == 0
        assert driver_for_login.find_element(*ENTER_AND_REGISTRATION_BUTTON).is_displayed()




