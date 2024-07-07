from selenium.webdriver.common.by import By

class ConstructorLocators:
    INGREDIENT = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[1]/a[1]/img")
    ADD_TO_ORDER_BUTTON = (By.ID, "add-to-order-button")
    CLOSE_DETAILS_BUTTON = (By.XPATH, "(.//button[@type='button' and contains(@class, 'modal__close')])[1]")
    SUBMIT_ORDER_BUTTON = (By.XPATH, "/html/body/div/div/main/section[2]/div/button")
    CONSTRUCTOR_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p")
    LOGIN_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/button")
    ORDER_LIST_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/ul/li[2]/a/p")
    COUNT_OF_INGREDIENTS = (By.XPATH, './/p[contains(@class, "counter_counter__num__3nue1")]')
    FIRST_BUN_FROM_BUNS = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")
    ORDER_AREA = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    MAKE_BURGER_HEADING = (By.XPATH, "//h1[contains(@class, 'text') and contains(@class, 'text_type_main-large') and contains(@class, 'mb-5') and contains(@class, 'mt-10')]")
    ORDER_LIST_HEADING = (By.XPATH, "/html/body/div/div/main/div/h1")
    DETAILS_OF_INGRADIENTS_HEADING = (By.XPATH, "/html/body/div/div/section[1]/div[1]/div/h2")
    INFORMATION_ON_SUBMIT_WINDOW = (By.XPATH, "/html/body/div/div/section/div[1]/div/div[2]/p[1]")

