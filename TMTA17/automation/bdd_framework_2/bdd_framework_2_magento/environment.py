from pages.create_account_page import CreateAccountPage
from pages.home_page import Home_page
from pages.home_page_logged_in_user_page import HomePageLoggedInUserPage
from pages.login_page import LoginPage
from pages.search_results_page import Search_Results_Page
from pages.create_account_page import CreateAccountPage


def before_all(context):
    # context este ca o cutiuta
    # care va stoca numele
    # tuturor obiectelor instantiate
    # din clasele de tip pages
    context.home_page = Home_page()
    context.search_result_page = Search_Results_Page()
    context.create_account_page = CreateAccountPage()
    context.logged_in_user = HomePageLoggedInUserPage()
    context.login_page = LoginPage()

def after_all(context):
    context.browser.close_browser()
