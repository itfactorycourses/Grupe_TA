from behave import *

@given('I am on the herokuapp homepage')
def step_impl(context):
    context.home_page.navigate_to_homepage()

@when('I click on the Java Script Alerts link')
def step_impl(context):
    context.home_page.click_javascript_alerts_link()
