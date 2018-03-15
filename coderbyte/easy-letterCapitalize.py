def LetterCapitalize(str):
    # code goes here
    counter = 0
    capitalizeNext = False
    newString = ""
    for char in str:

        if counter == 0 or capitalizeNext == True:
            char = char.upper()
            capitalizeNext == False
            counter = counter + 1
        if char == " ":
            capitalizeNext == True
            counter = 0


        newString = newString + char
    return newString


# keep this function call here
print (LetterCapitalize("hello world"))

##initialize newString, and counter
#step1 get string
#step2 capitalize first letter (position 0)
#step3 iterate through until a space is found, Capitalize the next letter.


def LetterCapitalize2soln(str):
    # split the string into a list
    words = str.split(" ")

    # we split the word into two parts and then combine the parts
    # the first part is the first letter which we capitalize and the
    # second part is the rest of the string
    for i in range(0, len(words)):
        words[i] = words[i][0].upper() + words[i][1:]

    # return the list of words joined into a string
    return " ".join(words)


print (LetterCapitalize2soln("hello world from coderbyte"))


def LetterCapitalize3soln(str):
    # in python there is a function called title which is
    # easier than using a regex pattern
    return str.title()


print (LetterCapitalize3soln("hello world from coderbyte"))
