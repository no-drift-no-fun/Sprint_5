from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from tests.parameters import test_password, test_login
from locators import EMAIL_INPUT, PASSWORD_INPUT, ENTER_BUTTON, EXIT_BUTTON, ENTER_AND_REGISTRATION_BUTTON, ACCOUNT_PHOTO, ACCOUNT_NAME


class TestLoginLogout:

    def test_login_positive_scenario(self, driver):
        driver.find_element(*ENTER_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(test_login)
        driver.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(visibility_of_element_located((ACCOUNT_PHOTO)))
        assert driver.find_element(*ACCOUNT_PHOTO).is_displayed()
        assert driver.find_element(*ACCOUNT_NAME).is_displayed()

    def test_logout_positive_scenario(self, driver):
        driver.find_element(*ENTER_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(test_login)
        driver.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(visibility_of_element_located((ACCOUNT_PHOTO)))
        driver.find_element(*EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(visibility_of_element_located((ENTER_AND_REGISTRATION_BUTTON)))
        assert len(driver.find_elements(*ACCOUNT_PHOTO)) == 0
        assert len(driver.find_elements(*ACCOUNT_NAME)) == 0
        assert driver.find_element(*ENTER_AND_REGISTRATION_BUTTON).is_displayed()




