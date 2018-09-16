from selene.support.conditions import have

from src.domain.User import User
from src.pages.LoginPage import LoginPage


def test_can_add_new_user():

    admin = User("admin", "admin")

    user = User("donald", "123456", "donald@mail.se")
    (LoginPage().open()
     .login_as(admin)
     .go_to_user_tab()
     .add_new_user(user)
     .table.user_names().should(have.text("donald")))
