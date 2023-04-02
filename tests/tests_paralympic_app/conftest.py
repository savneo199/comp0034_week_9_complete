import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from paralympic_app import create_app, config
from paralympic_app.models import Region


# Used for Flask route tests and Selenium tests
@pytest.fixture(scope="session")
def app():
    """Create a Flask app configured for testing"""
    app = create_app(config.TestConfig)
    yield app


# Used for Flask route tests
@pytest.fixture(scope="function")
def test_client(app):
    """Create a Flask test client"""
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


# Used for Selenium tests
@pytest.fixture(scope="session")
def chrome_driver():
    """Selenium webdriver with options to support running in GitHub actions
    Note:
        For CI: `headless` not commented out
        For running on your computer: `headless` to be commented out
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


# Data for any tests
@pytest.fixture(scope="module")
def region_json():
    """Creates a new region JSON for tests"""
    reg_json = {
        "NOC": "NEW",
        "region": "New Region",
        "notes": "Some notes about the new region",
    }
    return reg_json


# Data for any tests
@pytest.fixture(scope="module")
def region():
    """Creates a new region object for tests"""
    new_region = Region(
        NOC="NEW", region="New Region", notes="Some notes about the new region"
    )
    return new_region
