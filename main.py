"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y)

def _quadratic_multiply(x, y):
    if isinstance(x,BinaryNumber) ==False :
        x = BinaryNumber(x)
    if isinstance(y, BinaryNumber) == False:
        y = BinaryNumber(y)
    x.binary_vec,y.binary_vec = pad(x.binary_vec,y.binary_vec)
    n = len(x.binary_vec)
    # print("n=",n)

    if x.decimal_val <=1 and y.decimal_val<= 1:
        return x.decimal_val * y.decimal_val
    else:
        x_tuple = split_number(x.binary_vec)
        y_tuple = split_number(y.binary_vec)
        x_left = x_tuple[0]
        x_right = x_tuple[1]
        y_left = y_tuple[0]
        y_right = y_tuple[1]
        # print(x.binary_vec, y.binary_vec, x_left, x_right, y_left, y_right)
        first_before_shift = BinaryNumber(_quadratic_multiply(x_left, y_left))
        first =(bit_shift(first_before_shift, n)).decimal_val
        second_before_shift = BinaryNumber(_quadratic_multiply(x_left, y_right)+_quadratic_multiply(x_right, y_left))
        second= (bit_shift(second_before_shift, n // 2)).decimal_val
        third = _quadratic_multiply(x_right,y_right)
        # print(first_before_shift, first, n)
        # print(second_before_shift, second, n//2)
        # print(second)
        # print(third)
    return  first + second + third


    pass
    ###


def multiply(x,y):
    return x*y
    
def  time_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000


import time

# Iterate over powers of 10 for x and y
powers = [10**i for i in range(1, 7)]  # Adjust range as needed

# Print table header
print(f"{'x':<10}{'y':<10}{'Quadratic Time (ms)':<20}{'Multiply Time (ms)':<20}")

for x in powers:
    for y in powers:
        quad_time = time_quadratic_multiply(x, y, quadratic_multiply)
        mult_time = time_quadratic_multiply(x, y, multiply)
        print(f"{x:<10}{y:<10}{quad_time:<20.6f}{mult_time:<20.6f}")



# x         y         Quadratic Time (ms) Multiply Time (ms)
# 10        10        0.056028            0.000000
# 10        100       0.236034            0.001192
# 10        1000      0.165224            0.000954
# the quadratic function seems to have a O(lgn) run time and the multiply function seems to run much faster


    
    

