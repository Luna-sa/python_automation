from pages.base_page import BasePage


class MatchForm(BasePage):
    pass
    my_team_xpath = "//button[name()='myTeam']"
    enemy_team_xpath = "//button[name()='enemyTeam']"
    my_team_score_xpath = "//button[name()='myTeamScore']"
    enemy_team_score_xpath = "//button[name()='enemyTeamScore']"
    date_xpath = "//button[name()='date']"
    match_at_home_radiobutton_xpath = "//button[name()='matchAtHome']"
    match_out_home_radiobutton_xpath = "//button[name()='matchOutHome']"
    tshirt_xpath = "//button[name()='tshirt']"
    league_xpath = "//button[name()='league']"
    timePlayed_xpath = "//button[name()='timePlayed']"
    number_xpath = "//button[name()='number']"
    web_match_xpath = "//button[name()='webMatch']"
    general_xpath = "//button[name()='general']"
    rating_xpath = "//button[name()='rating']"
    submit_button_xpath = "//button[type()='submit']"
    clear_button_xpath = "//button[name()='Clear']"
