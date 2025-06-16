from ..locators.main_page_locators import MainPageLocators


test_data = [
    (MainPageLocators.QUESTION_COST, MainPageLocators.ANSWER_COST,
     "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (MainPageLocators.QUESTION_MULTIPLE_SCOOTERS, MainPageLocators.ANSWER_MULTIPLE_SCOOTERS,
     "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (MainPageLocators.QUESTION_RENT_TIME, MainPageLocators.ANSWER_RENT_TIME,
     "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (MainPageLocators.QUESTION_TODAY_ORDER, MainPageLocators.ANSWER_TODAY_ORDER,
     "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (MainPageLocators.QUESTION_EXTEND_RETURN, MainPageLocators.ANSWER_EXTEND_RETURN,
     "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (MainPageLocators.QUESTION_CHARGER, MainPageLocators.ANSWER_CHARGER,
     "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (MainPageLocators.QUESTION_CANCEL_ORDER, MainPageLocators.ANSWER_CANCEL_ORDER,
     "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (MainPageLocators.QUESTION_OUTSIDE_MKAD, MainPageLocators.ANSWER_OUTSIDE_MKAD,
     "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
]
