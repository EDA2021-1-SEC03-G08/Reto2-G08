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
from DISClib.Algorithms.Sorting import mergesort as sa
assert cf

# Construccion de modelos

def newCatalog():
    catalog = {'videos': None,
               'videosIds': None,
               'chennelTitle': None,
               'country': None,
               'views': None,
               'likes': None,
               'categories': None,
               'categoryIds':None}

# Falta completar que tipo de estrutctura elegir
    catalog['videos'] = lt.newList('SINGLE_LINKED')

    catalog['categories'] = lt.newList('SINGLE_LINKED')

    catalog['videosIds'] = mp.newMap(999983, maptype='CHAINING', loadfactor=5, comparefunction=compareMapVideoIds)

    catalog['categoryIds'] = mp.newMap(999983, maptype='CHAINING', loadfactor=5, comparefunction=compareMapCategoryIds)

    catalog['chennelTitle'] = mp.newMap(999983, maptype='CHAINING', loadfactor=5, comparefunction=compareChannelTitle)

    catalog['country'] = mp.newMap(999983, maptype='CHAINING', loadfactor=5, comparefunction=compareCountry)

    catalog['views'] = mp.newMap(999983, maptype='CHAINING', loadfactor=5, comparefunction=compareViews)

    catalog['likes'] = mp.newMap(999983, maptype='CHAINING', loadfactor=5, comparefunction=compareLikes)

    catalog['trending_date'] = mp.newMap(999983, maptype='CHAINING', loadfactor=5, comparefunction=compareTrendingDays)
    
    catalog['countries'] = mp.newMap(999983, maptype='CHAINING', loadfactor=5, comparefunction=compareCountry)
    return catalog




def emptyList():
    return lt.newList('SINGLE_LINKED')

def addCategory(catalog, category):
    lt.addLast(catalog["categories"], category)


def addCountryVideo(catalog, countryName, video):
    countries = catalog['countries']
    if mp.contains(countries, countryName):
        g = mp.get(countries, countryName)
        country = me.getValue(g) 
    else:
        country = newCountry(countryName)
        mp.put(countries, countryName, country)
    lt.addLast(country['videos'], video)


def addCategoryIdVideo(catalog, categoryId, video):
    catego = catalog['categoryIds']
    if mp.contains(catego, categoryId):
        g= mp.get(catego, categoryId)
        category = me.getValue(g) 
    else:
        category = newCategory(categoryId)
        mp.put(catego, categoryId, category)
    lt.addLast(category['videos'],video)


def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    mp.put(catalog['videosIds'], video['video_id'], video)
    channels = video['channel_title'].split(",")  
    country = video['country']
    categoryId = video["category_id"]
    addCountryVideo(catalog, country, video)
    addCategoryIdVideo(catalog, categoryId, video)
    for channel in channels:
        addChannel(catalog, channel.strip(), video)
    

def addPublishTime(catalog, video):

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

    channels = catalog['chennelTitle']
    existauthor = mp.contains(channels, channel)
    if existauthor:
        entry = mp.get(channels, channel)
        author = me.getValue(entry)
    else:
        author = newChannel(channel)
        mp.put(channels, channel, author)
    lt.addLast(author['videos'], video)


def newChannel(channelName):
    channel = {'name': "",
              "videos": None,
              "likes": 0}
    channel['name'] = channelName
    channel['videos'] = lt.newList('SINGLE_LINKED', compareChannelTitle)
    return channel


def newCountry(countryName):
    country={'nameCo':"","videos":None}
    country['nameCo'] = countryName
    country['videos'] = lt.newList('ARRAY_LIST', compareCountry)
    return country


def newCategory(catId):
    category = {'id':0, "videos":None}
    category['id'] = catId
    category['videos'] = lt.newList('ARRAY_LIST', compareCountries)
    return category


def getFirstVideo(catalog):
    return lt.firstElement(catalog['videos'])


def getCountry(catalog, countryName):
    countryN = mo.get(catalog["countries"], countryName)
    if countryN == countryName:
        return me.getValue(countryN) 
    return None


def getCategory(catalog, categoryId):
    category = mp.get(catalog['categoryIds'], categoryId)
    if category:
        return me.getValue(category)
    return None

def getVideosByCountry(catalog, country):
    countryList = mp.get(catalog['videos'], country)
    if countryList:
        return me.getValue(countryList)
    return None

###
def getTrendingDays(video, catalog):
    lstt = emptyList()
    counter = 0
    for i in lt.iterator(catalog['videos']):
        if i['video_id']==video['video_id']:
            t = i['trending_date']
            if t not in lstt:
                lt.addLast(lstt, t)
                counter=+1
    return(counter)


# Funciones utilizadas para comparar elementos dentro de una lista
def compareLikes(video1, video2):
    return (int(video1['likes']) > int(video2['likes']))

def compareViews(video1, video2):
    return (int(video1['views']) > int(video2['views']))


def compareMapVideoIds(key, param):
    tagentry = me.getKey(param)
    if (int(key) == int(tagentry)):
        return 0
    elif (int(key) > int(tagentry)):
        return 1
    else:
        return 0


def compareMapCategoryIds(cid,param):
    tagentry = me.getKey(param)
    if (int(cid) == int(tagentry)):
        return 0
    elif (int(cid) > int(tagentry)):
        return 1
    else:
        return 0

def compareChannelTitle(keyname, channelTitle):
    name = me.getKey(channelTitle)
    if (keyname == name):
        return 0
    elif (keyname > name):
        return 1
    else:
        return -1

def compareCountry(k1, c2):
    country = me.getKey(c2)
    if (int(k1) == int(country)):
        return 0
    elif (int(k1) > int(country)):
        return 1
    else:
        return -1

def compareDislikes(l1,l2):
    if (int(l1) == int(l2)):
        return 0
    elif (int(l1) > int(l2)):
        return 1
    else:
        return 0

def comparePublishTime(vid, t):
    entry = me.getKey(t)
    if (vid == entry):
        return 0
    elif (vid > entry):
        return 1
    else:
        return 0

def compareTrendingDays(d1, d2):
    if (int(d1) == int(d2)):
        return 0
    elif (int(d1) > int(d2)):
        return 1
    else:
        return 0
  
def sortVideosByTrendingDays(catalog):
    lst = catalog['videos']
    sa.sort(lst, compareTrendingDays)
    return lst


def sortVideosByLikes(videos):
    lst = catalog['videos']
    sa.sort(lst, compareLikes)
    return lst

def sortVideosByViews(videos):
    lst = videos['videos']
    sa.sort(lst, compareViews)
    return lst