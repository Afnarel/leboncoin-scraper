# -*- coding:utf-8 -*-

from urllib2 import urlopen
from bs4 import BeautifulSoup


CATEGORIES = ['voitures']


class Car(object):
    def __init__(self):
        pass

    def __str__(self):
        return 'Toto'


def build_voitures(data):
    return Car()


def browse(url):
    category = url.split('/')[3]
    if category not in CATEGORIES:
        raise Exception("Wrong URL: category '%s' does not exist" % category)
    # Browse each page using the navigation links at the bottom
    while True:
        page = urlopen(url)
        data = BeautifulSoup(page.read())
        nav = data.find('ul', id='paging')
        current = nav.find('li', class_='selected').text.strip()
        nb_pages_link = nav.findAll('li')[-1].a
        if nb_pages_link:
            href = nb_pages_link.get('href')
            nb_pages = href.split('=')[-1]
        else:
            nb_pages = current
        #####
        print "Processing page %s of %s: %s" % (current, nb_pages, url)
        liste = data.find('div', class_='list-lbc')
        # In each page browse each item link and create a
        for link in liste.findAll('a'):
            item_url = link.get('href')
            item_page = urlopen(item_url)
            item_data = BeautifulSoup(item_page.read())
            yield globals()['build_%s' % category](item_data)
        #####
        next_page_link = nav.findAll('li', class_='page')[1].a
        if not next_page_link:
            break
        url = next_page_link.get('href')


if __name__ == '__main__':
    URL = 'http://www.leboncoin.fr/voitures/'
    for car in browse(URL):
        print car
