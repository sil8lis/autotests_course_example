from atf import log, info
from atf.ui import *


class MainPageSbisRu(Region):
    tabs = CustomList(By.CSS_SELECTOR, '.sbisru-Header__menu-item', 'Вкладки')
    start_work = Button(By.CSS_SELECTOR, '.sbisru-Button--primary', 'Начать работу')


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[name="Login"]', 'логин')
    password = TextField(By.CSS_SELECTOR, '[name="Password"]', 'пароль')


class MainPageOnline(Region):
    news_title = CustomList(By.CSS_SELECTOR, '.feed-Title', 'Заголовки новостей')
    popup_menu = Element(By.CSS_SELECTOR, '[templatename="Controls/menu:Popup"]', 'Меню')


class Test(TestCaseUI):

    def test(self):
        sbis_site = self.config.get('SBIS_SITE')

        self.browser.open(sbis_site)
        log('Проверить адрес сайта')
        self.browser.should_be(UrlExact(sbis_site))

        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact('Вход в личный кабинет'))

        log('Авторизоваться')
        user_login, user_password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER)
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

        info('Навести курсор на новость и сделать контекстный клик')
        main_page_online = MainPageOnline(self.driver)
        main_page_online.news_title.item(2).scroll_into_view().context_click()

        log('Проверить отображение контекстного меню')
        main_page_online.popup_menu.should_be(Visible)
