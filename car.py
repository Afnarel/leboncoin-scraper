# -*- coding: utf-8 -*-
from utils import javascript_array_to_python
import sys


class Car(object):
    def __init__(self, item_url, data):
        self.item_url = item_url
        self.data = data

    def ad_number(self):
        print self.item_url

    def serialize(self):
        body = self.data.find('body')
        script_elt = str(body.findAll('script')[0])
        p1 = script_elt.index('{')
        p2 = script_elt.index('}') + 1
        object_data = script_elt[p1:p2]
        return javascript_array_to_python(object_data)

    def save(self):
        try:
            print self.serialize()
        except:
            print self.ad_number()
            print "%s: %s" % (sys.exc_info()[0], sys.exc_info()[1])

    def __str__(self):
        return 'Toto'
