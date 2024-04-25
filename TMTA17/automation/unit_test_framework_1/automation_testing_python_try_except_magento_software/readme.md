# Test Framework - Automation Testing

## 1. Test Setup

### a) Install libraries
- pip install selenium
- pip install html-testRunner
- pip install seleniumbase

### b) Define test structure
- test_files (starting with test_)
- test suite (in the file called suite)

## 2. Libraries used:
- from unittest import TestCase
- from selenium.webdriver import Keys
- from selenium.webdriver.common.by import By
- from selenium.webdriver.support.select import Select
- from seleniumbase import Driver
- import HtmlTestRunner

## 3. Running the tests
- can be done by running the entire test suite, which will start the running
  of all the tests in the classes that were called in the test suite
- the running will be done based on a runner defined as an instance of class HTMLTestRunner

## 4. Test results
Through running the test suites we have obtained a number of three executed tests, two passed and two failed.

The tests that were passed were the following:
- test_sorting_by_price_descending
- test_check_sign_in_not_possible_when_user_and_pass_empty

The test that was failed was _test_check_search_results_
The test was failed because the title of the search results products was not always in correspondence to the search criteria
For testing purposes we can consider this as a correct result since the test was properly designed to validate that all the products have the search criteria in the title In real life, this might be an expected behaviour  because the search criteria might coincide with some product parameters, even if the search criteria is not in the title, in which case we would have to clarify the expected  behaviour with a business analyst

Below the test execution report can be found:

![image](https://github.com/itfactorycourses/Grupe_TA/assets/143410937/608b471d-9bd9-4892-919c-be08c66364c5)


## 5. Performance indicators:
In order to make the code more efficient the most suitable selectors were found in order to be able to identify the web elements in consequence, id or link text selectors were used as means of identification, except when the specifics of a web element required otherwise

Also, CSS selector was preferred to XPATH selector since it is usually faster. Nevertheless, whenever we needed to search for an element that was not able to be found with CSS selector XPATH selector was used

In order to make the execution more efficient we have used elements like break in order to avoid unnecessary loop execution and also tried to make variable assignment only when needed, reducing variable reassignment to a minimum.

Also, the usage of a sleep instruction was reduced as much as possible and as a general trend the waits are to be preferred to the sleep instruction




