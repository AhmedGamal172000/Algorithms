import sys
import attributes_class
import Compare
import Generate_rand

def selcetionSort(arr, Tj):
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                Tj += 1
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return Tj

def main_selection():
    sel = attributes_class.attributes()
    sel.Name = 'Selection'
    if (Generate_rand.counter == 1):
        sel.start()
    x_axis, y_axis, Tj = sel.calculate(sel.Name)
    sel.plot_graph(x_axis, y_axis, sel.Name, Tj)

def main_selection_compare():
    sel = attributes_class.attributes()
    sel.Name = 'Selection'
    if (Generate_rand.counter == 1):
        sel.start()
    x_axis,y_axis, Tj = sel.calculate(sel.Name)
    Compare.compare(x_axis, y_axis, sel.Name)

