from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_HEADER_BTN = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[text()='Заказать']")
    ORDER_BOTTOM_BTN = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button[text()='Заказать']")
    YA_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    QUESTION_COST = (By.ID, "accordion__heading-0")
    QUESTION_MULTIPLE_SCOOTERS = (By.ID, "accordion__heading-1")
    QUESTION_RENT_TIME = (By.ID, "accordion__heading-2")
    QUESTION_TODAY_ORDER = (By.ID, "accordion__heading-3")
    QUESTION_EXTEND_RETURN = (By.ID, "accordion__heading-4")
    QUESTION_CHARGER = (By.ID, "accordion__heading-5")
    QUESTION_CANCEL_ORDER = (By.ID, "accordion__heading-6")
    QUESTION_OUTSIDE_MKAD = (By.ID, "accordion__heading-7")

    ANSWER_COST = (By.ID, "accordion__panel-0")
    ANSWER_MULTIPLE_SCOOTERS = (By.ID, "accordion__panel-1")
    ANSWER_RENT_TIME = (By.ID, "accordion__panel-2")
    ANSWER_TODAY_ORDER = (By.ID, "accordion__panel-3")
    ANSWER_EXTEND_RETURN = (By.ID, "accordion__panel-4")
    ANSWER_CHARGER = (By.ID, "accordion__panel-5")
    ANSWER_CANCEL_ORDER = (By.ID, "accordion__panel-6")
    ANSWER_OUTSIDE_MKAD = (By.ID, "accordion__panel-7")