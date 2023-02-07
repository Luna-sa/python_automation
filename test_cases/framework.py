from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import os
import unittest
from selenium import webdriver

from test_cases.set_up_test_cases import SetUpTestCases
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(SetUpTestCases):

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
