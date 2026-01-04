# Created by lenovo at 12/30/2025
Feature: Target Sign In tests

  Scenario: User can navigate to Sign In
    Given Open Target main page
    When Click "Account" button
    And From right side navigation menu, click "Sign In" button
    Then Verify Sign In form opened