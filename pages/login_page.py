from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button/span[1]"
    title_login_xpath = "//*[@text='Scouts Panel']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/login'

    # email = 'user10@getnada.com'
    # password = 'Test-1234'

    def type_in_email(self, email):
        print(email)
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def login_to_the_system(self):
        self.type_in_email('user10@getnada.com')
        self.type_in_password('Test-1234')
        self.click_on_the_element("//*[@id='__next']/form/div/div[2]/button/span[1]")

    # def click_on_the_element(self, sign_in_button_xpath, **kwargs):
    #     # self.field_send_keys(self.sign_in_button_xpath, signin).click()
    #     return self.driver.find_element(self.sign_in_button_xpath, sign_in_button_xpath).click()
