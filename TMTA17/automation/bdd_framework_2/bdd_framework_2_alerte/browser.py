from seleniumbase import Driver

class Browser():
		driver = Driver()
		driver.maximize_window()
		driver.implicitly_wait(5)
		driver.set_page_load_timeout(5)

		def close_browser(self):
				self.driver.quit()