
#BasePage 

import abc
from selenium.common.exceptions import NoAlertPresentException, ElementNotVisibleException,\
    NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

class Page(object):
	
	"""This is the super class for all the Pages. It contains all the wrappers for locators, any common functionality that is across
	pages and custom defined exceptions"""
	
	webdriver = None

	def __init__(self, webdriver, log = None):
		"""Constructor for Page Object."""
		if log == None:
		#instantiate the logger
			pass
		else:
			self.log = log
		self._validate_page(webdriver)
		self.webdriver = webdriver
		
	def locate_id(self, locator):
		element = self.webdriver.find_element_by_id(locator)
		if element:
			return element
		else:
			raise NoSuchElementException
			
	def locate_xpath(self, locator):
		element = self.webdriver.find_element_by_xpath(locator)
		if element:
			return element
		else:
			raise NoSuchElementException
	
	@abc.abstractmethod
	def _validate_page(self, webdriver):
		"""
		Perform checks to validate this page is the correct target page.
        
		@raise IncorrectPageException: Raised when we try to assign the wrong page to this page object.	
		"""
		return
		
class InvalidPageError(Exception):
	'''Thrown when tried to instantiate the incorrect page to a Page object.'''