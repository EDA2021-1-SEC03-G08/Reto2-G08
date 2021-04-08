"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Top videos por categoria en un pais")
    print("3- Videos con mas likes")
    print("4- Videos con mas likes por pais")

    
"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ...")
        catalog = controller.newCatalog()
        controller.loadData(catalog)
        print("Videos cargados " + str(lt.size(catalog["videos"])) + " videos")
        firstElement = controller.getFirstVideo(catalog)
        print("Info primer video")
        print("title: " + firstElement["title"])
        print("channel_title: " + firstElement["channel_title"])
        print("country: " + firstElement["country"])
        print("views: " + firstElement["views"])
        print("likes: " + firstElement["likes"])
        print("Categories")

        for category in lt.iterator(catalog["categories"]):
            print(category['name'] + ": " + category['id'])
    elif int(inputs[0]) == 2:
        category = input('Ingrese la categoria (category_id):\n')
        country = input('Ingrese el pais :\n')
        top = input('Numeros de videos a colocar:\n')
        videosByCountry = controller.getMostViewedVideos (catalog, country, category, top)
        for video in lt.iterator(videosByCountry):
            print('trending_date: ' + video['trending_date'])
            print('title: ' + video['title'])
            print('publish_time: ' + video['publish_time'])
            print('views: ' + video['views'])
            print('likes: ' + video['likes'])

    elif int(inputs[0]) == 3:
        top = input('Cantidad de videos a colocar:\n')
        videos = controller.getMostLikedVideos(catalog, top)
        for video in lt.iterator(videos):
            print("Title: " + video['title'])
            print("channel_title: " + video['channel_title'])
            print("views: " + video['views'])
            print("likes: " + video['likes'])
            print("tags: " + video['tags'])
            print("publish_time: " + video['publish_time'])

    elif int(inputs[0]) == 4:
        country = input('Ingrese el pais (country):\n')
        tag = input('Ingrese el tag:\n')
        top = input('Numeros de videos a listar:\n')
        videosTag = controller.getMostLikedVideosByCountryAndTag(
            catalog, country, tag, top)
        for video in lt.iterator(videosTag):
            print("Title: " + video['title'])
            print("channel_title: " + video['channel_title'])
            print("views: " + video['views'])
            print("likes: " + video['likes'])
            print("dislikes: " + video['dislikes'])
            print("publish_time: " + video['publish_time'])
            print("tags: " + video['tags'])
    else:
        sys.exit(0)
sys.exit(0)
