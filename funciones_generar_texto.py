import re
from random import choice,randint
from crea_elementos_web import *    

from ficheros_datos.keywords import *
from ficheros_datos.datos_población import *
from ficheros_datos.constantes_configuracion import *


def spinner(s):
     
    while True:
        s, n = re.subn('{([^{}]*)}',
                    lambda m: choice(m.group(1).split("|")),
                    s)
        if n == 0: break
    return s.strip()

def obten_texto_H1(provincia):
    with open('plantillas_textos/provincia_H1.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        texto=texto.replace("*Provincia*",provincia)
        cantidad_keywords=texto.find("#keyword#")
        i=0
        keywords_usadas=[]
        while i<cantidad_keywords:
            nueva_keyword=randint(0,len(keywords_h1)-1)
            if nueva_keyword not in keywords_usadas:
                keywords_usadas.append(nueva_keyword)
                texto=texto.replace("#keyword#",keywords_h1[nueva_keyword],1)      
            i+=1
        return texto
    
def obten_texto_H2_general(fichero,lista_keywords,provincia):
    with open(f'plantillas_textos/{fichero}', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        texto=texto.replace("*Provincia*",provincia)
        cantidad_keywords=texto.find("#keyword#")
        i=0
        keywords_usadas=[]
        while i<cantidad_keywords:
            nueva_keyword=lista_keywords[randint(0,len(lista_keywords)-1)]
            if nueva_keyword not in keywords_usadas:
                keywords_usadas.append(nueva_keyword)
                texto=texto.replace("#keyword#",nueva_keyword,1)      
            i+=1
        return texto   

def obten_texto_H2_transaccional():
    with open('plantillas_textos/H2_transaccional.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        cantidad_keywords=texto.find("#keyword#")
        i=0
        keywords_usadas=[]
        while i<cantidad_keywords:
            nueva_keyword=randint(0,len(keywords_transaccionales)-1)
            if nueva_keyword not in keywords_usadas:
                keywords_usadas.append(nueva_keyword)
                texto=texto.replace("#keyword#",keywords_transaccionales[nueva_keyword],1)      
            i+=1
        return texto
    
def obten_texto_H2_informacional():
    with open('plantillas_textos/H2_informacional.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        cantidad_keywords=texto.find("#keyword#")
        i=0
        keywords_usadas=[]
        while i<cantidad_keywords:
            nueva_keyword=randint(0,len(keywords_informacionales)-1)
            if nueva_keyword not in keywords_usadas:
                keywords_usadas.append(nueva_keyword)
                texto=texto.replace("#keyword#",keywords_informacionales[nueva_keyword],1)      
            i+=1
        return texto
def obten_texto_tipo_maquinaria():
    with open('plantillas_textos/H2_tipo_maquinaria.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        cantidad_keywords=texto.find("#keyword#")
        i=0
        keywords_usadas=[]
        while i<cantidad_keywords:
            nueva_keyword=randint(0,len(keywords_tipo_maquinaria)-1)
            if nueva_keyword not in keywords_usadas:
                keywords_usadas.append(nueva_keyword)
                texto=texto.replace("#keyword#",keywords_tipo_maquinaria[nueva_keyword],1)      
            i+=1
        return texto
def obten_texto_proyecto_sector():
    with open('plantillas_textos/H2_proyecto_sector.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        cantidad_keywords=texto.find("#keyword#")
        i=0
        keywords_usadas=[]
        while i<cantidad_keywords:
            nueva_keyword=randint(0,len(keywords_proyecto_sector)-1)
            if nueva_keyword not in keywords_usadas:
                keywords_usadas.append(nueva_keyword)
                texto=texto.replace("#keyword#",keywords_proyecto_sector[nueva_keyword],1)      
            i+=1
        return texto
def obten_texto_urgencia_flexibilidad():
    with open('plantillas_textos/urgencia_flexibilidad.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        cantidad_keywords=texto.find("#keyword#")
        i=0
        keywords_usadas=[]
        while i<cantidad_keywords:
            nueva_keyword=randint(0,len(keywords_urgencia_flexibilidad)-1)
            if nueva_keyword not in keywords_usadas:
                keywords_usadas.append(nueva_keyword)
                texto=texto.replace("#keyword#",keywords_urgencia_flexibilidad[nueva_keyword],1)      
            i+=1
        return texto
def obten_texto_provincia(provincia):
    with open('provincia.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        texto=texto.replace("*Provincia*",provincia)
        return texto
    
def obten_texto_municipio(municipio):
    with open('municipio.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        texto=texto.replace("*Municipio*",municipio)
        return texto
    
def crea_texto_ciudad(ciudad):
    lista_keywords=["transaccional","informacional","tipo_maquinaria","proyecto_sector","urgencia"]
    if ciudad in prioridad_maxima:
        cantidad_keywords=5
    elif ciudad in prioridad_media:
        cantidad_keywords=4
    elif ciudad in prioridad_baja:
        cantidad_keywords=3
    else:
        cantidad_keywords=2
        
    i=0
    keywords_usadas=[]
    while i<cantidad_keywords:
        nueva_keyword=lista_keywords[randint(0,len(lista_keywords)-1)]
        if nueva_keyword not in keywords_usadas:
            keywords_usadas.append(nueva_keyword)    
        i+=1
    res=""
    if lista_keywords[0] in keywords_usadas:
        res+=f'{crea_heading(f"Encuentra las mejores {tipo_negocio.lower()} en {ciudad}",2)}'
        res+=f'{crea_parrafo(obten_texto_H2_general("H2_transaccional.txt",keywords_transaccionales,ciudad))}'
    if lista_keywords[1] in keywords_usadas:
        res+=f'{crea_heading(f"Guía para {tipo_negocio.lower()} en {ciudad}",2)}'
        res+=f'{crea_parrafo(obten_texto_H2_general("H2_informacional.txt",keywords_informacionales,ciudad))}'
    if lista_keywords[2] in keywords_usadas:
        res+=f'{crea_heading(f"Tipos de maquinaria disponible en {ciudad}",2)}'
        res+=f'{crea_parrafo(obten_texto_H2_general("H2_tipo_maquinaria.txt",keywords_tipo_maquinaria,ciudad))}'
    if lista_keywords[3] in keywords_usadas:
        res+=f'{crea_heading(f"Maquinaria especializada según tu tipo de proyecto en {ciudad}",2)}'
        res+=f'{crea_parrafo(obten_texto_H2_general("H2_proyecto_sector.txt",keywords_proyecto_sector,ciudad))}'
    if lista_keywords[4] in keywords_usadas:
        res+=f'{crea_heading(f"Alquiler flexible de maquinaria y servicios urgentes en {ciudad}",2)}'
        res+=f'{crea_parrafo(obten_texto_H2_general("H2_urgencia_flexibilidad.txt",keywords_urgencia_flexibilidad,ciudad))}'
    return res
