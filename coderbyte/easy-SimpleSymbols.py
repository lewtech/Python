'''

Challenge
Using the Python language, have the function SimpleSymbols(str) take the str parameter being passed and determine if it
is an acceptable sequence by either returning the string true or false.
The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a)
and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false.
The string will not be empty and will have at least one letter.
Sample Test Cases

Input:"+d+=3=+s+"

Output:"true"


Input:"f++d+"

Output:"false"
'''

def SimpleSymbols(string):
    # pad the string so we dont run into out of bounds error
    string = '=' + string + '='

    # loop through the entire string
    for i in range(0, len(string)):

        # check if current character is an alphabetic character
        if string[i].isalpha():

            #check if + on left or right
            if string[i-1] != '+' or string[i+1] != '+':
                return False


    return True



assert SimpleSymbols("+++") == True
assert SimpleSymbols("+d+=3=+s+") == True
# assert SimpleSymbols("++") == False