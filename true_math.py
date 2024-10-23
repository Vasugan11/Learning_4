from math import inf

def divide(first, second):
    try:
        result = first / second
    except ZeroDivisionError:
        print(inf)
    else:
        print(result)


#divide(10, 0)
