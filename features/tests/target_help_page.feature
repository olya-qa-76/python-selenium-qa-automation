Feature: Tests for Help features

  Scenario: User verifies Target Help page UI
    Given Open Target Help page
    Then Verify 'Help' header
    And Verify 2 elements block
    And Verify 'Browse all help' button
    And Verify 'Help Search' field
    And Verify 'Search' button
    And Verify 'What would you like help with' header
    And Verify 'Navigation Card' wrapper
    And Verify 'Popular Pages' header
    And Verify 'Link Card' container