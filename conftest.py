import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://andreascandle.github.io/samir_test/qa_test_samir.html")
    yield driver
    driver.quit()