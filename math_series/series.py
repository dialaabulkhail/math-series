"""
        function fibonacci:
           It is a functoin that outputs a fibonacci series.
           Input is an integer and output is equal to the summation of two previous integers of that input.
           Special cases:
           - 0 that outputs 0.
           - 1 that outputs 1.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1 :
        return fibonacci(n-1) + fibonacci(n-2)


"""
          function lucas:
          It is a function that takes an input of integer and outputs the summation of the previous two integers.
          Special cases:
          - 0 that outputs 2.
          - 1 that outputs 1.
"""

def lucas(x):
    if x == 0:
        return 2
    elif x == 1:
        return 1
    elif x > 1:
        return lucas(x-1) + lucas(x-2)


"""
          function sum_series:
          It is a function that takes one required parameter and two optional parameters.
          Special cases:
          - if called with only required parameter --> returns fibonacci series.
          - if called with the two optional parameters --> returns lucas series.
"""

def sum_series(ele, x=0 ,y=1):
    if x == 2:
        return lucas(ele)
    else:
        return fibonacci(ele)