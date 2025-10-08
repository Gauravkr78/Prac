# Function 1: add two numbers and return result
def add(x, y):
    c = x + y
    return c

sum_res = add(21, 31)
print(sum_res)

# Function 2: print sum directly
def add1(x, y):
    print(x + y)

add1(2222, 31)

# Function 3: say hello
def hello_world():
    print("Hello world")

hello_world()

# Function 4: type-safe sum
def sum_numbers(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2

# Call it correctly with two arguments
ans = sum_numbers(10, 20)
print(ans)
