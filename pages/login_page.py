class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = '[data-test="username"]'
        self.password = '[data-test="password"]'
        self.login_button = '[data-test="login-button"]'
        self.error_message = '[data-test="error"]'

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_button)

    def get_error(self):
        return self.page.inner_text(self.error_message)
