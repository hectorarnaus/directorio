from pixabay_python import PixabayClient, Category, download,ImageOrientation

import os
from random import randint
from google_images_search import GoogleImagesSearch

def obten_nombre_fichero(url):
    datos=url.split("/")
    return datos[-1]


#https://pypi.org/project/Google-Images-Search/
def obten_imagen_google(nombre,carpeta):
    gis = GoogleImagesSearch("AIzaSyD8Gxqlbw9uVepbvc6tx4j7L-TvfqHQAXw","429c521e05e754bd1")
    _search_params = {
        'q': nombre,
        'num': 10,
        'fileType': 'jpg',
        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
        'imgSize': 'xlarge',
        'imgDominantColor': 'imgDominantColorUndefined',
        'imgColorType': 'color'
    }

    gis.search(search_params=_search_params)
    ficheros=[]
    for image in gis.results():
        image.url  # image direct url
        image.referrer_url  # image referrer url (source) 
        
        image.download(carpeta)  # download image
        ficheros.append(image.path)
    i=0
    if len(ficheros)==0:
        return False
    while i<len(ficheros):
       # print(i)
       # print(ficheros[i])
        os.rename(ficheros[i],carpeta+"/"+nombre+str(i)+".jpg")
        i+=1
    return True
  



def obten_imagen_pixabay(nombre,carpeta):
    client = PixabayClient(apiKey="50941131-9e334548d8a355bbadf6f5388")
    searchResult = client.searchImage(q=nombre,category=Category.PLACES)
    hitsList = list(searchResult.hits)
    if len(hitsList)>0:
        i=0
        while i<len(hitsList) and i<10:
            download(url=hitsList[i].largeImageURL, outputDir=carpeta)
            fichero=obten_nombre_fichero(hitsList[i].largeImageURL)
            os.rename(carpeta+"/"+fichero,carpeta+"/"+nombre+str(i)+".jpg")
            i+=1
        return True
    return False


if obten_imagen_pixabay("Soneja","img")==False:
    obten_imagen_google("Soneja","img")