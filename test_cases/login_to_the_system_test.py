import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from test_cases.set_up_test_cases import SetUpTestCases


class TestLoginPage(SetUpTestCases):

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user10@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_element("//*[@id='__next']/form/div/div[2]/button/span[1]")
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_page_title()

    def test_logout_from_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.login_to_the_system()
        user_login.click_on_the_element(Dashboard.sign_out_xpath)
        # wait = WebDriverWait(self.driver, 2)
        # wait.until(EC.presence_of_element_located(By.XPATH("//button/span[text()='Sign in']")))
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, "//button/span[text()='Sign in']").is_displayed()
