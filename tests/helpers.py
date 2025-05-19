from selenium import webdriver
from selenium.webdriver.common.by import By
from parameters import test_password
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


def create_user(random_email):
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    driver.find_element(By.XPATH, './/button[contains(text(), "Вход и регистрация")]').click()
    driver.find_element(By.XPATH, './/button[contains(text(), "Нет аккаунта")]').click()
    driver.find_element(By.XPATH, ".//input[@placeholder='Введите Email']").send_keys(random_email)
    driver.find_element(By.NAME, "password").send_keys(test_password)
    driver.find_element(By.NAME, "submitPassword").send_keys(test_password)
    driver.find_element(By.XPATH, './/button[contains(text(), "Создать аккаунт")]').click()
    WebDriverWait(driver, 3).until(visibility_of_element_located((By.CSS_SELECTOR, "svg.svgSmall")))
    driver.quit()

