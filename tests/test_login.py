from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def test_success_login(setup):
    login = LoginPage(setup)

    login.input_username("validUser")
    login.input_password("validPassword")
    login.click_button_login()

    show = login.success()
    assert show

def test_failed_invalid_password(setup):
    login = LoginPage(setup)

    login.input_username("validUser")
    login.input_password("v@lidPassword")
    login.click_button_login()

    show = login.failed()
    assert show

def test_failed_invalid_username(setup):
    login = LoginPage(setup)

    login.input_username("validuser")
    login.input_password("validPassword")
    login.click_button_login()

    show = login.failed()
    assert show

def test_failed_invalid_username_and_password(setup):
    login = LoginPage(setup)

    login.input_username("validuser")
    login.input_password("VALIDPASSWORD")
    login.click_button_login()

    show = login.failed()
    assert show

def test_failed_blank_password(setup):
    login = LoginPage(setup)

    login.input_username("validUser")
    login.click_button_login()

    show = login.failed()
    assert show

def test_failed_blank_username(setup):
    login = LoginPage(setup)

    login.input_password("validPassword")
    login.click_button_login()

    show = login.failed()
    assert show

def test_failed_blank(setup):
    login = LoginPage(setup)

    login.click_button_login()

    show = login.failed()
    assert show

