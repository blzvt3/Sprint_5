from selenium.webdriver.common.by import By

class Locators:
    NAME_INPUT = (By.XPATH, "//label[contains(text(),'Имя')]/following-sibling::input") # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input") # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(),'Пароль')]/following-sibling::input") # Поле ввода пароля

    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']") # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']") # Кнопка "Войти" на странице входа
    LOGIN_HYPERLINK = (By.XPATH, "//a[text() = 'Войти']") # Гиперссылка "Войти" на страницах регистрации и восстановления пароля
    PROFILE_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']") # Кнопка "Личный Кабинет"
    PROFILE_EMAIL = (By.XPATH, "//input[@value='tsukanov18000@mail.ru']") # Значение поля "Логин" в личном кабинете
    SIGNUP_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    SIGNUP_HYPERLINK = (By.XPATH, "//a[text() = 'Зарегистрироваться']") # Гиперссылка "Зарегистрироваться"
    RESET_PASSWORD_HYPERLINK = (By.XPATH, "//a[text() = 'Восстановить пароль']") # Гиперссылка "Восстановить пароль"
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[text() = 'Восстановить']")  # Кнопка "Восстановить"
    SIGN_OUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']") # Кнопка "Выход"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']") # Кнопка "Конструктор"
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Логотип "Stellar Burgers"
    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")  # Кнопка "Оформить заказ"
    PASSWORD_ERROR = (By.XPATH, "//p[text() = 'Некорректный пароль']")  # Ошибка "Некорректный пароль"

    BUNS_BUTTON =  (By.XPATH, "//span[text() = 'Булки']") # Кнопка "Булки"
    SAUCES_BUTTON = (By.XPATH, "//span[text() = 'Соусы']") # Кнопка "Соусы"
    FILLINGS_BUTTON = (By.XPATH, "//span[text() = 'Начинки']") # Кнопка "Начинки"
    BUNS_TITLE = (By.XPATH, "//h2[text() = 'Булки']")  # Заголовок "Булки"
    SAUCES_TITLE = (By.XPATH, "//h2[text() = 'Соусы']")  # Заголовок "Соусы"
    FILLINGS_TITLE = (By.XPATH, "//h2[text() = 'Начинки']")  # Заголовок "Начинки"