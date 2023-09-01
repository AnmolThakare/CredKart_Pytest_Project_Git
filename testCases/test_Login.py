
from selenium.webdriver.common.by import By


class Test_CredKart_Login:

    def test_pageTitle_001(self, setup):

        self.driver = setup
        self.driver.get("https://automation.credence.in/")
        if self.driver.title == "CredKart":
            self.driver.save_screenshot(".\\ScreenShots\\test_pageTitle_001_Pass.PNG")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_pageTitle_001_Fail.PNG")
            self.driver.close()
            assert False


    def test_CredKart_Login_002(self, setup):

        self.driver =setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys("Anmol94@test.in")
        self.driver.find_element(By.CSS_SELECTOR, "input[id = 'password']").send_keys("Credence9@143")
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space() = 'CredKart']")
            print("Login TestCase is Passed")
            self.driver.save_screenshot(".\\ScreenShots\\test_CredKart_Login_002_Pass.PNG")
            self.driver.close()
            assert True
        except:
            print("Login TestCase is Failed")
            self.driver.save_screenshot(".\\ScreenShots\\test_CredKart_Login_002_Fail.PNG")
            self.driver.close()
            assert False
