import unittest as unittest
from pages.basetest import BaseTest
from pages.basepage import BasePage
import time


class TestSearchTags(BaseTest):

	def __init__(self, methodName = 'runTest', log=None):
		BaseTest.__init__(self)
		
	def runTest(self):
		print "Starting Test"
		landing_page = BasePage(self.driver)
		tags_page = landing_page.header.click_on_tags_menu(self.driver)
		tags_page.enter_tag_to_search(self.driver, "qa")
		time.sleep(10)
		print "Tag searched for: qa"
		print "Count of the tag for this year"
		print tags_page.get_count_text(self.driver).split(" ")[0]
		

if __name__ =='__main__':
    unittest.main()
