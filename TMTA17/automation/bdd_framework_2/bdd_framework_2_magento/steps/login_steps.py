from behave import *


@when('I insert email as "{email_value}"')
def step_impl(context, email_value):
    context.login_page.insert_email(email_value)


@when('I insert password as "{password_value}"')
def step_impl(context, password_value):
    context.login_page.insert_password(password_value)


@when('I click on the sign in button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I receive an error message "{error_message}"')
def step_impl(context, error_message):
    context.login_page.check_email_error_message(error_message)
