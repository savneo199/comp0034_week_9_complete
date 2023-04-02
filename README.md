# Week 9 completed code

## Set-up

You will need to a Python environment e.g create and activate a venv.

Install the packages from requirements.txt.

Install the apps: `pip install -e .`

## Completed tests

The completed tests are in the [tests](/tests) directory.

Some fixtures for the Selenium tests differ by operating system. To address this, a few changes are made that differ from the tutorial instructions for running the apps:

1. The configuration for Flask is now handled with a Config class object which is an attribute passed to the create_app() function.
2. To avoid port conflict on port 5000 with two apps running in the tests, the method for assigning a port for the Iris app front end tests is a dynamic allocation.
3. There are two versions of the Selenium tests for windows and for macos. The mac tests will fail on Windows and vice-versa. Some fixtures have been moved from the conftest.py to within the test module and their scope changed from 'session' to 'module'.

    - Windows: `python -m pytest -v tests/tests_paralympic_app/ -W ignore::DeprecationWarning --ignore=tests/tests_paralympic_app/test_para_front_end_macos.py`

    - MacOS: `python -m pytest -v tests/tests_paralympic_app/ -W ignore::DeprecationWarning --ignore=tests/tests_paralympic_app/test_para_front_end_windows.py`

    -Windows : `python -m pytest -v tests/tests_iris_app/ -W ignore::DeprecationWarning --ignore=tests/tests_iris_app/test_iris_front_end_macos.py`

    -macOS : `python -m pytest -v tests/tests_iris_app/ -W ignore::DeprecationWarning --ignore=tests/tests_iris_app/test_iris_front_end_windows.py`

The `-W ignore::DeprecationWarning` flag ignores package deprecation warnings. This is done to reduce the amount of text reported from the tests which hopefully makes it a little easier for you to see the errors that are specific to the test code. You can ommit this if you want to see all the warnings.
