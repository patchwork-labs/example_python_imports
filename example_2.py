# Tests for import functions
import class_examples
# from class_examples import calculate_size
# import class_examples as ce
# from class_examples import calculate_size as cs
# from class_examples import calculate_size, new_doubled_function
# from class_examples import calculate_size, new_doubled_function as ndf
# from class_examples import calculate_size as cs, new_doubled_function as ndf
# from class_examples import calculate_size as cs, new_doubled_function
import math.gcd as g

 
# TODO: support non-local import functions
g(32)

def new_doubled_function():
    return 8

def call_call_calculate():
 return call_calculate()

def call_calculate():
 answer = class_examples.calculate_size()
 return answer

answer = class_examples.calculate_size()
calc = call_call_calculate()
