from behave import *

@then('The account should be created and the user should be direct to homepage')
def step_impl(context):
    context.logged_in_user.check_account_created()