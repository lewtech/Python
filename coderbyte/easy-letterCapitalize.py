def LetterCapitalize(str):
    # code goes here
    counter = 0
    capitalizeNext = False
    newString = ""
    for char in str:

        if counter == 0 or capitalizeNext == True:
            char = char.upper()
            capitalizeNext == False
        if char == " ":
            capitalizeNext == True
        counter = counter + 1
        newString = newString + char
    return newString


# keep this function call here
print (LetterCapitalize("hello world"))

##initialize newString, and counter
#step1 get string
#step2 capitalize first letter (position 0)
#step3 iterate through until a space is found, Capitalize the next letter.