Feature: Tests for Search

  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown

#  Scenario: User can search for a product on Target
#    Given Open Target main page
#    When Search for mug
#    Then Search results for mug are shown

#  Scenario: User can search for a product on Target
#    Given Open Target main page
#    When Search for coffee
#    Then Search results for coffee are shown

"""
 Scenario Outlines:
 For testing the same scenario with multiple sets of data,
 you can use Scenario Outline with Examples tables in Gherkin.
 Values in the examples table are referenced using <column_name> in the scenario steps.
"""

  Scenario Outline: User can search for a product on Target
    Given Open Target main page
    When Search for <product>
    Then Search results for <product_result> are shown
    Examples:
    |product    |product_result   |
    |tea        |tea              |
    |mug        |mug              |
    |coffee     |coffee           |

"""
NB. Scenario outlines are mostly used in registration input data tests (valid/invalid).
"""
#    Scenario Outline: Login error shown for invalid login
#    Given Open login page
#    When Enter login username <username>
#    And Enter login password <password>
#    Then Verify login error message <error_message>
#    Examples:
#    |username  |password        |error_message                 |
#    |non_exist |password122     |this account not found        |
#    |user123   |incorrect_pass  |this password is not correct  |