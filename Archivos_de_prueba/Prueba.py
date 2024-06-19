from selenium import webdriver
import data
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # controlador para usar en este caso Google Chrome
driver.maximize_window()  # Modo de pantalla completa para las pruebas
urban_routes = data.urban_routes_url
driver.get(data.urban_routes_url)
time.slee
# current_url = driver.current_url
#assert current_url == 'https://cnt-4d55fbf2-4e91-4267-9d2c-b367e3a1767f.containerhub.tripleten-services.com/?lng=es'
driver.find_element(By.ID, "from")

time.sleep(5)
driver.quit()



