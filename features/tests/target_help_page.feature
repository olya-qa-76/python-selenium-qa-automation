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

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

  Scenario: User can select Help topic Target Circle™
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened