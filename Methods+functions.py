
def name_func():
   '''
   DOCSTRING: Information about the function
   INPUT: no input
   OUTPUT: Hello
   '''
   print('Hello')

print(help(name_func))

def say_hello(name):
    return('Hello ' +name)

result = say_hello('Jeff')
print(result)

def add(n1,n2):
    return n1+n2

result = add(20,40)
print(result)

def pig_latin(word):
    first_letter = word[0]
#check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:]+ first_letter + 'ay'
    print(pig_word)

pig_latin('alol')

mystring = 'Jeff'

print(mystring.upper())

def myfunc(mystring):
    k = len(mystring)
    i = 0
    dumb_string = ''
    while i != k:
        if i%2 == 0:
            newletter = mystring[i]
            dumb_string = dumb_string + newletter.lower()
            i = i+1
        else:
            newletter = mystring[i]
            dumb_string = dumb_string + newletter.upper()
            i = i+1
    print(dumb_string)


def myfunc(mystring):
    dumb_string = []

    for i in range(len(mystring)):
        if i%2 == 0:
            dumb_string.append(mystring[i].lower())
        else:
           dumb_string.append(mystring[i].upper())
    print(''.join(dumb_string))

myfunc('pEpegagoblin')
