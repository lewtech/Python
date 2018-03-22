'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.

[Python3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
'''

#what are we trying to do here? we want the product of any adjacent numbers to be the highest
#maybe we can create an array of pairs and then multiply them
#sort by the highest pair, but how do we know what the pair was?

input_array = [3, 6, -2, -5, 7, 3]


def adjacentElementsProduct(array):
    solution = 0
    if len(array) == 1:
        solution = array[0]
    if len(array) == 2:
        solution = array[0] * array[1]
    if len(array) > 2:
        for i in (len(array) - 1):


    #print (solution)
    return solution

#I think the fastest is to just multiply them out, and then iterate back to the source
#tests and thoughts
adjacentElementsProduct(input_array)
print (adjacentElementsProduct([1]))
print (adjacentElementsProduct([1,2]))
print (adjacentElementsProduct([1,2,3]))
#hmmm, how can i find the greatest out of 3 or more items multiplied...perhaps a loop of x in len(array)-1
#@10:36pm, yeah algorithms are hard to figure out late at night.