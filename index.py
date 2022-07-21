hello = "hello world"
print(hello)

#-------------------------------------------------------
#Addition Function

def add_num(a,b):#function for addition
    sum=a+b;
    return sum; #return value
#num1=int(input("input number one: "))#input from user for num1
#num2=int(input("input number two:"))#input from user for num2

#print("The sum is",add_num(num1,num2))#call the function

#------------------------------------------------------
#Subtraction Function

def sub_num(a,b):#function for subtraction
    sub=a-b;
    return sub; #return value

#num1=int(input("input number one: "))#input from user for num1
#num2=int(input("input number two:"))#input from user for num2

#print("The subtraction is",sub_num(num1,num2))#call the function

#------------------------------------------------------
#Multiplication Function

def mul_num(a,b):#function for multiplication
    mul=a*b;
    return mul; #return value

#num1=int(input("input number one: "))#input from user for num1
#num2=int(input("input number two:"))#input from user for num2

#print("The multiplication is",mul_num(num1,num2))#call the function

#------------------------------------------------------
#Division Function

def div_num(a,b):#function for division
    div=a/b;
    return div; #return value

#num1=int(input("input number one: "))#input from user for num1
#num2=int(input("input number two:"))#input from user for num2

#print("The division is",div_num(num1,num2))#call the function

#------------------------------------------------------
#Calculator
while True:
    Operator = input("Select Operation:")

    if Operator in ('+','-','*','/'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    if Operator == '+':
        print(num1, "+", num2, "=", add_num(num1, num2))
    elif Operator == '-':
        print(num1, "-", num2, "=", sub_num(num1, num2))
    elif Operator == '*':
        print(num1, "*", num2, "=", mul_num(num1, num2))
    elif Operator == '/':
        print(num1, "/", num2, "=", div_num(num1, num2))
    else:
        print("Invalid operator: Try + for addition, - for subtraction, * for multiplication, / for division")

