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
 """

import config as cf
import model
import csv

# Inicialización del Catálogo 
def initCatalog():

    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

def newCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    loadVideos(catalog)
    loadCategories(catalog)

def loadVideos(catalog):
    videoFile = cf.data_dir+'videos-small.csv'
    inputFile = csv.DictReader(open(videoFile, encoding="utf-8"))
    for video in inputFile:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    categoryFile = cf.data_dir+'category-id.csv'
    inputFile = csv.DictReader(open(categoryFile, encoding="utf-8"))
    for category in inputFile:
        model.addCategory(catalog, category)

# Funciones de consulta sobre el catálogo

def getFirstVideo(catalog):
    return model.getFirstVideo(catalog)

def getMostLikedVideos(catalog, country, tag, top):
    counter = 0
    lst = model.sortVideosByLikes(catalog)
    emptyLst = model.emptyList()
    for video in lt.iterator(lst):
        if(counter <= int(top)):
            if(video['country'] == country):
                hasTag = False
                for tagItem in video['tags'].split('|'):
                    finalTag = tagItem.replace('"', "")
                    if(finalTag == tag):
                        hasTag = True
                if(hasTag):
                    lt.addLast(emptyLst, video)
                    counter = 1+counter
    return emptyLst

# Por categoria y pais
def getMostViewedVideos(catalog, country, categoryId, top):
    counter = 0
    lst = model.sortVideosByViews(catalog)
    emptyLst = model.emptyList()
    for video in lt.iterator(lst):
        if(counter < int(top)):
            if(video['country'] == country and video['category_id'] == categoryId):
                lt.addLast(emptyLst, video)
                counter = 1 + counter
    return emptyLst

