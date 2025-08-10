from funciones import *
from extraer_datos_excel import *
from autowordpress import *




dominio="https://calculadora-porcentajes-colombia.top"
wc=WpConnection(f"{dominio}//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
wc.connect()

etiquetas=['crepería','crepes','creperias cerca','crepe suzette','crepe nutella','crepe nocilla','crepe chocolate']
wp_article=WpPage(f"Creperías de prueba")
#wp_article.add_tag("provincias")
wp_article.add_element(WpHeader("Hola",2))
wp_article.set_slug("prueba-etiqueta")
print(wp_article.page)
wc.publica_page(wp_article)