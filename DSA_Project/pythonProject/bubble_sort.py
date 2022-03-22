import attributes_class
import Compare

def bubbleSort(arr,Tj):
    n = len(arr)
    Tj += 1
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        Tj += 1
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            Tj += 1
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:

                Tj += 3
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return Tj
def main_bubble():
    bubble = attributes_class.attributes()
    bubble.Name = 'Bubble'
    #bubble.start()
    x_axis, y_axis, Tj = bubble.calculate(bubble.Name)
    bubble.plot_graph(x_axis,y_axis,bubble.Name, Tj)

def main_bubble_compare():
    bubble = attributes_class.attributes()
    bubble.Name = 'Bubble'
    #bubble.start()
    x_axis, y_axis, Tj = bubble.calculate(bubble.Name)
    Compare.compare(x_axis, y_axis, bubble.Name)