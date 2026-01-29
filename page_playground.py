class Page:  # blueprint

    def click(self):
        print('Clicking...')

    def input_text(self, text):
        print(f"Entering text: {text}")

    def verify_element(self, locator):
        print(f"Verifying element: {locator}")


class LoginPage(Page):

    def open_login(self):
        print("Opening login...")

    def click_login(self):
        self.click()

    def input_username(self):
        self.input_text("Username")

    def verify_button(self):
        self.verify_element("Login")


class RegisterPage(Page):
    pass

class Header(Page):
    pass

login_page = LoginPage()
login_page.open_login()
login_page.click_login()
login_page.input_username()
login_page.verify_button()