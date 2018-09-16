from selene import browser
from selene.support.jquery_style_selectors import s

from src.pages.MainPage import MainPage


class LoginPage(object):
    def __init__(self):
        self.username_input = s("#inputEmail3")
        self.password_input = s("#inputPassword")
        self.login_btn = s("button.btn")

    def open(self):
        browser.open_url("https://push.gravitec.net")
        return self

    def login_as(self, user):
        self.username_input.set(user.name)
        self.password_input.set(user.password)
        self.login_btn.click()
        return MainPage()
