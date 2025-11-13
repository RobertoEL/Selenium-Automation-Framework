from pages.checkbox_page import CheckboxPage

def test_checkbox_selection(browser):
    checkbox_page = CheckboxPage(browser)
    checkbox_page.open()
    checkbox_page.select_checkbox(0)
    assert checkbox_page.is_checkbox_selected(0)
