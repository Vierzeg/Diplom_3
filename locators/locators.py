# locators.py

from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD_LOG = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD_LOG = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    LOGIN_FROM_REG_BUTTON = (By.XPATH, "//a[text()='Войти']")

class RegisterPageLocators:
    NAME_FIELD_REG = (By.XPATH, "//input[@name='name']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    LOG_IN_ACC_CRIT = (By.XPATH, '//p[contains(text(), "новый пользователь")]/a')

class ProfilePageLocators:
    PROFILE_BUTTON = (By.XPATH, "//a[p[text()='Личный Кабинет']]")
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    PROFILE_LOC = (By.XPATH, '//a[text()="Профиль"]')
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGO_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_HISTORY_BLOCK = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r')]")

class ConstructorPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, '//a[@href="/"]/p[text()="Конструктор"]')
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]")
    SELECTED_TAB = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")
    INGREDIENT = (By.XPATH, '//p[contains(@class, "BurgerIngredient_ingredient__text__") and text()="Флюоресцентная булка R2-D3"]')
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    INGREDIENT_MODAL = (By.XPATH, '//h2[contains(@class, "Modal_modal__title__") and text()="Детали ингредиента"]')
    INGREDIENT_MODAL_CLOSE = (By.XPATH, '//button[contains(@class, "Modal_modal__close__")]')
    CART_DROPZONE = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]/li[contains(@class, 'BurgerConstructor_basket__listItem__aWMu1')]")
    COLLECT_INGREDIENT = (By.XPATH, '//h1[text()="Соберите бургер"]')

class OrdersFeedPageLocators:
    ORDERS_FEED_LINK = (By.XPATH, "//a[@href='/feed']")
    ORDER_ITEM = (By.XPATH, '(//ul[contains(@class, "OrderHistory_list__")]/li)[1]')
    CLOSE_MODAL_BUTTON = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close")]')
    TOTAL_ORDERS_COUNTER = (By.XPATH, '//div[contains(@class, "OrderFeed")]/descendant::p[contains(@class, "OrderFeed_number__")]')
    TODAY_ORDERS_COUNTER = (By.XPATH, '//p[contains(@class, "OrderFeed_number__") and contains(@class, "text_type_digits-large")]')
    ORDER_STATUS_TEXT = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    ORDER_DETAIL_MODAL = (By.XPATH, '//p[contains(text(), "Cостав")]')

class RecoveryPageLocators:
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(@class, "button_type_primary") and text()="Восстановить"]')
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class, "input__icon-action")]')
    CODE_INPUT_FIELD = (By.XPATH, '//label[text()="Введите код из письма"]')
