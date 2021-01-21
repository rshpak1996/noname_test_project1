from selenium import webdriver
import pytest
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # код виконається після завершення тесту
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()