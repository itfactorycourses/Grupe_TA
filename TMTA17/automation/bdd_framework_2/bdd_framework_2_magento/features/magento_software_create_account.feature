Feature: This feature will verify the behaviour of the create account functionality
            in order to ensure proper functionality


  @T2 @create_account
  Scenario: Verify that when the user inserts valid data into the input fields, then he will be able to create account
    Given I am on magento software testing homepage
    When I click on the Create an Account link
    When I insert "Daniela" on the first name field
    When I insert "Bodron" on the last name field
    When I insert "daniela.bodron@gmail.com" on the email field
    When I insert "wegh#@%$T^$%" on the password field
    When I insert "wegh#@%$T^$%" on the confirm password field
    When I click on the Create Account button
    Then The account should be created and the user should be direct to homepage


