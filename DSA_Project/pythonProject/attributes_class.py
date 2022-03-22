import math
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
import random
import time

import Compare
import counting_sort
import insertion_sort
import merge_sort
import quick_sort
import selection_sort
import heap_sort
import radix_sort
import bubble_sort

from tkinter import ttk





x_main = []
y_main = []

n = 5000
def radix_notation(Tj):
    temp = 0
    c = 10
    for i in range(n):
        # if temp**2 >= Tj:
        # break
        x_main.append(temp)
        y_main.append(3*(c+100))
        c+=50
        temp = temp + 1
    return x_main, y_main

def x_power_2(Tj):
    temp = 0
    for i in range(n):
        #if temp**2 >= Tj:
            #break
        x_main.append(temp)
        y_main.append(temp**2)
        temp = temp + 1
    return x_main, y_main

def x_log_x(Tj):
    temp = 1

    for i in range(n):
        #if temp*b >=Tj:
           #break
        x_main.append(temp)
        a = math.log(temp,2)
        y_main.append(temp*a)
        temp = temp + 1
    return x_main, y_main

class attributes:
    arr = []
    temp_arr = []
    Name = ''
    def plot_graph(self,x_axis, y_axis,name,Tj):
        plt.plot(x_axis, y_axis,label=name)
        #notation for x^2
        if name == 'Insertion' or name == 'Bubble' or name =='Selection':
            x, y = x_power_2(Tj)
            plt.plot(x, y, label='N^2 notation')
            x.clear()
            y.clear()
        #notation for n log n
        if name == 'Heap' or name =='Quick' or name =='Merge':
            x,y = x_log_x(Tj)
            plt.plot(x,y,label='nlog(n) notation')
            x.clear()
            y.clear()
        if name == 'Radix':
            x,y = radix_notation(Tj)
            plt.plot(x, y, label='d(n+b)')
            x.clear()
            y.clear()

        plt.xlabel('x-axis  n Numbers')
        plt.ylabel('y-axis  time taken by each n')
        plt.title(name + ' Sort')
        plt.legend()
        plt.show()
        x_axis.clear()
        y_axis.clear()
        name = ''

    def plot_graph_compare(self,x_axis1,y_axis1,name1,x_axis2,y_axis2,name2):
        plt.plot(x_axis1, y_axis1,label=name1)
        plt.plot(x_axis2, y_axis2,label=name2)
        plt.xlabel('x-axis  n Numbers',)
        plt.ylabel('y-axis  time taken by each n')

        plt.title('Compare '+name1 + ' & ' + name2 + ' Sorting Algorithms')
        plt.legend()
        plt.show()
        x_axis1.clear()
        y_axis1.clear()
        name1 = ''
        x_axis2.clear()
        y_axis2.clear()
        name2 = ''

    def start(self):
        file = open("Numbers", "w")
        self.Random_Numbers(self.temp_arr)
        self.save_rand_in_file(file, self.temp_arr)
        file.close()

    def Random_Numbers(self, temp_arr):
        for i in range(10000):
            num = random.randint(1, 100)
            temp_arr.append(num)

    def save_rand_in_file(self, file, temp_arr):
        for i in range(len(temp_arr)):
            file.write("%d\n" % temp_arr[i])

    def readFile(self):
        fileObj = open("Numbers", "r")  # opens the file in read mode
        words = fileObj.read().splitlines()  # puts the file into an array
        fileObj.close()
        return words


    def calculate(self,Name):

        n = 10
        arr = []
        x_axis=[]
        y_axis=[]
        temp = self.readFile()
        for i in range(0, 100):
            arr.clear()
            if n >= 5000:
                break
            #fill arr from the file

            for x in range(0,n):
                arr.append(temp[x])
            if(Name == 'Insertion'):
                Tj = 0
                Tj = insertion_sort.insertionSort(arr,Tj)
            elif(Name == 'Merge'):
                Tj = 0
                Tj = merge_sort.mergeSort(arr, Tj)
            elif(Name == 'Selection'):
                Tj=0
                Tj = selection_sort.selcetionSort(arr,Tj)
            elif (Name == 'Radix'):
                Tj=0
                Tj = radix_sort.radixSort(arr, Tj)
            elif(Name == 'Heap'):
                Tj = 0
                Tj = heap_sort.heapSort(arr, Tj)
            elif (Name == 'Bubble'):
                Tj = 0
                Tj = bubble_sort.bubbleSort(arr, Tj)
            elif (Name == 'Quick'):
                Tj = 0
                Tj = quick_sort.quickSort(arr,0,len(arr)-1, Tj)


            x_axis.append(n)
            y_axis.append(Tj)
            n = n + 50

        return x_axis,y_axis,Tj





