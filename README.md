# Selenium Automation Framework

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-orange)](https://www.selenium.dev/)
[![GitHub Actions](https://github.com/RobertoEL/selenium-automation-framework/workflows/Selenium%20Tests/badge.svg)](https://github.com/RobertoEL/selenium-automation-framework/actions)

---

## Table of Contents

- [Description](#description)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running Tests Locally](#running-tests-locally)
- [Reports](#reports)
- [CI/CD Integration](#cicd-integration)
- [Contributing](#contributing)

---

## Description

This repository contains a **Selenium Automation Framework** for web application testing. It is designed with **Page Object Model (POM)**, **Pytest**, **logging**, **screenshots on failure**, and **config-driven setup**.  
The framework currently targets [The Internet](https://the-internet.herokuapp.com/) demo website, including login and checkbox functionality.  

It also includes CI/CD automation using **GitHub Actions**, generating **HTML** and **Allure** reports for test execution results.

---

## Tech Stack

- **Programming Language:** Python 3.10  
- **Test Automation:** Selenium WebDriver, Pytest  
- **Data Handling / Config:** JSON for test configuration  
- **Reporting:** pytest-html, Allure  
- **Browser Drivers:** Chrome (primary), Firefox, Edge  
- **Utilities:** Logging, Screenshots, Driver Factory  
- **CI/CD:** GitHub Actions  

---

## Project Structure

selenium-automation-framework/  
│  
├── config/  
│ └── config.json # Central configuration  
├── pages/  
│ ├── base_page.py # Base Page class  
│ ├── login_page.py # Login page object  
│ └── checkbox_page.py # Checkbox page object  
├── tests/  
│ ├── conftest.py # Pytest fixtures and setup  
│ ├── test_login.py  
│ └── test_checkboxes.py  
├── utils/  
│ ├── driver_factory.py # Browser setup  
│ ├── logger.py # Logging utility  
│ └── screenshot.py # Screenshot utility  
├── reports/  
│ ├── test_report.html # HTML test report  
│ └── allure-report/ # Allure report folder  
├── .github/workflows/  
│ └── selenium-tests.yml # GitHub Actions workflow  
├── requirements.txt  
└── README.md  

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/selenium-automation-framework.git
cd selenium-automation-framework
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Running Tests Locally

1. Run all tests and generate an **HTML report**:

```bash
pytest --html=reports/test_report.html --self-contained-html
```

2. Open the HTML report in your browser:

```bash
open reports/test_report.html   # macOS/Linux
start reports\test_report.html  # Windows
```

3. Screenshots for failed tests will be automatically saved in:

```bash
reports/screenshots/
```

## Reports

- **HTML Report:** `reports/test_report.html`  
- **Allure Report:** `reports/allure-report/index.html`  
  Generate manually (if needed):

```bash
pytest --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

## CI/CD Integration

- GitHub Actions workflow: `.github/workflows/selenium-tests.yml`  
- Triggered automatically on `push` or `pull_request` to `main`  
- Generates **HTML** and **Allure** reports and uploads as artifacts  

**Workflow Badge:**  
![GitHub Actions](https://github.com/RobertoEL/selenium-automation-framework/workflows/Selenium%20Tests/badge.svg)

---

## Contributing

1. Fork the repository  
2. Create a feature branch: `git checkout -b feature/my-feature`  
3. Commit your changes: `git commit -m "Add feature"`  
4. Push to the branch: `git push origin feature/my-feature`  
5. Open a pull request  

---

## Notes

- Update `<YOUR_GITHUB_USERNAME>` in badges and clone URL to your GitHub username.  
- Browser versions and drivers must match locally and on CI.
