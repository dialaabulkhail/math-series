from math_series.series import fibonacci, lucas
num = int()
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1)+ fibonacci(num-2)
     

def test_one():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_two():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


#Lucas

number = int()
def lucas(number):
    if number == 0:
        return 2
    elif number == 1:
        return 1
    else:
        return lucas(number-1) + lucas(number-2)


def test_three():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_four():
    actual = lucas(5)
    expected = 11
    assert actual == expected


# sum series 
ele = int()
def sum_series(ele, x = 0, y = 1):
    if x == 2:
        return lucas(ele)
    else:
        return fibonacci(ele)
  
def test_five():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_six():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected


