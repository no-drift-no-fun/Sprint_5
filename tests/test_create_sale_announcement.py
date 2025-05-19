from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.parameters import test_password, name, description, price
from tests.helpers import create_user
from locators import CREATE_ANNOUNCEMENT_BUTTON, MODAL_WINDOW, EMAIL_INPUT, PASSWORD_INPUT, ENTER_BUTTON, ACCOUNT_PHOTO, TITLE, CATEGORY_DROPDOWN, CATEGORY, PRICE, CITY_DROPDOWN, CITY, CONDITION, DESCRIPTION, PUBLISH_BUTTON, PROFILE_BUTTON, ANNOUNCEMENT_IN_PROFILE

class TestCreateAnnouncement:

    def test_create_by_user_without_registration(self, driver_for_announcement):
        driver_for_announcement.find_element(*CREATE_ANNOUNCEMENT_BUTTON).click()
        WebDriverWait(driver_for_announcement, 5).until(EC.visibility_of_element_located(MODAL_WINDOW))
        assert "Чтобы разместить объявление, авторизуйтесь" in driver_for_announcement.find_element(*MODAL_WINDOW).text

    def test_create_announcement_positive_scenario(self, driver_for_login, random_email):
        create_user(random_email)
        driver_for_login.find_element(*EMAIL_INPUT).send_keys(random_email)
        driver_for_login.find_element(*PASSWORD_INPUT).send_keys(test_password)
        driver_for_login.find_element(*ENTER_BUTTON).click()
        WebDriverWait(driver_for_login, 5).until(EC.visibility_of_element_located(ACCOUNT_PHOTO))
        driver_for_login.find_element(*CREATE_ANNOUNCEMENT_BUTTON).click()
        driver_for_login.find_element(*TITLE).send_keys(name)
        driver_for_login.find_element(*CATEGORY_DROPDOWN).click()
        category = driver_for_login.find_element(*CATEGORY)
        driver_for_login.execute_script("arguments[0].scrollIntoView();", category)
        driver_for_login.find_element(*CATEGORY).click()
        driver_for_login.find_element(*CITY_DROPDOWN).click()
        city = driver_for_login.find_element(*CITY)
        driver_for_login.execute_script("arguments[0].scrollIntoView();", city)
        driver_for_login.find_element(*CITY).click()
        driver_for_login.find_element(*CONDITION).click()
        driver_for_login.find_element(*DESCRIPTION).send_keys(description)
        driver_for_login.find_element(*PRICE).send_keys(price)
        driver_for_login.find_element(*PUBLISH_BUTTON).click()
        WebDriverWait(driver_for_login, 5).until(EC.visibility_of_element_located(PROFILE_BUTTON))
        WebDriverWait(driver_for_login, 5).until(EC.element_to_be_clickable(PROFILE_BUTTON))
        driver_for_login.find_element(*PROFILE_BUTTON).click()
        WebDriverWait(driver_for_login, 5).until(EC.visibility_of_element_located(ANNOUNCEMENT_IN_PROFILE))
        assert name in driver_for_login.find_element(*ANNOUNCEMENT_IN_PROFILE).text










