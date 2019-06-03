Feature: Home page

"""Перейдя на movix.ru  попадаем на домашнию страницу с лого"""

  Background: start browser chrome
    Given start browser chrome

  Scenario: displayed sections
    Given open page "http://movix.ru/"
    Then displayed slider
    Then displayed catalog item "Телевидение"
    Then displayed catalog item "Пакеты каналов"
    Then displayed catalog item "Фильмы"
    Then displayed catalog item "Подборки"
    Then displayed catalog item "Подписки"
    Then displayed catalog item "Жанры"
    Then displayed catalog item "Сериалы"
    * close browser





