import attributes_class
import Compare
import Generate_rand

def countSort(arr,Tj):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
    # Store count of each character
    for i in range(0, len(arr)):
        Tj+=1
        count_arr[arr[i] - min_element] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        Tj+=1
        count_arr[i] += count_arr[i - 1]

    # Build the output character array
    for i in range(len(arr) - 1, -1, -1):
        Tj+=2
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        Tj+=1
        arr[i] = output_arr[i]

    return Tj
def main_counting():
    count = attributes_class.attributes()
    count.Name = 'Counting'
    if(Generate_rand.counter == 1):
        count.start()
    x_axis, y_axis , Tj=count.calculate(count.Name)
    count.plot_graph(x_axis,y_axis, count.Name, Tj)

def main_counting_compare():
    count = attributes_class.attributes()
    count.Name = 'Counting'
    if(Generate_rand.counter == 1):
        count.start()
    x_axis, y_axis , Tj= count.calculate(count.Name)
    Compare.compare(x_axis,y_axis,count.Name)
