from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data


# no modificar

class UrbanRoutesPage:
    urban_url = data.urban_routes_url
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.CLASS_NAME, 'button.button.round')
    tariff_comfort = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_number_form = (By.CSS_SELECTOR, '.np-button .np-text')
    phone_numer_field = (By.ID, 'phone')
    get_confirmation_code_button = (By.XPATH, "//button[@type='submit'][@class='button full']")
    confirmation_writing_field = (By.ID, 'code')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')



