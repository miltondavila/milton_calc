from math_operations.add_numbers import add_numbers
from math_operations.subtract_numbers import subtract_numbers



if __name__ == '__main__':

    num1 = 5
    num2 = 10
    
    sum_result = add_numbers(num1, num2)
    substract_result = subtract_numbers(num1, num2)

    print(f'The sum of {num1} and {num2} is {sum_result}')
    print(f'The difference between {num1} and {num2} is {substract_result}')


