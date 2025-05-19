import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
from locators import ENTER_AND_REGISTRATION_BUTTON, NO_ACCOUNT_BUTTON


@pytest.fixture
def driver_for_registration():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    driver.find_element(*ENTER_AND_REGISTRATION_BUTTON).click()
    driver.find_element(*NO_ACCOUNT_BUTTON).click()
    yield driver
    driver.quit()

@pytest.fixture
def driver_for_login():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    driver.find_element(*ENTER_AND_REGISTRATION_BUTTON).click()
    yield driver
    driver.quit()

@pytest.fixture
def driver_for_announcement():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def random_email():
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for _ in range(10))
    domain = ''.join(random.choice(letters) for _ in range(5))
    return f"{username}@{domain}.com"