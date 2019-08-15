
                    ############################
                    #JUPYTER NOTEBOOK EXCERCICES#
                    ############################

###################### TASK 1 #######################
#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
#but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

def lesserfunc(n1,n2):
    if n1%2 == 0 and n2%2 == 0:
        if n1<n2:
            return(n1)
        else:
            return(n2)
    else:
        if n1>n2:
            return(n1)
        else:
            return(n2)

num1 = int(input('Enter Number 1: '))
num2 = int(input('Enter Number 2: '))


print(lesserfunc(num1, num2))
print('TASK COMPLETE')


####################### TASK 2 #######################
#ANIMAL CRACKERS:
# Write a function takes a two-word string and returns True if both words begin with same letter


def animal_cracker(word1):
    wordlist = word1.split()
    print(wordlist[0][0] == wordlist[1][0])

word1 = input('Enter a two words: ')
animal_cracker(word1)
print('TASK COMPLETE')

####################### TASK 3 #######################
# MAKES TWENTY:
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False



def makes_twenty(num1,num2):
    numbers = []
    numbers.append(num1)
    numbers.append(num2)
    if num1 == 20 or num2 == 20:
        return True
    elif sum(numbers) == 20:
        return True
    else:
        return False

num1 = int(input('Enter Number 1: '))
num2 = int(input('Enter Number 2: '))
print(makes_twenty(num1, num2))
print('TASK COMPLETE')

####################### LEVEL 1 PROBLEMS #######################

#OLD MACDONALD:
#Write a function that capitalizes the first and fourth letters of a name

def macdonald_func(mystring):
    dumb_string = []
    for i in range(len(mystring)):
        if i == 0 or i == 3:
            dumb_string.append(mystring[i].upper())
        else:
           dumb_string.append(mystring[i].lower())
    print(''.join(dumb_string))

macdonald_func(input("Enter a word: "))

#MASTER YODA:
# Given a sentence, return a sentence with the words reversed

def master_yoda(mystring):
    word_list = mystring.split()
    new_word_list = []
    back_of_list = len(word_list)
    for i in word_list:
        new_word_list.append(word_list[back_of_list-1])
        back_of_list -= 1

    print(new_word_list)
    newword = ' '.join(new_word_list)
    return newword.capitalize()

print(master_yoda(input("Enter a sentence: ")))

# ALMOST THERE:
# Given an integer n, return True if n is within 10 of either 100 or 200
#
# ALMOST THERE:
# Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(num1):
    return abs(100-num1) <= 10 or abs(200-num1) <=10

print(almost_there(int(input('Enter a number: '))))

#FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def find33(nums):

    last_num = 0
    for i in range(len(nums)):
        if nums[i] == 3 and last_num == 3:
            return True
        last_num = nums[i]
    return False

print(find33([1,2,3,4,3,3,1,3]))

# PAPER DOLL:
# Given a string, return a string where for every character in the original there are three characters

def paper_doll(mystring):
    trpl_word = ''
    for i in range(len(mystring)):
        trpl_word = trpl_word + mystring[i] * 3
    print(trpl_word)

paper_doll(input('ENTER WORD HERE: '))

# BLACKJACK:
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(n1,n2,n3):
    num_list = [n1,n2,n3]
    sum_numb = sum(num_list)
    if sum_numb <= 21:
        return(sum_numb)
    elif 11 in num_list and sum_numb > 21:
        sum_numb -= 10
        print('-10!\n')
        if sum_numb > 21:
            return 'BUST!'
        else:
            return sum_numb
    else:
        return 'BUST!'
n1 = int(input("ENTER NUMBER 1: "))
n2 = int(input("ENTER NUMBER 2: "))
n3 = int(input("ENTER NUMBER 3: "))
print(blackjack(n1,n2,n3))


# SUMMER OF '69:
# Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.

def summer69(mylist):
    newlist = []
    stopcounting = False
    for i in range(len(mylist)):
        if mylist[i] == 6:
            stopcounting = True
        elif mylist[i] == 9 and stopcounting == True:
            stopcounting = False
        elif stopcounting == False:
            newlist.append(mylist[i])
        else:
            pass
    return sum(newlist)


print(summer69([9,2,6,7,9]))

# SPY GAME:
# Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(mylist):
    last_num = 1
    last_last_num = 1
    for i in range(len(mylist)):
        if mylist[i] == 7 and last_num == 0 and last_last_num == 0:
            return True
        last_last_num = last_num
        last_num = mylist[i]
    return False

print(spy_game([1,0,7,5,1,0,7,2,3]))



# COUNT PRIMES:
# Write a function that returns the number of prime numbers that exist up to and including a given number

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
def count_primes(upper):
    mylist = []
    for num in range(0,upper + 1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               mylist.append(num)

    print(mylist)
count_primes(30)
def count_primes(num):
    #list_of_primes = []
    for i in range(2,num+1):
        add_to_list = True
        for k in range(2,i):
            if i%k == 0:
                add_to_list = False
        if add_to_list == True:
            list_of_primes.append(i)
    return list_of_primes
