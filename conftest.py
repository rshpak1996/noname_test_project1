from selenium import webdriver
import pytest
import time

def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    time.sleep(3)
    print("'\nquit browser...")
    browser.quit()