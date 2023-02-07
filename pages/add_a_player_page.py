from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    add_player_page_title_xpath = '//form//span[contains(@class, "MuiCardHeader-title")]'
    expected_title_add_a_player = 'Add player'
    add_player_form_name_xpath = '//input[@name="name"]'
    add_player_form_surname_xpath = '//input[@name="surname"]'
    add_player_form_age_xpath = '//input[@name="age"]'
    add_player_form_main_position_xpath = '//input[@name="mainPosition"]'
    submit_button_xpath = "//button[@type='submit']"
    surname_validation_error_xpath = "//input[@name='surname']/../following-sibling::p"

    def check_page_title(self):
        print('Page title ' + self.get_element_text(self.add_player_page_title_xpath))
        print('Expected title ' + self.expected_title_add_a_player)
        assert self.get_element_text(self.add_player_page_title_xpath) == self.expected_title_add_a_player

    def fill_add_player_form_mandatory_fields(self, name, surname, age, main_position):
        self.field_send_keys(self.add_player_form_name_xpath, name)
        self.field_send_keys(self.add_player_form_surname_xpath, surname)
        self.field_send_keys(self.add_player_form_age_xpath, age)
        self.field_send_keys(self.add_player_form_main_position_xpath, main_position)
