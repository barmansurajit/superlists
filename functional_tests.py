from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit();

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Aran has heard about a cool new online to-do app. He goes to check out its homepage
        self.browser.get('http://localhost:8000')
        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        self.fail('Finish the test')

        # He is invited to enter a to-do item straight away

        # He types "Buy Pokemon cards" into a text box

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy Pokemon cards" as an item in a to-do lists

        # There is still a text box inviting him to add another item. He
        # enters "Count the total health score of the Pokemon cards"

        # The page updates again, and now shows both the items in his lists

        # Aran wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him

        # He visits the URL - his to-do list is still there

        # Satisfied, he goes to sleep

if __name__ == '__main__':
    unittest.main()
