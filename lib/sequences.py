#!/usr/bin/env python3

def print_fibonacci(length):
    empty_li = []  # Initialize an empty list to store the Fibonacci sequence
    for i in range(length):  # Loop from 0 to length-1
        if i < 2:
            empty_li.append(i)  # If i is 0 or 1, add i to the sequence
        else:
            empty_li.append(empty_li[-1] + empty_li[-2])  # Add the last two numbers in the sequence to get the next one

    print(empty_li)  # Print the resulting Fibonacci sequence

print_fibonacci(9)  # Call the function with a length of 9
