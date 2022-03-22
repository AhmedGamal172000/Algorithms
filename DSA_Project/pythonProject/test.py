import random
def Random_Numbers(self, temp_arr):
    for i in range(10000):
        num = random.randint(1, 100)
        temp_arr.append(num)


def save_rand_in_file(self, file, temp_arr):
    for i in range(len(temp_arr)):
        file.write("%d\n" % temp_arr[i])

def readFile():
        fileObj = open("Numbers", "r")  # opens the file in read mode
        words = fileObj.read().splitlines()  # puts the file into an array
        fileObj.close()
        return words
ahmed = readFile()
print(ahmed[15])