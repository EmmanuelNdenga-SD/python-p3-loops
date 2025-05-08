#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i >=1: #because we want to count down from 10 to 1
        print(i) #print the value of i
        i -= 1 # decrement i by 1 because it is a countdown
    print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    new_list = []
    for i in int_list: 
        new_list.append(i**2)
    return new_list
    
def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:  # Check for multiples of both 3 and 5 first
            print("FizzBuzz")
        elif num % 3 == 0:  
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the function
fizzbuzz()