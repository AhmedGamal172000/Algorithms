import attributes_class
import Compare
import Generate_rand
def countingSort(arr, exp1,Tj):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)
    # initialize count array as 0
    count = [0] * (10)
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (int(arr[i]) / int(exp1))
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        Tj+=1
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1

    while i >= 0:
        Tj+=1
        index = (int(arr[i]) / int(exp1))
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1
    i = 0

    for i in range(0, len(arr)):
        Tj+=1
        arr[i] = output[i]
    return Tj
def radixSort(arr,Tj):
    # Find the maximum number to know number of digits
    Tj+=1

    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1


    while (int(max1)/exp) > 0:
        Tj+=2
        Tj = countingSort(arr, exp,Tj)
        exp *= 10

    return Tj

def main_radix():
    radix = attributes_class.attributes()
    radix.Name = 'Radix'
    if (Generate_rand.counter == 1):
        radix.start()
    x_axis, y_axis, Tj = radix.calculate(radix.Name)
    radix.plot_graph(x_axis, y_axis, radix.Name, Tj)
def main_radix_compare():
    radix = attributes_class.attributes()
    radix.Name = 'Radix'
    if (Generate_rand.counter == 1):
        radix.start()
    x_axis,y_axis, Tj = radix.calculate(radix.Name)
    Compare.compare(x_axis, y_axis, radix.Name)

