import Compare
import attributes_class
import Generate_rand

def heapify(arr, n, i,Tj):

    largest = i  # Initialize largest as root

    l = 2 * i + 1  # left = 2*i + 1

    r = 2 * i + 2  # right = 2*i + 2
    Tj+=3

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        Tj += 1
        largest = l
        Tj += 1

    # See if right child of root exists and is
    # greater than root
    Tj+=1
    if r < n and arr[largest] < arr[r]:
        Tj += 1
        largest = r
        Tj += 1

    # Change root, if needed
    if largest != i:
        Tj += 1
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        Tj += 1

        # Heapify the root.
        Tj = heapify(arr, n, largest, Tj)
    return Tj


def heapSort(arr, Tj):
    Tj +=1
    n = len(arr)
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n // 2 - 1, -1, -1):
        Tj = heapify(arr, n, i,Tj)

    # One by one extract elements

    for i in range(n - 1, 0, -1):
        Tj += 1
        arr[i], arr[0] = arr[0], arr[i]  # swap
        Tj = heapify(arr, i, 0, Tj)
    return Tj

def main_heap():
    heap = attributes_class.attributes()
    heap.Name = 'Heap'
    if (Generate_rand.counter == 1):
        heap.start()
    x_axis, y_axis, Tj = heap.calculate(heap.Name)
    heap.plot_graph(x_axis, y_axis, heap.Name, Tj)

def main_heap_compare():
    heap = attributes_class.attributes()
    heap.Name = 'Heap'
    if (Generate_rand.counter == 1):
        heap.start()
    x_axis,y_axis,Tj = heap.calculate(heap.Name)
    Compare.compare(x_axis,y_axis,heap.Name)
