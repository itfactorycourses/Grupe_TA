from behave import *

@when('I click on the JS Alert Button')
def step_impl(context):
    context.alerts_page.click_javascript_alert()

@when('I accept the alert')
def step_impl(context):
    context.alerts_page.accept_alert()

@then('I should see the text "{alert_text}"')
def step_impl(context, alert_text):
    context.alerts_page.check_alert_results_text(alert_text)

@when('I click on the JS Confirm Button')
def step_impl(context):
    context.alerts_page.click_js_confirm_alert()

@when('I cancel the alert')
def step_impl(context):
    context.alerts_page.cancel_alert()

@when('I click on the JS Prompt Button')
def step_impl(context):
    context.alerts_page.click_js_prompt_button()

@when('I insert text "{input_text}" into the alert prompt and I click ok')
def step_impl(context, input_text):
    context.alerts_page.insert_prompt_text(input_text)