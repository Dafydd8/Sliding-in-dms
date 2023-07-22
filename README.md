# Sliding-in-dms
Proyectito básico de web scraping

## Selenium y ChromeDriver
El programa requiere un package de Python llamada *Selenium* y una herramienta llamada *ChromeDriver*. *Selenium* se puede instalar usando el package manager pip, con el comando `pip install selenium` o con *conda*, usando el comando `conda install -c conda-forge selenium `. *ChromeDriver* se puede descargar de la página oficial. También se deja una opción ya en el repositorio. Se puede ubicar en el mismo directorio que el programa, o en el PATH del sistema operativo.

## Instrucciones de uso:
  1.	Completar *datos.py* con nombre de usuario, clave y un código de seguridad. Luego ingresar en *url* el link al chat al que se desea enviar un mensaje. Para eso, se debe haber iniciado sesión previamente en Instagram, ingresado al chat deseado y obtenido su url.
*Nota: Los códigos de seguridad se consiguen desde la app de Instagram en la sección de seguridad. Cada uno de ellos se puede usar una sola vez*
  2.	Completar *run.py* con el mensaje a enviar.
  3.	Correr *run.py* con el comando `python run.py` o `python3 run.py`.
