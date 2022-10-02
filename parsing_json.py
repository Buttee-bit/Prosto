import imp
import json
import random
import requests as R
import numpy as np

def open_js(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def list_keys(jsons):
    list_key = [i for i in jsons.keys()]
    return list_key


def random_key(jsons, list_key):
    init = 4
    rand_min = 0
    rand_max = len(list_key)-1
    disct_answer = {}
    for i in range(init):
        random_integer = random.randint(rand_min, rand_max)
        disct_answer[list_key[random_integer]
                     ] = jsons[list_key[random_integer]]
    return disct_answer



def download_Photos(listURLs):
    intCount = 1
    list_img = []
    for strURL in listURLs:
        with open(r'static\\shift' + '\\' + str(intCount) + '.jpg', 'wb') as file:
            img = R.get(strURL)
            file.write(img.content)
        intCount += 1


def main(path):
    name_ = path.split('.')[0]
    print(name_)
    full_path = name_ + '.json'
    open_js_ = open_js(full_path)
    list_keys_ = list_keys(open_js_)
    answer = random_key(open_js_, list_keys_)
    download_Photos(answer.values())

