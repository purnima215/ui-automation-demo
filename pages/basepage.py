from page import Page

class BasePage(Page):

    webdriver = Page.webdriver

    @property
    def header(self):
        return BasePage.HeaderRegion(self.webdriver)

    @property
    def footer(self):
        return BasePage.FooterRegion(self.webdriver)

    def _validate_page(self, webdriver):
        pass

    class HeaderRegion(Page):

        #sign_up_link = 
		#login_link = 
		
		#Menu items
		tags_menu = lambda self:self.locate_id("nav-tags")
		
		def click_on_tags_menu(self, driver):
			#self.log.debug("About to click on the tags menu")
			self.tags_menu().click()
			from pages.tags_page import TagsPage
			return TagsPage(driver)
		
		
			
			
