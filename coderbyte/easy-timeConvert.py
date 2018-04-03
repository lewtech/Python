'''
Using the Python language, have the function TimeConvert(num) take the num parameter being passed
and return the number of hours and minutes the parameter converts to
(ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon.

Sample Test Cases
Input:126

Output:"2:6"


Input:45

Output:"0:45"
'''

# the important thing is to divide the number into hours
# print that on the left side of the colon
# the remainder which will be modulo will be in minutes
# format printing and done.

def TimeConvert(num):
    hours = int(num/60)
    minutes = num % 60
    return ("{}:{}".format(hours,minutes))



assert TimeConvert(126) == "2:6"
assert TimeConvert(45) == "0:45"