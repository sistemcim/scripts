#!/usr/bin/python
# This script is a sample python file.
##
# Author: sistemcim
# Blog: https://sistemcim.wordpress.com
# Github: https://github.com/sistemcim
#

SHOW_SAMPLE_STRING=0
SHOW_SAMPLE_LIST=0
SHOW_SAMPLE_TUPLE=0
SHOW_SAMPLE_DICTIONARY=0

SHOW_SAMPLE_IF=0

SHOW_SAMPLE_WHILE_LOOP=0
SHOW_SAMPLE_FOR_LOOP=0

print "Hello\n"
#User Input
#input=raw_input("\n\nPress the enter key to exit.")

# Data Types
    # ------------------- NUMBER
    #       int     10      (signed integers)
    #       long    0122L   (long integers, they can also be represented in octal and hexadecimal)
    #       float   15.20   (floating point real values)
    #       complex 3.14j   (complex numbers)

if SHOW_SAMPLE_STRING != 0 : 
    # ------------------- STRING
    #       Represented in the quotation marks.
    print "########### String Example #############"
    str = 'Hello World!'
    print str
    print str[0]
    print str[2:5]
    print str[2:]
    print str * 2 # Prints string two times
    print str + "TEST"

if SHOW_SAMPLE_LIST != 0 : 
    # ------------------- LIST
    #       Lists are enclosed in brackets [] and their elements and size can be changed.
    #       All the items belonging to a list can be of different data type.
    print "########### List Example #############"
    list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
    tinylist = [123, 'john']

    print list # Prints complete list
    print list[0] # Prints first element of the list
    print list[1:3] # Prints elements starting from 2nd till 3rd
    print list[2:] # Prints elements starting from 3rd element
    print tinylist * 2 # Prints list two times
    print list + tinylist # Prints concatenated lists

if SHOW_SAMPLE_TUPLE != 0 : 
    # ------------------- TUPLE
    #       Tuples are enclosed in parentheses ( ) and cannot be updated
    print "########### Tuple Example #############"
    tuple = ( 'abcd', 786 , 2.23, 'john', 70.2)
    tinytuple = (123, 'john')
    
    print tuple # Prints complete list
    print tuple[0] # Prints first element of the list
    print tuple[1:3] # Prints elements starting from 2nd till 3rd
    print tuple[2:] # Prints elements starting from 3rd element
    print tinytuple * 2 # Prints list two times
    print tuple + tinytuple # Prints concatenated lists

if SHOW_SAMPLE_DICTIONARY != 0 : 
    # ------------------- DICTIONARY
    #       Dictionaries are kind of hash table type.
    #       Dictionaries are enclosed by curly braces { } and values can be assigned and accessed using square braces [].
    print "########### Dictionary Example #############"

    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"
    tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
    print dict['one'] # Prints value for 'one' key
    print dict[2] # Prints value for 2 key
    print tinydict # Prints complete dictionary
    print tinydict.keys() # Prints all the keys
    print tinydict.values() # Prints all the values

# Operators
    # ------------------- Arithmetic Operators
    #       +, -, *, /, %, **(exponent), //(floor division)
    # ------------------- Comparison (Relational) Operators
    #       ==, !=, <>, >, <, >=, <=
    # ------------------- Assignment Operators
    #       =, +=, -=, *=, /=, %=, **=, //=
    # ------------------- Logical Operators
    #       and, or, not
    # ------------------- Bitwise Operators
    #       &(and), |(or), ^(xor), ~(complement), <<(left shift), >>(right shift) 
    # ------------------- Membership Operators
    #       in, not in
    # ------------------- Identity Operators
    #       is, is not

if SHOW_SAMPLE_IF != 0 : 
    #----- If Elif Condition ----------------------
    print "########### If Elif Example #############"
    input="f"
    if input == "a" :
        print "input is a"
    elif input == "b" :
        print "input is b"
    else :
        print "input is ", input

if SHOW_SAMPLE_WHILE_LOOP != 0 :
    #----- While Loop With Else ------------------
    print "########### While Loop Example #############"
    count = 0
    while count < 5:
        print count, " is less than 5"
        count = count + 1
    else:
        print count, " is not less than 5"

if SHOW_SAMPLE_FOR_LOOP != 0 :
    #----- For Loop -----------------------------
    print "########### For Loop Example #############"
    for letter in 'Python':
        print 'Current Letter :', letter

    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:
        print 'Current fruit :', fruit

    fruits = ['banana', 'apple', 'mango']
    for index in range(len(fruits)):
        print 'Current fruit :', fruits[index]

    for num in range(10,20): #to iterate between 10 to 20
        for i in range(2,num): #to iterate on the factors of the number
            if num%i == 0: #to determine the first factor
                j=num/i #to calculate the second factor
                print '%d equals %d * %d' % (num,i,j)    
                break #to move to the next number, the #first FOR
        else:# else part of the loop
            print num, 'is a prime number'
    print "\n"


