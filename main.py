import os
import openpyxl 
from funciones import *
from autowordpress import *





wc=WpConnection("https://calculadora-porcentajes-colombia.top//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
wc.connect()

etiquetas=['crepería','crepes']



ruta=os.getcwd()+("/img")
for img in os.listdir(ruta):
    provincia=obten_nombre_provincia(img)
    print(f"Creando el artículo de la provincia de {provincia}")
    #texto_con_estado=cambia_estado(texto_base,estado)
    #parrafos=texto_con_estado.split("\n")
    wp_img=Image(ruta+"/"+img,f"Creperías en la provincia de {provincia}")
    wp_img.upload(wc)
    wp_article=WpPost(f"Creperías en la provincia de {provincia}")
    #imagen=WpImage(wp_img)
    wp_article.add_element(crea_provincia("https://calculadora-porcentajes-colombia.top",provincia,obten_texto_provincia(provincia),wp_img))
    wc.publica_post(wp_article)


'''creperias=openpyxl.load_workbook('creperias.xlsx')
hoja_activa = creperias.active
fila=1
while fila<hoja_activa.max_row:
    print(hoja_activa.cell(row=fila,column=1).value)
    fila+=1'''