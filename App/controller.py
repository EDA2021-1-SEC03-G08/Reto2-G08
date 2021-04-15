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
import time
import tracemalloc
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
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadVideos(catalog)
    loadCategories(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory

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

def getVideoWithMostTrendingDaysByCountry(catalog, country):
    lst = model.sortVideosByTrendingDays(catalog)
    for vid in lt.iterator(lst):
        if(vid['country'] == country):
            return vid

def getVideoWithMostTrendingDaysByCategory(catalog, categoryId):
    lst = model.sortVideosByTrendingDays(catalog)
    for video in lt.iterator(lst):
        if(video['category_id'] == categoryId):
            return video


def getTrendingDays(video):
    return model.getTrendingDays(video)

def getTime():
    
    return float(time.perf_counter()*1000)


def getMemory():
   
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
  
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff

    delta_memory = delta_memory/1024.0
    return delta_memory