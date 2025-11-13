from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert login_page.is_success_message_displayed(), "Login success message not found"
