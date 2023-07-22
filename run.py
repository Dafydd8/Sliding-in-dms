from selenium import webdriver
import datos
import acciones
import time

chromedriver = datos.chromedriverpath
usuario = datos.usuario
clave = datos.clave
code = datos.code
url = datos.url
mensaje = 'acá va tu mensaje'
try:
	driver = webdriver.Chrome()
except:
	driver = webdriver.Chrome(chromedriver)
driver.get(url)

acciones.iniciar_sesion(driver, usuario, clave)
time.sleep(3.0)
acciones.insert_code(driver, code)
time.sleep(3.0)
acciones.ahora_no(driver)
time.sleep(3.0)
acciones.enviar_msg(driver, mensaje)







