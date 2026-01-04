# Created by lenovo at 12/29/2025
Feature: Tests for search

  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown

  Scenario: User verifies Cart is empty
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown