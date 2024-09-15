from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configuramos el WebDriver para Internet Explorer
driver = webdriver.Ie(executable_path='"C:\Webserver"')

try:
    # Navega a la página de tu aplicación
    driver.get("C:\Users\isido\breaks\isuuki.github.io\index.html")  

    # Encuentra el campo de entrada y el botón
    minutes_input = driver.find_element_by_id("minutes")
    start_button = driver.find_element_by_id("startButton")

    
    minutes_input.send_keys("5")  # Establece el temporizador para 5 minutos
    start_button.click()  # Inicia el temporizador

    # Esperar un momento para observar el resultado
    driver.implicitly_wait(10)  # Espera hasta 10 segundos

    # Captura de pantalla
    driver.save_screenshot('screenshot.png')

finally:
    # Cerrar el navegador
    driver.quit()
