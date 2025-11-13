from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxPage(BasePage):
    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def open(self):
        self.open_url(self.URL)

    def select_checkbox(self, index=0):
        checkbox = self.find_element((By.CSS_SELECTOR, f"input[type='checkbox']:nth-child({index+1})"))
        if not checkbox.is_selected():
            checkbox.click()

    def is_checkbox_selected(self, index=0):
        checkbox = self.find_element((By.CSS_SELECTOR, f"input[type='checkbox']:nth-child({index+1})"))
        return checkbox.is_selected()
