import numpy
# use numpy.array


def arrays(array):
    # Convert the list of strings to a NumPy array with float data type and reverse it
    reversed_array = numpy.array(array, dtype=float)[::-1]
    return reversed_array


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
