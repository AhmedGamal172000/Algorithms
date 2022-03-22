from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import numpy as np
import matplotlib.pyplot as plt
import turtle

import insertion_sort
import merge_sort
from insertion_sort import main_insertion
from insertion_sort import main_insertion_compare
from merge_sort import main_merge
from merge_sort import main_merge_compare
from selection_sort import main_selection
from selection_sort import main_selection_compare
from heap_sort import main_heap
from heap_sort import main_heap_compare
from bubble_sort import main_bubble
from bubble_sort import main_bubble_compare
from quick_sort import main_quick
from quick_sort import main_quick_compare
from counting_sort import main_counting
from counting_sort import main_counting_compare
from radix_sort import main_radix
from radix_sort import main_radix_compare
from Generate_rand import Generate
import threading

root = Tk()
root.title("Sorting algorithm")
root.geometry("600x480")
root.config(bg="#E5DCFC")




def page1():

    def page_compare_sort():
        label_welcome.destroy()
        btn_single.destroy()
        btn_compare.destroy()
        def back():
            label1.destroy()
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
            btn4.destroy()
            btn6.destroy()
            btn7.destroy()
            btn8.destroy()
            btn_create_random.destroy()
            btn_back.destroy()
            page1()

        def ins():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_insertion_compare)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()

        def merg():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_merge_compare)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()

            window.mainloop()

        def sel():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_selection_compare)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()

        def he():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_heap_compare)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()

        def rad():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_radix_compare)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()

        def bub():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_bubble_compare)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()

        def qui():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_quick_compare)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()

        label1 = Label(root, text='Choose two sorting algorithms from all Sorting Algorithm', bg="#E5DCFC"
                       ,font='TIMES_NEW_ROMAN')
        label1.pack(pady = 10)

        btn1 = Button(root, text="insertion sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_insertion_compare)
        btn1.pack(pady = 2)

        btn2 = Button(root, text="merge sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_merge_compare)
        btn2.pack(pady=2)

        btn3 = Button(root, text="selection sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_selection_compare)
        btn3.pack(pady=2)

        btn4 = Button(root, text="heap sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_heap_compare)
        btn4.pack(pady=2)

        btn6 = Button(root, text="radix sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_radix_compare)
        btn6.pack(pady=2)

        btn7 = Button(root, text="Bubble sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_bubble_compare)
        btn7.pack(pady=2)

        btn8 = Button(root, text="Quick sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_quick_compare)
        btn8.pack(pady=2)

        #btn9 = Button(root, text="Counting sort", bg="#e91e63", fg="white", borderwidth=0, command=main_counting_compare)
        #btn9.pack()

        btn_create_random = Button(root, text="Generate Random Numbers", bg="#A9F488", fg="black", height=1,
                                   width=25, borderwidth=5, command=Generate)
        btn_create_random.pack(pady =10)

        btn_back = Button(root, text="Back", bg="#19360C", fg="white", height=1, width=10, borderwidth=5,
                          command=back)
        btn_back.pack(pady=5, side=LEFT, padx=20)




    def page_single_sort():
        label_welcome.destroy()
        btn_single.destroy()
        btn_compare.destroy()



        def back():
            label1.destroy()
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
            btn4.destroy()
            btn6.destroy()
            btn7.destroy()
            btn8.destroy()
            btn_create_random.destroy()
            btn_back.destroy()
            page1()

        def ins():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL,length=200,mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_insertion)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()

        def merg():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL,length=200,mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_merge)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()

            window.mainloop()
        def sel():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL,length=200,mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_selection)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()
        def he():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL,length=200,mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_heap)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()
        def rad():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL,length=200,mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_radix)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()
        def bub():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL,length=200,mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_bubble)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()
        def qui():
            window = Tk()
            window.title("Loading")
            window.geometry("300x200")
            bar = ttk.Progressbar(window, orient=HORIZONTAL,length=200,mode='indeterminate')
            bar.pack()
            t1 = threading.Thread(target=main_quick)
            t2 = threading.Thread(target=bar.start)
            t1.start()
            t2.start()
            window.mainloop()

        label1 = Label(root, text='Choose a single sort from all Sorting Algorithm', bg="#E5DCFC",
                       font='TIMES_NEW_ROMAN')
        label1.pack(pady=20)

        btn1 = Button(root, text="insertion sort", bg="#E2589B", fg="white", height=1, width=25,
                      borderwidth=5, command=main_insertion)
        btn1.pack(pady=2)

        btn2 = Button(root, text="merge sort", bg="#E2589B", fg="white", height=1, width=25,
                      borderwidth=5, command=main_merge)
        btn2.pack(pady=2)

        btn3 = Button(root, text="selection sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_selection)
        btn3.pack(pady=2)

        btn4 = Button(root, text="heap sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_heap)
        btn4.pack(pady=2)

        btn6 = Button(root, text="radix sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_radix)
        btn6.pack(pady=2)

        btn7 = Button(root, text="Bubble sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_bubble)
        btn7.pack(pady=2)

        btn8 = Button(root, text="Quick sort", bg="#E2589B", fg="white", height=1, width=25, borderwidth=5,
                      command=main_quick)
        btn8.pack(pady=2)

        #btn9 = Button(root, text="Counting sort", bg="#e91e63", fg="white", borderwidth=0, command=main_counting)
        #btn9.pack()

        btn_create_random = Button(root, text="Generate Random Numbers", bg="#A9F488", fg="black", height=1, width=25,
                                   borderwidth=5, command=Generate)
        btn_create_random.pack(pady = 20)
        btn_back = Button(root, text="Back", bg="#19360C", fg="white",height=1, width=10, borderwidth=5, command=back)
        btn_back.pack(pady=4, side=LEFT, padx=20)






    label_welcome= Label(root,text='Welcome to our Sorting Algorithm Application',bg="#E5DCFC",font='TIMES_NEW_ROMAN')
    label_welcome.pack(pady=20)
    btn_single = Button(root, text="Choose a Single Sorting Algorithm", bg="#E2589B", fg="white",
                        borderwidth=5, height=3, width=35, command=page_single_sort)
    btn_single.pack(pady=40)
    btn_compare = Button(root, text="Compare between two Algorithms", bg="#E2589B", fg="white",
                         height=3, width=35, borderwidth=5, command=page_compare_sort)
    btn_compare.pack(pady=20)


page1()

root.mainloop()


