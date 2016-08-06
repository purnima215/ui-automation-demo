#Class for Region of Tags. 

from basepage import BasePage
from page import InvalidPageError
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

class TagsPage(BasePage):
	
	"""This covers the Tag page region."""

	_tags_page_title = "Tags - Stack Overflow"
	
	tagfilter_textbox = lambda self:self.locate_id("tagfilter")
	#Instead of xpath, the better way to locate such elements is sizzle. That would need modification to webdriver.py
	#The assumption here is that the search results are already sorted. And that the last string gives the count of the year. 
	count_text = lambda self:self.locate_xpath("//*[@id='tags-browser']/tbody/tr[1]/td[1]/div[2]/div[1]/a[2]")	
	
	def _validate_page(self, driver):
		'''Validates if it is Tags Page that is currently opened.'''
		if driver.title != self._tags_page_title:
			#self.is_error_present_on_opened_page(driver)
			raise InvalidPageError("This is not Stack Overflow Tags Page. Currently at %s" %(driver.current_url))			
	
	def get_count_text(self, driver):
		'''Gets the text of the count element displayed.'''
		return self.count_text().text
		
	def enter_tag_to_search(self, driver, search_string):
		"""Enters the search string in the Tags Filter"""
		self.tagfilter_textbox().send_keys(search_string)
		
