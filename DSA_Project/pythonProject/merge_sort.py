import Compare
import Generate_rand
import attributes_class

# Python program for implementation of MergeSort
from Generate_rand import Generate
def mergeSort(arr,Tj):
    count=0
    Tj+=1
    if len(arr) > 1:
        Tj+=3

        # Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        count += mergeSort(L,Tj)


        # Sorting the second half
        count += mergeSort(R,Tj)
        Tj = count
        i = j = k = 0
        Tj += 1
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            Tj+=1
            if L[i] < R[j]:
                Tj += 2
                arr[k] = L[i]
                i += 1
            else:
                Tj += 2
                arr[k] = R[j]
                j += 1
            k += 1
            Tj += 1


            # Checking if any element was left
        while i < len(L):
                Tj+=3

                arr[k] = L[i]
                i += 1
                k += 1


        while j < len(R):
                Tj += 3
                arr[k] = R[j]
                j += 1
                k += 1

    return Tj
    # Code to print the list

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

    # Driver Code

def main_merge():
    merge = attributes_class.attributes()

    merge.Name ='Merge'

    if(Generate_rand.counter == 1):
        merge.start()

    x_axis,y_axis,Tj = merge.calculate(merge.Name)
    merge.plot_graph(x_axis, y_axis, merge.Name, Tj)
def main_merge_compare():
    merge = attributes_class.attributes()
    merge.Name = 'Merge'
    if (Generate_rand.counter == 1):
        merge.start()
    x_axis,y_axis, Tj = merge.calculate(merge.Name)

    Compare.compare(x_axis,y_axis, merge.Name)




