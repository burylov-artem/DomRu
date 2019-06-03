from behave import *
from selenium.webdriver.common.keys import Keys
from features.steps.Abstract_selectors import Abstract_selectors
from features.steps.Find_selectors import Find_selectors
from selenium import webdriver
import unittest

use_step_matcher("re")


class Abstract_steps(unittest.TestCase):

    @Given("start browser chrome")
    def start(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.wd.maximize_window()

    @Given("open page \"(.*)\"")
    def open_page(self, url):
        self.wd.get(url)

    @Then("compare current url page with \"(.*)\"")
    def compare_current_url_page_with(self, home_url):
        current_url = self.wd.current_url
        self.assertEqual(current_url, home_url, "Текущий url не совпал с ожидаемым")

    @Then("displayed logo movix")
    def displayed_logo_movix(self):
        self.wd.find_element_by_xpath(Abstract_selectors.logo_img)

    @Then("displayed cards with text \"(.*)\" in result search")
    def displayed_card_with_text_in_result_search(self, text):
        self.wd.find_elements_by_xpath(str.format(Abstract_selectors.card_image_in_result_search, text))

    @Then("displayed card film with name \"(.*)\" in section movies")
    def displayed_card_film_with_name_in_section_movies(self, text):
        self.wd.find_elements_by_xpath(str.format(Abstract_selectors.section_card_film, text))

    @Then("displayed error text technical problems")
    def displayed_error_text_technical_problems(self):
        self.wd.find_element_by_xpath(Abstract_selectors.error_result_search)

    @Step("close browser")
    def close_browser(self):
        self.wd.quit()

    @Then("displayed slider")
    def displayed_slider(self):
        self.wd.find_element_by_xpath(Abstract_selectors.section_slider)

    @Then("displayed catalog item \"(.*)\"")
    def displayed_slider(self, text):
        self.wd.find_element_by_xpath(str.format(Abstract_selectors.catalog_item, text))

    @Then("displayed input global search")
    def displayed_input_global_search(self):
        self.wd.find_element_by_xpath(Find_selectors.input_global_search)

    @Then("displayed placeholder in input global search")
    def displayed_placeholder_in_input_global_search(self):
        self.wd.find_element_by_xpath(Find_selectors.input_search_with_placeholder)

    @Then("displayed magnifier in input global search")
    def displayed_magnifier_in_input_global_search(self):
        self.wd.find_element_by_xpath(Find_selectors.magnifier_in_global_search)

    @When("enter text in global search \"(.*)\"")
    def enter_text_in_global_search(self, text):
        self.wd.find_element_by_xpath(Find_selectors.input_global_search).send_keys(text)

    @When("push enter in global search")
    def push_enter(self):
        self.wd.find_element_by_xpath(Find_selectors.input_global_search).send_keys(Keys.ENTER)

    @Then("displayed text \"(.*)\" in input global search")
    def displayed_text_in_input_global_search(self, text):
        self.wd.find_element_by_xpath(str.format(Find_selectors.input_global_search_with_value, text))

    @When("clear input global search")
    def clear_input_global_search(self):
        self.wd.find_element_by_xpath(Find_selectors.input_global_search).clear()

    @Then("displayed text \"(.*)\" in drop down list results global search")
    def displayed_results_in_drop_down_list_input_global_search(self, text):
        self.wd.find_elements_by_xpath(str.format(Find_selectors.result_search_drop_down_list, text))

    @Then("displayed text not result search")
    def not_result_global_search(self):
        self.wd.find_element_by_xpath(Find_selectors.not_result_search)

    @Then("displayed label in result global search")
    def displayed_label_in_input_global_search(self):
        self.wd.find_element_by_xpath(Find_selectors.label_search)

    @Then("go to all search results")
    def open_page(self):
        self.wd.find_element_by_xpath(Find_selectors.all_result_search_in_input_search).click()

    @Then("go to first search result")
    def go_to_first_search_result(self):
        self.wd.find_element_by_xpath(Find_selectors.first_result_search_in_input_search).click()
