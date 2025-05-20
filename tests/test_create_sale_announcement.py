from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.parameters import test_password, name, description, price, test_login
from locators import ENTER_AND_REGISTRATION_BUTTON, CREATE_ANNOUNCEMENT_BUTTON, MODAL_WINDOW, EMAIL_INPUT, PASSWORD_INPUT, ENTER_BUTTON, ACCOUNT_PHOTO, TITLE, CATEGORY_DROPDOWN, CATEGORY, PRICE, CITY_DROPDOWN, CITY, CONDITION, DESCRIPTION, PUBLISH_BUTTON, PROFILE_BUTTON, ANNOUNCEMENT_IN_PROFILE

class TestCreateAnnouncement:

    def test_create_by_user_without_registration(self, driver):
        driver.find_element(*CREATE_ANNOUNCEMENT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MODAL_WINDOW))
        assert "Чтобы разместить объявление, авторизуйтесь" in driver.find_element(*MODAL_WINDOW).text

    def test_create_announcement_positive_scenario(self, driver):
        driver.find_element(*ENTER_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(test_login)
        driver.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ACCOUNT_PHOTO))
        driver.find_element(*CREATE_ANNOUNCEMENT_BUTTON).click()
        driver.find_element(*TITLE).send_keys(name)
        driver.find_element(*CATEGORY_DROPDOWN).click()
        category = driver.find_element(*CATEGORY)
        driver.execute_script("arguments[0].scrollIntoView();", category)
        driver.find_element(*CATEGORY).click()
        driver.find_element(*CITY_DROPDOWN).click()
        city = driver.find_element(*CITY)
        driver.execute_script("arguments[0].scrollIntoView();", city)
        driver.find_element(*CITY).click()
        driver.find_element(*CONDITION).click()
        driver.find_element(*DESCRIPTION).send_keys(description)
        driver.find_element(*PRICE).send_keys(price)
        driver.find_element(*PUBLISH_BUTTON).click()
        driver.find_element(*PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ANNOUNCEMENT_IN_PROFILE))
        assert name in driver.find_element(*ANNOUNCEMENT_IN_PROFILE).text










