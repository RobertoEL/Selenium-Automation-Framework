import pytest
from utils.driver_factory import create_driver

@pytest.fixture
def browser():
    driver = create_driver("chrome")
    yield driver
    driver.quit()
