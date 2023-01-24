from pages.base_page import BasePage


class Dashboard(BasePage):
    pass
    main_page_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_xpath = "//button[text()='Players']"
    lang_piker_xpath = "//*[@id=['__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_xpath = "//button[text()='Sign out']"
    add_player_xpath = "//button[text()='Add player']"
    dev_team_contact_xpath = "//button[text()='Dev team contact']"
    last_created_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
    last_created_match_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
    last_updated_report_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"


