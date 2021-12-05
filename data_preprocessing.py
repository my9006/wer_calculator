import os
import glob


def pre_process(directory):
    cases = os.listdir(directory)
    warehouse = {}
    for i in cases:
        item = {}
        with open(glob.glob(directory + "/" + i + "/*txt")[0]) as file:
            text = file.readline()
            item['text'] = text
        audio = glob.glob(directory + "/" + i + "/*flac")[0]
        item['audio'] = audio
        warehouse[i] = item
    return warehouse
