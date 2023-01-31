from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    add_player_page_title_xpath = '//form//span[contains(@class, "MuiCardHeader-title")]'
    expected_title_add_a_player = 'Add player'

    def check_page_title(self):
        print('Page title ' + self.get_element_text(self.add_player_page_title_xpath))
        print('Expected title ' + self.expected_title_add_a_player)
        assert self.get_element_text(self.add_player_page_title_xpath) == self.expected_title_add_a_player
