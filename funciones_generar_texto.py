import re
from random import choice,randint

keywords_h1 = [
    "alquiler de maquinaria de construcción",
    "alquiler de maquinaria de obra civil",
    "alquiler de maquinaria pesada",
    "alquiler de maquinaria industrial",
    "alquiler de maquinaria para obra",
    "alquiler de maquinaria para reformas",
    "alquiler de maquinaria para excavaciones",
    "alquiler de maquinaria para movimiento de tierras",
    "alquiler de maquinaria para demolición",
    "alquiler de maquinaria para obras públicas",
    "alquiler de maquinaria para carreteras",
    "alquiler de maquinaria para urbanizaciones",
    "alquiler de maquinaria para proyectos industriales",
    "alquiler de maquinaria para construcción residencial",
    "alquiler de maquinaria para construcción comercial",
    "alquiler de maquinaria para naves industriales",
    "alquiler de maquinaria para infraestructuras",
    "alquiler de maquinaria para ingeniería civil",
    "alquiler de maquinaria para grandes obras",
    "alquiler de maquinaria para pequeñas obras",
    "alquiler de equipos de construcción",
    "alquiler de equipos de obra civil",
    "alquiler de equipos de maquinaria pesada",
    "alquiler profesional de maquinaria de construcción",
    "alquiler profesional de maquinaria industrial",
    "servicios de alquiler de maquinaria de construcción",
    "servicios de alquiler de maquinaria pesada",
    "empresas de alquiler de maquinaria de construcción",
    "empresas de alquiler de maquinaria industrial",
    "empresas de alquiler de maquinaria pesada",
    "empresas de alquiler de maquinaria de construcción",
    "empresas de alquiler de maquinaria industrial",
    "alquiler de maquinaria de construcción",
    "alquiler de maquinaria de obra civil",
    "alquiler de maquinaria pesada",
    "alquiler de equipos industriales para construcción",
    "alquiler de equipos pesados para obra",
    "alquiler de maquinaria para pavimentación",
    "alquiler de maquinaria para cimentaciones",
    "alquiler de maquinaria para túneles",
    "alquiler de maquinaria para puentes",
    "alquiler de maquinaria certificada para obra",
    "alquiler de maquinaria homologada para construcción",
    "alquiler de maquinaria homologada para obra",
    "alquiler de maquinaria certificada para construcción",
    "alquiler de maquinaria especializada para construcción",
    "alquiler de maquinaria para rehabilitación",
    "alquiler de maquinaria para instalaciones",
    "proveedores de alquiler de maquinaria de construcción",
    "proveedores de alquiler de maquinaria de construcción",
    "proveedores de alquiler de maquinaria de obra civil",
    "proveedores de alquiler de maquinaria pesada",
    "proveedores de alquiler de maquinaria industrial",
    "proveedores de alquiler de maquinaria para obra",
    "proveedores de alquiler de maquinaria para reformas",
    "proveedores de alquiler de maquinaria para excavaciones",
    "proveedores de alquiler de maquinaria para movimiento de tierras",
    "proveedores de alquiler de maquinaria para demolición",
    "proveedores de alquiler de maquinaria para obras públicas",
    "proveedores de alquiler de maquinaria para carreteras",
    "proveedores de alquiler de maquinaria para urbanizaciones",
    "proveedores de alquiler de maquinaria para proyectos industriales",
    "proveedores de alquiler de maquinaria para construcción residencial",
    "proveedores de alquiler de maquinaria para construcción comercial",
    "proveedores de alquiler de maquinaria para naves industriales",
    "proveedores de alquiler de maquinaria para infraestructuras",
    "proveedores de alquiler de maquinaria para ingeniería civil",
    "proveedores de alquiler de maquinaria para grandes obras",
    "proveedores de alquiler de maquinaria para pequeñas obras",
    "proveedores de alquiler de equipos de construcción",
    "proveedores de alquiler de equipos de obra civil",
    "proveedores de alquiler de equipos de maquinaria pesada",
]

keywords_transaccionales = [
    "alquiler de excavadoras por días",
    "empresas de alquiler de grúas telescópicas",
    "alquiler maquinaria construcción precio económico",
    "renta de retroexcavadoras para obra",
    "alquiler plataformas elevadoras con operario",
    "alquiler compactadoras vibratorias fin de semana",
    "dónde alquilar dumpers para construcción",
    "empresas alquiler maquinaria pesada cerca de mí",
    "alquiler maquinaria industrial por horas",
    "presupuesto alquiler excavadora con transporte",
    "alquiler de palas cargadoras baratas",
    "empresas alquiler camiones volquete",
    "alquiler torres de iluminación para obra",
    "renta de montacargas diesel",
    "alquiler minicargadoras bobcat",
    "alquiler de apisonadoras manuales",
    "compañías alquiler equipos demolición",
    "alquiler manipuladoras telescópicas construcción",
    "renta de sierras de pavimento",
    "alquiler bombas de hormigón autopropulsadas",
    "alquiler fresadoras para asfalto",
    "empresas alquiler compresores aire industrial",
    "alquiler zanjadoras para instalaciones",
    "renta de niveladoras láser topográficas",
    "alquiler grupos electrógenos silenciosos obra",
    "alquiler carros de obra autopropulsados",
    "empresas renta maquinaria forestal",
    "alquiler cortadoras de hormigón profesionales",
    "renta de equipos perforación horizontal",
    "alquiler pisones compactadores gasolina",
    "alquiler camiones grúa certificados",
    "empresas alquiler cisternas para agua",
    "renta de plataformas tijera eléctricas",
    "alquiler minicargadoras orugas construcción",
    "alquiler cortadoras juntas pavimento",
    "empresas renta equipos hidrolimpieza industrial",
    "alquiler vibradores hormigón eléctricos",
    "renta de motoniveladoras 140 hp",
    "alquiler dumpers articulados todo terreno",
    "empresas alquiler mezcladoras hormigón"
]

keywords_informacionales = [
    "cuánto cuesta alquilar una grúa torre",
    "las mejores empresas de alquiler de maquinaria de construcción",
    "qué maquinaria necesito para una excavación",
    "cual es el precio del alquiler mensual de una excavadora de 20 toneladas",
    "los requisitos para alquilar maquinaria pesada en España",
    "la diferencia entre alquilar y comprar maquinaria industrial",
    "cómo elegir empresa de alquiler de equipos de construcción",
    "la documentación necesaria para el alquiler de maquinaria de construcción",
    "los seguros incluidos en el alquiler de maquinaria industrial",
    "el mantenimiento de la maquinaria de alquiler para construcción",
    "las ventajas del alquiler de maquinaria frente a compra",
    "cuánto cuesta alquilar una excavadora cada semana",
    "qué incluye el alquiler de maquinaria industrial",
    "una comparativa de precios de alquiler de grúas",
    "la normativa del alquiler de maquinaria pesada en España",
    "cuándo conviene alquilar o comprar equipos construcción",
    "los seguros obligatorios de maquinaria de alquiler para obras",
    "las certificaciones necesarias para operar maquinaria alquilada",
    "las tarifas de alquiler de maquinaria de construcción en 2025",
    "el mantenimiento preventivo de equipos de alquiler para construcción",
    "las responsabilidades en un contrato de alquiler de maquinaria industrial",
    "las diferencias en el alquiler de maquinaria con sin operador",
    "las inspecciones técnicas de la maquinaria de alquiler",
    "qué revisar antes de alquilar una excavadora",
    "las cláusulas importantes en un contrato de alquiler de equipos",
    "los periodos mínimos alquiler maquinaria pesada",
    "las garantías a exigir a la empresa de alquiler de maquinaria",
    "el comparador de empresas de alquiler de equipos de construcción",
    "las opiniones sobre las empresas de alquiler de maquinaria",
    "el checklist para alquilar maquinaria de construcción de manera segura",
    "los costes ocultos del alquiler de maquinaria industrial",
    "la diferencia entre renting y alquiler de maquinaria",
    "los impuestos aplicables añ alquiler de equipos de construcción en España",
    "las bonificaciones al alquiler de largo plazo de maquinaria",
    "la flexibilidad de los contratos de alquiler de equipos industriales",
    "los plazos de entrega de la maquinaria en alquiler",
    "la disponibilidad de maquinaria en temporada alta de la construcción",
    "los servicios adicionales de las empresas de alquiler de equipos",
    "si el transporte está incluido en el precio del alquiler de maquinaria",
    "la formación necesaria de los operadores de maquinaria alquilada"
]

keywords_tipo_maquinaria = [
    "el alquiler de miniexcavadoras para jardines",
    "la renta de bulldozers para movimiento de tierras",
    "el alquiler de carretillas elevadoras eléctricas",
    "el alquiler de hormigoneras industriales de gran capacidad",
    "el alquiler de motoniveladora para caminos rurales",
    "el alquiler de martillos hidráulicos para demolición",
    "la renta de equipos de pavimentación asfáltica",
    "el alquiler de generadores eléctricos para obra",
    "el alquiler de andamios metálicos certificados",
    "el alquiler de rodillos compactadores autopropulsados",
    "el alquiler de tractores oruga para el movimiento de tierras",
    "la renta de excavadoras hidráulicas de 30 toneladas",
    "el alquiler de plataformas articuladas diesel",
    "el alquiler de perforadoras neumáticas para demolición",
    "la renta de compactadores placa vibrante",
    "el alquiler de grúas autopropulsadas de 50 metros",
    "el alquiler de mezcladoras de cemento portátiles",
    "la renta de equipos de izaje de cargas pesadas",
    "el alquiler de rozadoras para túneles",
    "el alquiler de equipos de cribado de áridos",
    "la renta de dragas para excavación fluvial",
    "el alquiler de cargadoras frontales con ruedas",
    "el alquiler de extendedoras asfalto autopropulsadas",
    "la renta de equipos de sondeo geotécnico",
    "el alquiler de camiones hormigonera de 8m3",
    "el alquiler de equipos para el hincado de pilotes",
    "la renta de barredoras industriales autopropulsadas",
    "el alquiler de cintas transportadoras de materiales",
    "el alquiler de torres andamio móviles de aluminio",
    "la renta de equipos de pulido de hormigón",
    "el alquiler de bombas de achique de aguas residuales",
    "el alquiler de trituradoras de residuos construcción",
    "la renta de equipos de soldadura industrial",
    "el alquiler de remolques basculantes de carga",
    "el alquiler de grúas de pluma articulada",
    "la renta de equipos de ventilación obras subterráneas",
    "el alquiler de mesas vibrantes prefabricadas",
    "el alquiler de equipos de asfaltado en caliente",
    "la renta de plataformas elevadoras con brazo telescópico",
    "el alquiler de equipos de compactación suelos"
]

keywords_proyecto_sector = [
    "alquiler de maquinaria de excavación de sótanos",
    "alquiler de equipos industriales para la construcción de puentes",
    "alquiler de maquinaria para instalaciones solares",
    "alquiler de equipos de construcción de túneles",
    "alquiler de maquinaria industrial para obras hidráulicas",
    "alquiler de equipos de construcción de aparcamientos",
    "alquiler de maquinaria pesada para la construcción de aeropuertos",
    "alquiler de equipos de urbanización de jardines",
    "alquiler de maquinaria industrial para la construcción de hospitales",
    "alquiler de equipos obras marítimas portuarias",
    "alquiler de maquinaria para la construcción de instalaciones deportivas",
    "alquiler de equipos de rehabilitación de edificios históricos",
    "alquiler de maquinaria industrial para la construcción de centros comerciales",
    "alquiler de equipos de instalación de tuberías",
    "alquiler de maquinaria para la construcción de plantas industriales",
    "alquiler de equipos de cimentaciones especiales",
    "alquiler de maquinaria industrial para la construcción de depuradoras",
    "alquiler de equipos obras ferroviarias",
    "alquiler de maquinaria para la construcción de parques eólicos",
    "alquiler de equipos de acondicionamiento de terrenos",
    "alquiler de maquinaria industrial para el desmonte y explanaciones",
    "alquiler de equipos para la construcción de presas y embalses",
    "alquiler de maquinaria para la construcción de gasolineras",
    "alquiler de equipos para obras de alcantarillado",
    "alquiler de maquinaria industrial para la pavimentación de parkings",
    "alquiler de equipos para la construcción de muros contención",
    "alquiler de maquinaria para obras de canalización de redes",
    "alquiler de equipos construcción de rotondas",
    "alquiler de maquinaria industrial para demoliciones controladas",
    "alquiler de equipos para la construcción de hoteles",
    "alquiler de maquinaria para reformas de edificios",
    "alquiler de equipos industriales para la construcción de piscinas",
    "alquiler de maquinaria para proyectos agrícolas",
    "alquiler de equipos de movimiento tierras para urbanización",
    "alquiler de maquinaria industrial para obras públicas",
    "alquiler de maquinaria de construcción para naves industriales",
    "alquiler de equipos alquiler para rehabilitación de fachadas",
    "alquiler de maquinaria pesada para construcción de carreteras y autopistas",
    "alquiler de equipos construcción para viviendas unifamiliares",
    "alquiler de maquinaria para polígonos industriales"
]

keywords_urgencia_flexibilidad = [
    "alquiler de maquinaria de construcción con entrega inmediata",
    "alquiler de maquinaria industrial sin permanencia",
    "alquiler de equipos disponibles en 24 horas",
    "alquiler de maquinaria de construcción para corto plazo",
    "alquiler de maquinaria pesada con el servicio técnico incluido",
    "alquiler de equipos industriales con seguro a todo riesgo",
    "alquiler de maquinaria con mantenimiento incluido",
    "alquiler de maquinaria de construcción con transporte gratis",
    "alquiler de equipos industriales con contratos flexibles",
    "alquiler de maquinaria pesada con operador certificado",
    "alquiler de maquinaria de construcción en el último minuto",
    "alquiler de equipos de servicio 7 días",
    "alquiler de maquinaria pesada con cancelación gratis",
    "alquiler de equipos industriales sin depósito",
    "alquiler de maquinaria con facturación inmediata",
    "alquiler de maquinaria de construcción con pago aplazado",
    "alquiler de equipos industriales con contrato mensual",
    "alquiler de maquinaria pesada sin compromiso",
    "alquiler de equipos con reposición garantizada",
    "alquiler de maquinaria de construcción con entrega los sábados",
    "alquiler de equipos industriales con soporte telefónico 24h",
    "alquiler de maquinaria pesada con reserva online",
    "alquiler de equipos con descuento en largo plazo",
    "alquiler de maquinaria de construcción con tarifa cerrada",
    "alquiler de equipos industriales con ampliación del periodo",
    "alquiler de maquinaria pesada con recambios incluidos",
    "alquiler de equipos con asistencia técnica urgente",
    "alquiler de maquinaria de construcción sin gastos ocultos",
    "alquiler de equipos industriales con formación incluida",
    "alquiler de maquinaria pesada con devolución flexible",
    "alquiler de equipos con inspección previa",
    "alquiler de maquinaria de construcción con renovación automática",
    "alquiler de equipos industriales con carburante incluido",
    "alquiler de maquinaria pesada con servicio recogida",
    "alquiler de equipos con descuento para nuevos clientes",
    "alquiler de maquinaria de construcción en paquetes para obra",
    "alquiler de equipos industriales con precio todo incluido",
    "alquiler de maquinaria pesada con contratos temporada",
    "alquiler de equipos con bonos prepago",
    "alquiler de maquinaria de construcción con operador bilingüe"
]



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