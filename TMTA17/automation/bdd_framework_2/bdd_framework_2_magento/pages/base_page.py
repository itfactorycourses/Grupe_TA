from browser import Browser


# contine metode care sunt folosite in mai multe clase de test (spre exemplu,
# 		putem sa folosim input si in modulul de login, si in modulul de search,
#  		si in modulul de creare cont. E practic o pagina ajutatoare

class Base_Page(Browser):

		def enter_text(self, by, value, search_value):
				self.driver.find_element(by, value).send_keys(search_value)

