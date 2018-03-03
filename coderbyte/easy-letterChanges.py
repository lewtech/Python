def LetterChanges(str):
    '''   # THIS WAS MY FIRST ATTEMPT
    str = str.lower()
    str = str.split()
    for i in len(str):
        asciiString = ord(str[i])
        if (asciiString[i] > 96 and asciiString[i] < 122):
            asciiString[i] = asciiString[i] + 1
        if (asciiString[i] == 122):
            asciiString[i] = 97


        str[i]=asciiString


    return join(str)


# keep this function call here
assert (LetterChanges("a")=='z'),print("fail")
assert (LetterChanges('z')=='a'),print("fail")
'''
    newString = ""
    for char in str:
        if char.isalpha():
            if char.lower() == 'z':
                char = 'a'
            else:
                char = chr(ord(char) + 1)
        if char is 'aeiou':
            char = char.upper()

        newString = newString + char
    return newString

print (LetterChanges("abcde"))