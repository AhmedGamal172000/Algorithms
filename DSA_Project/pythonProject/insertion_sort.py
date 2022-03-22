import random
import time
from tkinter import *
from PIL import Image
from PIL import ImageTk
import matplotlib.pyplot as plt
import numpy as np

import attributes_class
import Compare
import Generate_rand


def insertionSort(arr,Tj):
    Tj += 1
    for i in range(1, len(arr)):
        Tj += 2
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            Tj += 2
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        Tj+=1
    return Tj


def main_insertion():

    ins = attributes_class.attributes()
    ins.Name = 'Insertion'
    if (Generate_rand.counter == 1):
        ins.start()
    x_axis,y_axis,Tj = ins.calculate(ins.Name)
    ins.plot_graph(x_axis, y_axis, ins.Name,Tj)


def main_insertion_compare():
    ins = attributes_class.attributes()
    ins.Name = 'Insertion'
    if (Generate_rand.counter == 1):
        ins.start()
    x_axis,y_axis, Tj = ins.calculate(ins.Name)
    Compare.compare(x_axis,y_axis,ins.Name)

    return 1


