import time
import data
import confirmation_code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# chrome_options = ChromeOptions()
# chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data.urban_routes_url)
validating_current_url = driver.current_url

print(validating_current_url)
print(data.urban_routes_url)
# assert validating_current_url == data.urban_routes_url


# # fill address spaces
# WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "from")))
# driver.find_element(By.ID, "from").send_keys(data.address_from)
# driver.find_element(By.ID, "to").send_keys(data.address_to)
#
# # first button
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'button.button.round')))
# taxi_button = driver.find_element(By.CLASS_NAME, 'button.button.round')
# taxi_button.click()
#
# # tariff selection
# tariff_comfort = driver.find_element(By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
# tariff_comfort.click()
#
# # BOTÓN PARA NUMERO DE TELEFONO
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.np-button .np-text')))
# phone_number_form = driver.find_element(By.CSS_SELECTOR, '.np-button .np-text')
# phone_number_form.click()
#
# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".head[text='Introduce tu número de teléfono']")))
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.full')))
# phone_numer_field = driver.find_element(By.ID, 'phone')
# phone_numer_field.send_keys(data.phone_number)
#
# get_confirmation_code_button = driver.find_element(By.XPATH, "//button[@type='submit'][@class='button full']")
# get_confirmation_code_button.click()
#
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'code')))
# driver.implicitly_wait(5)
# confirmation_writing_field = driver.find_element(By.ID, 'code')
# confirmation_writing_field.send_keys(confirmation_code.retrieve_phone_code())
#
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp-button.filled")))
# credit_card_selector = driver.find_element(By.CLASS_NAME, "pp-button.filled")
# credit_card_selector.click()
#
# add_credit_card_button = driver.find_element(By.CLASS_NAME, "pp-plus-container")
# add_credit_card_button.click()
#
# add_card_numer = driver.find_element(By.ID, "number")
# add_card_numer.send_keys(data.card_number)
#
# add_card_code = driver.find_element(By.NAME, "code")
# add_card_code.send_keys(data.card_code)
#
# scratch_space = driver.find_element(By.CLASS_NAME, "plc")
# scratch_space.click()
#
# submit_button = driver.find_element(By.XPATH, "//button[text()='Agregar']")
# # submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'].button.full")
# submit_button.click()
#
# # close_credit_card_popup = driver.find_element(By.CLASS_NAME, 'close-button.section-close')
# # close_credit_card_popup = driver.find_element(By.CSS_SELECTOR, "button[class='close-button section-close']")
# # close_credit_card_popup = driver.find_element(By.CLASS_NAME, "close-button")
# close_credit_card_popup = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")
# close_credit_card_popup.click()
#
# send_comment_driver = driver.find_element(By.ID, 'comment')
# send_comment_driver.send_keys(data.message_for_driver)
#
# # Despliegue de opciones
# # service_request = driver.find_element(By.CLASS_NAME, 'reqs-head')
# # service_request.click()
#
#
# # blanket_label = driver.find_element(By.CSS_SELECTOR, "div.r-sw-label:contains('Manta y pañuelos')")
# # blanket_label = driver.find_element(By.CLASS_NAME, "r-sw-container")
# # blanket_slider_css_selector = '.reqs-body .r-type-switch:nth-of-type(1) .slider'
# blanket_slider_css_selector = ".r-sw-container:nth-of-type(1) .slider.round"
# WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, blanket_slider_css_selector)))
# driver.find_element(By.CSS_SELECTOR, blanket_slider_css_selector).click()
#
# ice_cream_plus = ".r-counter-container:nth-of-type(1) .counter-plus"
# driver.find_element(By.CSS_SELECTOR, ice_cream_plus).click()
# driver.find_element(By.CSS_SELECTOR, ice_cream_plus).click()
#
# # strawberry_plus = ".r-counter-container:nth-of-type(3) .counter-plus"
# # driver.find_element(By.CSS_SELECTOR, strawberry_plus).click()

time.sleep(3)
driver.quit()
