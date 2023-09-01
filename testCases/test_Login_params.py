from selenium.webdriver.common.by import By


class Test_CredKart_Login_params:

    def test_CredKart_Login_params_003(self, setup, getDataforLogin):

        self.driver =setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(getDataforLogin[0])
        self.driver.find_element(By.CSS_SELECTOR, "input[id = 'password']").send_keys(getDataforLogin[1])
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space() = 'CredKart']")
            print("Login TestCase is Passed")
            self.driver.save_screenshot(".\\ScreenShots\\"+getDataforLogin[0]+"_"+getDataforLogin[1]+"_"+"test_CredKart_Login_002.PNG")
            self.driver.close()
            assert True
        except:
            print("Login TestCase is Failed")
            self.driver.save_screenshot(".\\ScreenShots\\" + getDataforLogin[0] + "_" + getDataforLogin[1] + "_" + "test_CredKart_Login_002.PNG")
            self.driver.close()
            assert False
