import time

from pages.add_a_player_page import AddPlayerPage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from test_cases.default_test_case import SetUpTestCases


class TestLoginPage(SetUpTestCases):

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user10@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_element("//*[@id='__next']/form/div/div[2]/button/span[1]")
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        user_login.click_on_the_element(dashboard_page.add_player_xpath)
        time.sleep(3)
        add_a_player_page = AddPlayerPage(self.driver)
        add_a_player_page.check_page_title()


