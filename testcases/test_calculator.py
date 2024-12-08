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

@allure.description("Calculator add method")
@allure.severity(severity_level="CRITICAL")
def test_add(test_setup):

   num1 =20
   num2=10
   num3 =num1+num2
   assert num3==30

@allure.description("Calculator subtraction method")
@allure.severity(severity_level="NORMAL")
def test_sub(test_setup):
    num1 = 20
    num2 = 10
    num3 = num1 - num2
    assert num3 == 10
    if "pass"=="passx":
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(), name="Invalid Credentials",
                      attachment_type=allure.attachment_type.PNG)

@allure.description("Calculator multiplication method")
@allure.severity(severity_level="NORMAL")
def test_mul(test_setup):
    num1 = 20
    num2 = 10
    num3 = num1 * num2
    assert num3 == 201


@allure.description("Calculator division method")
@allure.severity(severity_level="NORMAL")
def test_div(test_setup):
    num1 = 20
    num2 = 10
    num3 = num1 / num2
    assert num3 == 21



