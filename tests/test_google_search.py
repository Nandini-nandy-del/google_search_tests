import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test1:

    def test_google_search(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element(By.NAME, "q").send_keys("recent rape cases happening in India")
        res = self.driver.find_elements(By.CLASS_NAME, "G43f7e")
        assert len(res) > 0, "No search suggestions were found."

