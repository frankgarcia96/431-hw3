from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_add_new_post(self):
        #user decides to create a post
        self.browser.get('http://localhost:8000/post/new/')

        #user checks the title of the page
        self.assertIn('Django Girls blog', self.browser.title)

        #user inputs a title for the post
        inputbox = self.browser.find_element_by_id('id_title')
        inputbox.send_keys('test title')

        #user goes to text box
        inputbox.send_keys(Keys.ENTER)

        #user enters their post content
        inputbox = self.browser.find_element_by_id('id_text')
        inputbox.send_keys('hello, from user123')

    def test_add_comment(self):
        # Suzy Q Wants to post a comment on our website
        self.browser.get('http://localhost:8000/post/1')
        driver = webdriver.Firefox()
        driver.get('http://localhost:8000/post/1')

        # She is invited to enter a comment by clicking the button
        driver.find_elements_by_link_text('Add Comment').click()
        time.sleep(1)

    	#She is taken to the comment page, and is prompted to enter author
        inputbox = self.browser.find_element_by_id('id_author')
        inputbox.send_keys('Suzy Q')

    	#When she hits enter, she is transferred to the content box
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # She is invited to enter a her comment, and enters her comment
        inputbox = self.browser.find_element_by_id('id_text')
        inputbox.send_keys('I love this post lol')

    	#When she clicks save, she is transferred back to the post
        driver.find_element_by_class('save').click()
        time.sleep(1)
        self.assertIn('post/1',self.browser.current_url)

test = NewVisitorTest()
test.setUp()
test.test_add_new_post()
test.test_add_comment()
