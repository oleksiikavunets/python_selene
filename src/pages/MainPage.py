from selene.support.jquery_style_selectors import s

from src.pages.UsersPage import UsersPage


class MainPage(object):

    def __init__(self):
        self.logo = s("a.navbar")

    def go_to_user_tab(self):
        s("#users_link").click()
        return UsersPage()
