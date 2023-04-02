import random
import secrets
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from iris_app import create_app, config


# Used for the Flask routes tests and the Selenium tests
@pytest.fixture(scope="session")
def app():
    """Create a Flask app configured for testing"""
    app = create_app(config.TestConfig)

    yield app


# Used for the Flask route tests
@pytest.fixture(scope="function")
def test_client(app):
    """Create a Flask test test_client"""
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


# Used for the Selenium tests
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


# Data for any of the tests
@pytest.fixture(scope="module")
def form_data():
    """Data for a prediction.

    Uses: 7.0,3.2,4.7,1.4,versicolor
    """
    form_data_versicolor = {
        "sepal_length": 7.0,
        "sepal_width": 3.2,
        "petal_length": 4.7,
        "petal_width": 1.4,
    }
    yield form_data_versicolor


def generate_random_email():
    """Create random email addresses for testing with random domain names"""
    valid_chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    valid_doms = "abcdefghijklmnopqrstuvwxyz"
    login = ""
    server = ""
    dom = ""
    login_len = random.randint(4, 15)
    server_len = random.randint(3, 9)
    dom_len = random.randint(2, 3)
    for i in range(login_len):
        pos = random.randint(0, len(valid_chars) - 1)
        login = login + valid_chars[pos]
    if login[0].isnumeric():
        pos = random.randint(0, len(valid_chars) - 10)
        login = valid_chars[pos] + login
    for i in range(server_len):
        pos = random.randint(0, len(valid_doms) - 1)
        server = server + valid_doms[pos]
    for i in range(dom_len):
        pos = random.randint(0, len(valid_doms) - 1)
        dom = dom + valid_doms[pos]
    email = login + "@" + server + "." + dom
    return email


def generate_random_password():
    """Generate random password using secrets"""
    password_len = random.randint(6, 15)
    password = secrets.token_urlsafe(password_len)
    return password


@pytest.fixture(scope="function")
def random_email():
    """returns a random email as a fixture"""
    return generate_random_email()


@pytest.fixture(scope="function")
def random_password():
    """returns a random password as a fixture"""
    return generate_random_password()
