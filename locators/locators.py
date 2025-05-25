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
    CONSTRUCTOR_LINK = (By.XPATH, '//a[@href="/"]/p[text()="Конструктор"]')#(By.LINK_TEXT, "Конструктор")
    BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]")
    SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]")
    FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]")
    SELECTED_TAB = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")
    INGREDIENT = (By.XPATH, '//p[contains(@class, "BurgerIngredient_ingredient__text__") and text()="Флюоресцентная булка R2-D3"]')#(By.XPATH, "//img[@class='BurgerIngredient_ingredient__image__3e-07' and @alt='Краторная булка N-200i']")
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    INGREDIENT_MODAL = (By.XPATH, '//h2[contains(@class, "Modal_modal__title__") and text()="Детали ингредиента"]')#(By.XPATH, "//div[contains(@class, 'Modal_modal_opened__3ISw4')]")
    INGREDIENT_MODAL_CLOSE = (By.XPATH, '//button[contains(@class, "Modal_modal__close__")]')#(By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    CART_DROPZONE = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]/li[contains(@class, 'BurgerConstructor_basket__listItem__aWMu1')]")
    COLLECT_INGREDIENT = (By.XPATH, '//h1[text()="Соберите бургер"]')

class OrdersFeedPageLocators:
    ORDERS_FEED_LINK = (By.XPATH, "//a[@href='/feed']")
    ORDER_ITEM = (By.XPATH, '(//ul[contains(@class, "OrderHistory_list__")]/li)[1]')#(By.XPATH, '//button[text()="Оформить заказ"]')#(By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList__cBvyi')]/li[1]")
    CLOSE_MODAL_BUTTON = (By.XPATH, '//button[@type="button" and contains(@class, "Modal_modal__close")]')#(By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, '//div[contains(@class, "OrderFeed")]/descendant::p[contains(@class, "OrderFeed_number__")]')#(By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[@class='OrderFeed_number__2MbrQ']")
    TODAY_ORDERS_COUNTER = (By.XPATH, '//p[contains(@class, "OrderFeed_number__") and contains(@class, "text_type_digits-large")]')#(By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[@class='OrderFeed_number__2MbrQ']")
    ORDER_STATUS_TEXT = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')#(By.XPATH, "//p[contains(@class, 'OrderInfo_status__1i4OX')]")
    ORDER_DETAIL_MODAL = (By.XPATH, '//p[contains(text(), "Cостав")]')#(By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]//h2[contains(@class, 'Modal_modal__title__2L34m')]")

class RecoveryPageLocators:
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(@class, "button_type_primary") and text()="Восстановить"]')#(By.XPATH, "//button[contains(@class, 'button_button_type_primary') and text()='Войти']") # (By.XPATH, '/html/body/div/div/main/div/form/button')
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class, "input__icon-action")]')#(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/div')#(By.XPATH, "//input[@type='password' or @type='text']/following-sibling::svg")
    CODE_INPUT_FIELD = (By.XPATH, '//label[text()="Введите код из письма"]')
