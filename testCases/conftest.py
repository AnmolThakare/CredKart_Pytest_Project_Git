import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# add argument --browser
def pytest_addoption(parser):
    parser.addoption("--browser")


# passing the value to --browser
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# here we are passing actual value to --browser
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("headlessmode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://automation.credence.in")
    return driver

def pytest_metadata(metadata):
    # To Add
    metadata["class"] = "Credence"
    metadata["Batch"] = "CT#12"
    metadata["URL"] = "https://automation.credence.in"
    # To Remove
    metadata.pop("platform", None)


# How to edit summary in html report this is your today's task

# Use parameter when you have small amount of data set

@pytest.fixture(params=[
    ("Anmol94@test.in", "Credence9@143"),
    ("Anmol94@test.in1", "Credence9@143"),
    ("Anmol94@test.in", "Credence9@1432"),
    ("Anmol94@test.in1", "Credence9@1432")
])
def getDataforLogin(request):
    return request.param

# pytest -v --html=HTMLReports/myreport.html --alluredir="allure-results" -n=2 testCases\test_Login.py --browser chrome