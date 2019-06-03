Feature: Testing module global search

  Background: start browser chrome
    Given start browser chrome

#  """Проверяем отображение поиска во всех разделах портала"""

  Scenario: Check displayed input global find on all pages
    Given open page "http://movix.ru/"
    Then displayed input global search

    Given open page "http://movix.ru/television"
    Then displayed input global search

    Given open page "http://movix.ru/tv-program"
    Then displayed input global search

    Given open page "http://movix.ru/services"
    Then displayed input global search

    Given open page "http://movix.ru/videoteka"
    Then displayed input global search
    * close browser

#  """Проверяем соответствие требований к глобальному поиску"""

  Scenario: Check compliance with the requirements to global search
    Given open page "http://movix.ru/"

    Then displayed placeholder in input global search
    Then displayed magnifier in input global search
    Then displayed label in result global search
    * close browser

  Scenario:  Negative tests on the search engine
    Given open page "http://movix.ru/"

    When enter text in global search "Запретная зона123123"
    Then displayed text not result search
    When clear input global search

    When enter text in global search "11111111111111111111111111111111111111111111111111111111111111111111"
    Then displayed text not result search
    When push enter in global search
    Then displayed text "11111111111111111111111111111111111111111111111111111111111111111111" in input global search
    When clear input global search

    Given open page "http://movix.ru/"
    When enter text in global search "<script>alert('Test');</script>"
    When push enter in global search
    Then displayed error text technical problems

    * close browser


#  """Позитивные тесты на механизм работы поиска"""

  Scenario: Positive tests on the search engine
    Given open page "http://movix.ru/"

#    """Присутствуют результаты поиска в выпадающем списке поиска"""
    When enter text in global search "Запретная зона"
    Then displayed text "Запретная зона" in drop down list results global search

#    """Присутствуют результаты на странице поиска (переход по enter)"""
    When push enter in global search
    Then displayed text "Запретная зона" in input global search
    Then displayed cards with text "Запретная зона" in result search

#    """Присутствуют результаты на странице поиска (переход по пункту Все результаты поиска)"""
    Given open page "http://movix.ru/"
    When enter text in global search "Запретная зона"
    Then go to all search results
    Then displayed text "Запретная зона" in input global search
    Given open page "http://movix.ru/"
    Then displayed cards with text "Запретная зона" in result search

#    """Переход по первому результату поиска"""
    Given open page "http://movix.ru/"
    When enter text in global search "Запретная зона"
    Then go to first search result
    Then displayed card film with name "Запретная зона" in section movies
    * close browser










