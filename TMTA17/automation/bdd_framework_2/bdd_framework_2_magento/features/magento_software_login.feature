Feature: We want to check the login functionality

    @T3
    Scenario Outline: Verify that when the user inserts invalid data into the login fields, then he is not able to login into the application
      Given I am on magento software testing homepage
      When I click on the sign in link
      When I insert email as "<email_value>"
      When I insert password as "<password_value>"
      When I click on the sign in button
      Then I receive an error message "<error_message>"
      Examples:
        | email_value            | password_value    | error_message                                                |
        | johndoe                | testpass          | Please enter a valid email address (Ex: johndoe@domain.com). |
        | johndoe@gmail.com      | testpass          | Email was not found in the database. Please try again        |
        | johndoesafg1@gmail.com | testpass          | Username or password is invalid. Please try again            |
        | johndoe@gmail.com      | testpassword1234% | Username or password is invalid. Please try again            |

      # johndoesafg1@gmail.com / testpassword1234%





