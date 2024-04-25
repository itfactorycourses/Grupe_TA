from behave import *

@then('I should have at least "{number_of_results}" results returned')
def step_impl(context,number_of_results):
		context.search_result_page.check_number_of_search_results(number_of_results)

@then('The search results should have "{search_value}" in the product title')
def step_impl(context,search_value):
		context.search_result_page.check_that_results_are_correct(search_value)

