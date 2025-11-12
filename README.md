# 🧪 Selenium Automation Framework – The Internet (Herokuapp)

An end-to-end **web automation framework** built with **Python, Selenium, and pytest**, designed to automate functional tests for [The Internet](https://the-internet.herokuapp.com/) — a web application created by Elemental Selenium for QA practice.

This project demonstrates **Page Object Model (POM)** architecture, **data-driven testing**, and **automated reporting**, providing a clean, scalable example of professional QA automation design.

---

## 🚀 Features

- ✅ Page Object Model (POM) architecture for scalable, maintainable test cases  
- 🧠 Covers multiple scenarios: Login, Dropdowns, Checkboxes, File Uploads, Alerts, and Dynamic Elements  
- ⚙️ Configurable browser options (Chrome, Firefox, Edge)  
- 📊 HTML and Allure test report generation  
- 🧩 Data-driven test examples using JSON or CSV  
- 🔁 CI/CD-ready with GitHub Actions integration  
- 📸 Automatic screenshot capture on test failure  

---

## 🧱 Project Structure

selenium-automation-framework/  
│  
├── config/  
│   ├── config.json            # Base URL, browser type, timeouts  
│  
├── pages/  
│   ├── base_page.py           # Common WebDriver actions  
│   ├── login_page.py          # Login page elements and methods  
│   ├── checkbox_page.py       # Checkbox interaction page  
│   ├── dropdown_page.py       # Dropdown selection page  
│   ├── upload_page.py         # File upload page  
│  
├── tests/  
│   ├── test_login.py          # Valid/invalid login tests  
│   ├── test_checkboxes.py     # Checkbox selection tests  
│   ├── test_dropdown.py       # Dropdown tests  
│   ├── test_upload.py         # File upload test  
│  
├── utils/  
│   ├── driver_factory.py      # WebDriver initialization and teardown  
│   ├── logger.py              # Logging configuration  
│   ├── screenshot.py          # Screenshot on failure  
│  
├── reports/  
│   ├── test_report.html       # Pytest HTML report output  
│  
├── requirements.txt           # Python dependencies  
└── README.md                  # Project documentation  

---

## 🧰 Tech Stack

Language: Python 3.10+  
Libraries: Selenium, pytest, pytest-html, allure-pytest  
Tools: Git, VS Code, ChromeDriver, GitHub Actions  
Design Pattern: Page Object Model (POM) + Data-driven testing

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
git clone https://github.com/RobertoEL/Selenium-Automation-Framework.git  
cd Selenium-Automation-Framework

### 2️⃣ Create a Virtual Environment
python -m venv venv  
source venv/bin/activate     # Mac/Linux  
venv\Scripts\activate        # Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Run Tests
pytest --html=reports/test_report.html

To run with Allure reporting:  
pytest --alluredir=reports/allure-results  
allure serve reports/allure-results

---

## 🧪 Example Test Case

### Test: Login Page (Valid Credentials)
from pages.login_page import LoginPage

def test_valid_login(browser):  
    login_page = LoginPage(browser)  
    login_page.open()  
    login_page.login("tomsmith", "SuperSecretPassword!")  
    assert login_page.is_success_message_displayed(), "Login success message not found"  

### Test: Checkbox Interaction
from pages.checkbox_page import CheckboxPage

def test_checkbox_selection(browser):  
    checkbox_page = CheckboxPage(browser)  
    checkbox_page.open()  
    checkbox_page.select_checkbox(1)  
    assert checkbox_page.is_checkbox_selected(1)

---

## 📈 CI/CD Integration

This framework integrates easily with GitHub Actions or Jenkins.  
Example GitHub Actions workflow (.github/workflows/selenium-tests.yml):

name: Selenium Tests

on: [push, pull_request]

jobs:  
  test:  
    runs-on: ubuntu-latest  
    steps:  
      - uses: actions/checkout@v3  
      - name: Set up Python  
        uses: actions/setup-python@v4  
        with:  
          python-version: '3.10'  
      - name: Install dependencies  
        run: pip install -r requirements.txt  
      - name: Run Selenium tests  
        run: pytest --html=reports/test_report.html  

---

## 🧩 Future Enhancements

- Parallel test execution (pytest-xdist)
- Visual regression testing with image comparison
- Add API layer testing (Requests + pytest)
- Power BI integration for test metrics visualization

---

## 👤 Author

[Roberto Esparza]
Software QA Engineer | Python Developer | Data Enthusiast  
📫 [phd.roberto.esparza@gmail.com](mailto:phd.roberto.esparza@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/robertoesparzalepe/) • [Portfolio / Website](https://github.com/RobertoEL)

---

⭐ "Automation is the bridge between precision, performance, and confidence in every release."
