# Created by lenovo at 12/30/2025
Feature: Target Sign In tests

  Scenario: User can navigate to Sign In
    Given Open Target main page
    When Click "Account" button
    And From right side navigation menu, click "Sign In" button
    Then Verify Sign In form opened

  Scenario: User can open and close Privacy Policy from sign in page
    Given Open sign in page
    And Store original window
    When Click on Target privacy policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And User can close new window and switch back to original

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    And Store original window
    When Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page opened
    And User can close new window and switch back to original