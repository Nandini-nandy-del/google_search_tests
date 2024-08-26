from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    request.cls.driver = driver
    yield
    driver.quit()

