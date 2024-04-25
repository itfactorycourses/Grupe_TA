from behave import *

@when('I click on the Create an Account link')
def step_impl(context):
    context.create_account_page.click_account_link()

@when('I insert "{first_name}" on the first name field')
def step_impl(context, first_name):
    context.create_account_page.insert_first_name_name(first_name)

@when('I insert "{last_name}" on the last name field')
def step_impl(context, last_name):
    context.create_account_page.insert_last_name_name(last_name)

@when('I insert "{email}" on the email field')
def step_impl(context, email):
    context.create_account_page.insert_create_account_email(email)

@when('I insert "{password}" on the password field')
def step_impl(context, password):
    context.create_account_page.insert_create_account_password(password)

@when('I insert "{confirm_password}" on the confirm password field')
def step_impl(context, confirm_password):
    context.create_account_page.insert_confirm_password(confirm_password)

@when('I click on the Create Account button')
def step_impl(context):
    context.create_account_page.click_account_button()
