from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # I am going to check out a new to-do list app on the internet. I am going to the homepage now.
        self.browser.get(self.live_server_url)
        
        # The page title and header have 'to-do' in it.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        #I am interested in entering a todo item right away.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        
        #I type "Whatever I want" into a text box.
        inputbox.send_keys("Whatever I want")
        
        #When I hit enter, the page updates, and now the page lists my todo item.
        inputbox.send_keys(Keys.ENTER)
        keith_list_url = self.browser.current_url
        self.assertRegex(keith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Whatever I want')
        # import time
        # time.sleep(10)
        
        #I can still add another item, since there is still a text box inviting me to do so. So i enter "Wash my Car".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Wash my Car")
        inputbox.send_keys(Keys.ENTER)

        #The page now updates again, and shows both items in my list.
        self.check_for_row_in_list_table('1: Whatever I want')
        self.check_for_row_in_list_table('2: Wash my Car')
        ## Now a new user comes along, Alison.
        ## We use a new browser session to make sure that no information of Mine comes through in the cookies.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Alison visits the home page. There is nothing of Mine showing.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Whatever I want', page_text)
        self.assertNotIn('Wash my Car', page_text)

        # Alison starts making her own list.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #Alison gets her own uniique URL.
        alison_list_url = self.browser.current_url
        self.asserRegex(alison_list_url, '/lists/.+')
        self.assertNotEqual(alison_list_url, keith_list_url)

        # Again there is now trace of My list.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Whatever I want', page_text)
        self.assertIn('Buy milk', page_text)



        #Now Im wondering if the site will remember my list. But then I notice a unique URL, just for me.
        self.fail('Pick up here!')
        #I go ahead and visit that URL, and low and behold, my list is still alive!

        #Happy that Ive got my list in order, I go grab a beer.
        browser.quit()


# if __name__ == '__main__':
    # unittest.main(warnings='ignore')

