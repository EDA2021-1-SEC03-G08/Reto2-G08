"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
     catalog = {'videos': None,
               'videosIds': None,
               'chennelTitle': None,
               'country': None,
               'views': None,
               'likes': None,
               'dislikes': None
               'publishTime': None
               'categories': None}

# Falta completar que tipo de estrutctura elegir
    catalog['videos'] = lt.newList('SINGLE_LINKED', compareVideosIds)
    catalog['categories'] = lt.newList()
    catalog['videosIds'] = mp.newMap(100000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareMapVideosIds)
    catalog['chennelTitle'] = mp.newMap(100000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareChannelTitle)                                                
    catalog['country'] = mp.newMap(100000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareCountry)
    catalog['views'] = mp.newMap(100000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareViews)
    catalog['likes'] = mp.newMap(100000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareLikes)
    catalog['dislikes'] = mp.newMap(100000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareDislikes)
    catalog['publish_time'] = mp.newMap(100000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=comparePublishTime)       
    catalog['trending_date'] = mp.newMap(100000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareTrendingDate)
    return catalog

# Funciones para agregar informacion al catalogo

def emptyList():
    return lt.newList('ARRAY_LIST')

def addCategory(catalog, category):
    lt.addLast(catalog["categories"], category)

def addVideo(catalog, video):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['videos'], video)
    mp.put(catalog['videosIds'], video['video_id'], video)
    channels = video['channel_title'].split(",")  
    for channel in channels:
        addChannel(catalog, channel.strip(), video)
    addPublishTime(catalog, video)

def addPublishTime(catalog, video):
    """
    Esta funcion adiciona un libro a la lista de libros que
    fueron publicados en un año especifico.
    Los años se guardan en un Map, donde la llave es el año
    y el valor la lista de libros de ese año.
    """
    try:
        pTime = catalog['publishTime']
        if (video['publish_time'] != ''):
            pubyear = video['publish_time']
            pubyear = int(float(pubyear))
        else:
            pubyear = 2020
        existyear = mp.contains(pTime, pubyear)
        if existyear:
            entry = mp.get(pTime, pubyear)
            year = me.getValue(entry)
        else:
            year = newYear(pubyear)
            mp.put(pTime, pubyear, year)
        lt.addLast(year['videos'], video)
    except Exception:
        return None

def addChannel(catalog, channel, video):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    channels = catalog['chennelTitle']
    existauthor = mp.contains(channels, channel)
    if existauthor:
        entry = mp.get(channels, channel)
        author = me.getValue(entry)
    else:
        author = newChannel(channel)
        mp.put(channels, channel, author)
    lt.addLast(author['videos'], video)
   
# Funciones para creacion de datos
def newChannel(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings. Se crea una lista para guardar los
    libros de dicho autor.
    """
    channel = {'name': "",
              "videos": None,
              "likes": 0,
              }
    channel['name'] = name
    channel['videos'] = lt.newList('SINGLE_LINKED', compareChannelTitle)
    return channel
# Funciones de consulta

def getFirstVideo(catalog):
    return lt.firstElement(catalog["videos"])

def getVideosByCountry(catalog, country):
    countryList = mp.get(catalog['videos'], country)
    if countryList:
        return me.getValue(countryList)
    return None


# Funciones utilizadas para comparar elementos dentro de una lista
def compareLikes(video1, video2):
    return (int(video1['likes']) > int(video2['likes']))

def compareViews(video1, video2):
    return (int(video1['views']) > int(video2['views']))

def sortVideosByLikes(catalog):
    lst = catalog['videos']
    sa.sort(lst, compareLikes)
    return lst

def sortVideosByViews(catalog):
    lst = catalog['videos']
    sa.sort(lst, compareViews)
    return lst