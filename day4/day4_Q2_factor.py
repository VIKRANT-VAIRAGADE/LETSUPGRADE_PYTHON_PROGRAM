
a = int(input("enter the number = "))

def factorial(a):
    if a ==0:
        return 1
    if a <0 or a==1:
        return 0

    else :
        num =1
        while (a>1):
            num = num*a
            a=a-1
        return num



#result = factorial(a)
print("factor of number",a, "is",factorial(a))