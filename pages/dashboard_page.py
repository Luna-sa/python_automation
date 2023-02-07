from pages.base_page import BasePage


class Dashboard(BasePage):
    pass
    main_page_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_xpath = "//button[text()='Players']"
    lang_piker_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    sign_out_xpath = "//button[text()='Sign out']"
    add_player_xpath = "//a[contains(@href, 'en/players/add')]/button"
    dev_team_contact_xpath = "//button[text()='Dev team contact']"
    last_created_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
    last_created_match_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
    last_updated_report_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    title_dashboard_xpath = '//*[@id="__next"]//h6'

    expected_title_dashboard = "Scouts Panel"

    def check_page_title(self):
        print('Page title ' + self.get_element_text(self.title_dashboard_xpath))
        print('Expected title ' + self.expected_title_dashboard)
        assert self.get_element_text(self.title_dashboard_xpath) == self.expected_title_dashboard
