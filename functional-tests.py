from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # I am going to check out a new to-do list app on the internet. I am going to the homepage now.
        self.browser.get('http://localhost:8000')
        # The page title and header have 'to-do' in it.
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        #I am interested in entering a todo item right away.

        #I type "Whatever I want" into a text box.

        #When I hit enter, the page updates, and now the page lists my todo item.

        #I can still add another item, since there is still a text box inviting me to do so. So i enter "Wash my Car".

        #The page now updates again, and shows both items in my list.

        #Now Im wondering if the site will remember my list. But then I notice a unique URL, just for me.

        #I go ahead and visit that URL, and low and behold, my list is still alive!

        #Happy that Ive got my list in order, I go grab a beer.
        browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')

