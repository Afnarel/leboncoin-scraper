# -*- coding: utf-8 -*-


def javascript_array_to_python(array):
    dic = {}
    liste = array[1:-1].split(",")
    for it in liste:
        k, v = it.split(":")
        dic[k.strip()] = v.strip()[1:-1]
    return dic
