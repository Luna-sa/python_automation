import time

from pages.add_a_player_page import AddPlayerPage
from pages.dashboard_page import Dashboard
from pages.edit_player_page import EditPlayerPage
from pages.login_page import LoginPage
from test_cases.set_up_test_cases import SetUpTestCases


class TestAddPlayer(SetUpTestCases):

    def test_add_to_player_page(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user10@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_element("//*[@id='__next']/form/div/div[2]/button/span[1]")
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)
        user_login.click_on_the_element(dashboard_page.add_player_xpath)
        time.sleep(2)
        add_a_player_page = AddPlayerPage(self.driver)
        add_a_player_page.check_page_title()

    def test_add_player_to_database(self):
        user_login = LoginPage(self.driver)
        user_login.login_to_the_system()
        dashboard_page = Dashboard(self.driver)
        user_login.click_on_the_element(dashboard_page.add_player_xpath)
        time.sleep(1)
        add_a_player_page = AddPlayerPage(self.driver)
        expected_user_name = "Muse"
        expected_user_surname = "AI"
        add_a_player_page.fill_add_player_form_mandatory_fields(expected_user_name, expected_user_surname, "01.01.1990",
                                                                "45")
        add_a_player_page.click_on_the_element(add_a_player_page.submit_button_xpath)
        time.sleep(5)
        assert self.driver.current_url.__contains__("/edit")
        expected_title = "Edit player" + " " + expected_user_name + " " + expected_user_surname
        assert add_a_player_page.get_element_text(
            EditPlayerPage.edit_player_page_form_title_xpath) == expected_title

    def test_form_validation(self):
        user_login = LoginPage(self.driver)
        user_login.login_to_the_system()
        dashboard_page = Dashboard(self.driver)
        user_login.click_on_the_element(dashboard_page.add_player_xpath)
        time.sleep(1)
        add_a_player_page = AddPlayerPage(self.driver)
        add_a_player_page.field_send_keys(add_a_player_page.add_player_form_name_xpath, "Muse")
        add_a_player_page.click_on_the_element(add_a_player_page.submit_button_xpath)
        assert add_a_player_page.get_element_text(add_a_player_page.surname_validation_error_xpath) == 'Required'
