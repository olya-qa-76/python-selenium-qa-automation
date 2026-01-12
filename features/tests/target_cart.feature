Feature: Tests for Cart feature

#  Scenario: User verifies Cart is empty
#    Given Open Target main page
#    When Click on Cart icon
#    Then Verify “Your cart is empty” message is shown

  Scenario: User verifies cart has individual items
    Given Open Target main page
    When Search for tea
    And Click "Add to cart" button
    And Click Side Nav "Add to cart" button
    And Open Target Cart page
    Then Verify Cart has more than 1 item(s)