# -*- coding: utf-8 -*-
from utils import javascript_array_to_python


class Car(object):
    def __init__(self, item_url, data):
        self.item_url = item_url
        self.data = data
        self.serialized_data = None

    def ad_number(self):
        p1 = self.item_url.rindex("/") + 1
        p2 = self.item_url.index(".htm")
        return self.item_url[p1:p2]

    def serialize(self):
        body = self.data.find('body')
        script_elt = str(body.findAll('script')[0])
        p1 = script_elt.index('{')
        p2 = script_elt.index('}') + 1
        object_data = script_elt[p1:p2]
        self.serialized_data = javascript_array_to_python(object_data)

    def save(self):
        print self.serialized_data
