def add(x,y):
    c=x+y
    return c
sum_res=add(21,31)
print(sum_res)


def add1(x,y):
    print(x+y)

add1(2222,31)



def hello_world():
    print("Hello world")
hello_world()

def sum(num1, num2):
    if ( type(num1) is not int or type(num2) is not int):
        return 0

    return num1+num2
ans=sum()
print(ans)