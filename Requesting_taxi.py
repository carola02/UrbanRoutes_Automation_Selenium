import confirmation_code
import data
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WDW


class UrbanRoutesPages:

    # Setting route
    from_field_id = 'from'
    to_field_id = "to"
    home_url = data.urban_routes_url
    # Selecting a tariff
    taxi_button_class = 'button.button.round'
    tariff_comfort_xpath = "//div[@class='tcard-title' and text()='Comfort']"
    # Client info
    # Phone number
    phone_number_form_css_selector = '.np-button .np-text'
    phone_numer_field_id = "phone"
    get_confirmation_code_xpath = "//button[@type='submit'][@class='button full']"
    code = 'code'
    confirmation_code_button = "//button[text()='Confirmar']"
    # Payment method
    credit_card_selector_field_class_name = 'pp-button.filled'
    add_credit_card_button_class_name = "pp-plus-container"
    add_card_numer_id = "number"
    add_card_code_id = "code"
    scratch_space_class_name = "plc"
    submit_button_xpath = "//button[text()='Agregar']"
    close_credit_card_popup_xpath = "//*[@id='root']/div/div[2]/div[2]/div[1]/button"
    # Driver comment
    send_comment_driver_id = 'comment'
    # Special Requests
    blanket_slider_css_selector = ".r-sw-container:nth-of-type(1) .slider.round"
    ice_cream_plus_css_selector = ".r-counter-container:nth-of-type(1) .counter-plus"
    # Call for taxi
    call_taxi_button = "smart-button"
    waiting_window_popup = '.order-header-title'


class TestUrbanRoutes:

    home = None
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.home = UrbanRoutesPages.home_url
        cls.driver.get(cls.home)

    def test_set_route_1(self):
        driver = self.driver
        home = UrbanRoutesPages
        WDW(driver, 10).until(EC.presence_of_element_located((By.ID, home.from_field_id)))
        from_field = driver.find_element(By.ID, home.from_field_id)
        from_field.send_keys(data.address_from)
        to_field = driver.find_element(By.ID, home.to_field_id)
        to_field.send_keys(data.address_to)

        # # asserts
        # assert from_field.get_attribute('value') == data.address_from, "La dirección de origen es correcta"
        # assert to_field.get_attribute('value') == data.address_to, "La dirección de destino es correcta"

    def ask_for_taxi_2(self):
        driver = self.driver
        home = UrbanRoutesPages
        WDW(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, home.taxi_button_class)))
        driver.find_element(By.CLASS_NAME, home.taxi_button_class).click()

    def select_tariff_3(self):
        driver = self.driver
        home = UrbanRoutesPages
        driver.find_element(By.XPATH, home.tariff_comfort_xpath).click()

    def entering_phone_number_4(self):
        driver = self.driver
        home = UrbanRoutesPages
        WDW(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, home.phone_number_form_css_selector)))
        driver.find_element(By.CSS_SELECTOR, home.phone_number_form_css_selector).click()
        WDW(driver, 5).until(EC.element_to_be_clickable((By.ID, home.phone_numer_field_id)))
        phone_field_assertion = driver.find_element(By.ID, home.phone_numer_field_id)
        driver.find_element(By.ID, home.phone_numer_field_id).send_keys(data.phone_number)
        # assert
        assert phone_field_assertion.get_attribute('value') == data.phone_number, "El número de teléfono no es correcto"
        driver.find_element(By.XPATH, home.get_confirmation_code_xpath).click()
        WDW(driver, 5).until(EC.element_to_be_clickable((By.ID, home.code)))
        driver.implicitly_wait(5)
        sms_code = confirmation_code.retrieve_phone_code(driver=self.driver)
        driver.find_element(By.ID, home.code).send_keys(sms_code)
        driver.find_element(By.XPATH, home.confirmation_code_button).click()
        # pop-up will close itself once the code has been entered

    def credit_card_5(self):
        driver = self.driver
        home = UrbanRoutesPages
        WDW(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, home.credit_card_selector_field_class_name)))
        driver.find_element(By.CLASS_NAME, home.credit_card_selector_field_class_name).click()
        driver.find_element(By.CLASS_NAME, home.add_credit_card_button_class_name).click()
        driver.find_element(By.ID, home.add_card_numer_id).send_keys(data.card_number)
        driver.find_element(By.NAME, home.add_card_code_id).send_keys(data.card_code)
        driver.find_element(By.CLASS_NAME, home.scratch_space_class_name).click()
        driver.find_element(By.XPATH, home.submit_button_xpath).click()
        driver.find_element(By.XPATH, home.close_credit_card_popup_xpath).click()

    def comment_to_driver_6(self):
        driver = self.driver
        home = UrbanRoutesPages
        comment_field = driver.find_element(By.ID, home.send_comment_driver_id)
        comment_field.send_keys(data.message_for_driver)
        # Assert
        assert comment_field.get_attribute('value') == data.message_for_driver, "El comentario al conductor no es correcto"

    def special_requests_7(self):
        driver = self.driver
        home = UrbanRoutesPages
        WDW(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, home.blanket_slider_css_selector)))
        driver.find_element(By.CSS_SELECTOR, home.blanket_slider_css_selector).click()
        driver.find_element(By.CSS_SELECTOR, home.ice_cream_plus_css_selector).click()
        driver.find_element(By.CSS_SELECTOR, home.ice_cream_plus_css_selector).click()

    def call_for_taxi_8(self):
        driver = self.driver
        home = UrbanRoutesPages
        driver.find_element(By.CLASS_NAME, home.call_taxi_button).click()
        time.sleep(22)
        WDW(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, home.waiting_window_popup)))

    @classmethod
    def teardown_class(cls):
        time.sleep(3)
        cls.driver.quit()
