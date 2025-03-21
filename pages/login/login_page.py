from playwright.sync_api import Page, Locator

from pages.Products.products_page import ProductsListPage
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self._selectors = self._Selectors()

    def set_username(self, value: str):
        self.current_page.fill(self._selectors.USERNAME, value)

    def set_password(self, value: str):
        self.current_page.fill(self._selectors.PASSWORD, value)

    def click_login(self):
        self.current_page.click(self._selectors.LOGIN_BUTTON)

    def login_to_application(self, username: str, password: str) -> ProductsListPage:
        self.set_username(username)
        self.set_password(password)
        self.click_login()
        return ProductsListPage(self.current_page)

    def get_error_locator(self) -> Locator:
        return self.current_page.locator(self._selectors.ERROR_MSG)

    def get_login_button_locator(self) -> Locator:
        return self.current_page.locator(self._selectors.LOGIN_BUTTON)

    class _Selectors:
        USERNAME = "#outlined-adornment-email-login"
        PASSWORD = "#outlined-adornment-password-login"
        LOGIN_BUTTON = "//button[text()='Sign in']"
        ERROR_MSG = "[data-test='error']"