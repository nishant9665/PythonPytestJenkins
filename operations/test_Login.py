import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure



@pytest.fixture
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(30)
    driver.get("https://practicetestautomation.com/")

    yield
    driver.quit()

@allure.description("Login with valid credentials")
@allure.severity(severity_level="CRITICAL")
def test_Login(test_setup):
    driver.find_element(By.XPATH,"//li//a[contains(text(),'Practice')]").click()
    driver.find_element(By.XPATH,"//p//a[contains(text(),'Test Login Page')]").click()
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    loginSuccessMsg = driver.find_element(By.XPATH,"//div/h1[@class='post-title']")
    assert "Logged" in  loginSuccessMsg.text
    driver.find_element(By.XPATH, "//div//a[contains(text(),'Log out')]").click()

@allure.description("Login with invalid 'USER' credentials")
@allure.severity(severity_level="NORMAL")
def test_InvalidUserLogin(test_setup):
    driver.find_element(By.XPATH,"//li//a[contains(text(),'Practice')]").click()
    driver.find_element(By.XPATH,"//p//a[contains(text(),'Test Login Page')]").click()
    driver.find_element(By.ID, "username").send_keys("student123")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    userIDInvalid = driver.find_element(By.ID,"error")
    print("This is invalid user id text : ", userIDInvalid.text)
    assert "username" in  userIDInvalid.text
    if "pass"=="passx":
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(), name="Invalid Credentials",
                      attachment_type=allure.attachment_type.PNG)

@allure.description("Login with invalid 'PASSWORD' credentials")
@allure.severity(severity_level="NORMAL")
def test_InvalidPasswordLogin(test_setup):
    driver.find_element(By.XPATH,"//li//a[contains(text(),'Practice')]").click()
    driver.find_element(By.XPATH,"//p//a[contains(text(),'Test Login Page')]").click()
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password1234")
    driver.find_element(By.ID, "submit").click()
    passwordIDInvalid = driver.find_element(By.ID,"error")
    assert "password" in  passwordIDInvalid.text




