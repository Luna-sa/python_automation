import time

from pages.dashboard_page import Dashboard
from test_cases.set_up_test_cases import SetUpTestCases
from pages.login_page import LoginPage


class TestLocalization(SetUpTestCases):

    def test_change_language_picker(self):
        user_login = LoginPage(self.driver)
        user_login.login_to_the_system()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_element(dashboard_page.lang_piker_xpath)
        # not sure how to properly wait for that action
        time.sleep(1)
        assert self.driver.current_url == "https://scouts-test.futbolkolektyw.pl/pl"
        assert dashboard_page.get_element_text(dashboard_page.main_page_xpath) == "Strona główna"
