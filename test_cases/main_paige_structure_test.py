import time

from selenium.webdriver.common.by import By

from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from test_cases.set_up_test_cases import SetUpTestCases


class MainPageStructureTest(SetUpTestCases):

    def test_players_count_has_right_color(self):
        user_login = LoginPage(self.driver)
        user_login.login_to_the_system()
        assert self.driver.find_element(By.XPATH, Dashboard.players_count_xpath).is_displayed()
