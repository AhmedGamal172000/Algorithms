

import Compare
import attributes_class
import Generate_rand

def partition(arr, low, high,Tj):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot
    Tj += 2
    for j in range(low, high):
        Tj += 1
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            Tj += 1
            # increment index of smaller element
            i = i + 1
            Tj += 1
            arr[i], arr[j] = arr[j], arr[i]
            Tj += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    Tj += 1
    return (i + 1), Tj


def quickSort(arr, low, high,Tj):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi, Tj = partition(arr, low, high,Tj)

        # Separately sort elements before
        # partition and after partition
        Tj=quickSort(arr, low, pi - 1,Tj)
        Tj=quickSort(arr, pi + 1, high,Tj)

    return Tj

def main_quick():
    quick = attributes_class.attributes()
    quick.Name ='Quick'
    if (Generate_rand.counter == 1):
        quick.start()
    x_axis,y_axis,Tj = quick.calculate(quick.Name)
    quick.plot_graph(x_axis, y_axis, quick.Name, Tj)

def main_quick_compare():
    quick = attributes_class.attributes()
    quick.Name ='Quick'
    if (Generate_rand.counter == 1):
        quick.start()
    x_axis, y_axis, Tj=quick.calculate(quick.Name)
    Compare.compare(x_axis, y_axis, quick.Name)