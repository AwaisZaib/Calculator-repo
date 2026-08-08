import math
#basic arithmetic functions
def add(num):
    nextNum=float(input("enter next num :"))
    result= num+nextNum
    return result
def subtract(num):
    nextNum=float(input("enter next num :"))
    result= num-nextNum
    return  result
def multiply(num):
    nextNum=float(input("enter next num :"))
    result= num*nextNum
    return result
def division(num):
    try:
        nextNum = float(input("Enter next num: "))
        return num / nextNum

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return 0
def power(num):
    nextNum=float(input("enter next num :"))
    result= math.pow(num,nextNum)
    return result
def percentage(num):
    nextNum=float(input("enter next num :"))
    result= (num*nextNum)
    return result
def sqrt(num):
    if(num<0):
     return num
    result=math.sqrt(num)
    return result
def log(num):
    if(num<0):
     return num
    result= math.log10(num)
    return result
def factorial(num):
    result= math.factorial(int(num))
    return result

# trignometric functions 
def sin_func(num):
    result= math.sin( math.radians(num))
    return result
def cos_func(num):
    result= math.cos( math.radians(num))
    return result
def tan_func(num):
    result= math.tan( math.radians(num))
    return result

# inverse trignometric functions 
def asin_value(num):
    if num<-1 or num>1:
        return "none"
    result=math.degrees(math.asin(num))
    return result
def acos_value(num):
    if  num<-1 or num>1:
     return "none"
    result=math.degrees(math.acos(num))
    return result
def atan_value(num):
    if num <-1 or num >1:
        return "none"
    result=math.degrees(math.atan(num))
    return result
    

#nunmber system conversions
def decimal_toBinary(num):
    return bin(num).replace("0b"," ")
def decimal_toOctal(num):
    return oct(num).replace("0o"," ")
def decimal_toHexadecimal(num):
    return hex(num).replace("0x"," ")

num=float(input("enter a num :"))
while True:
        opr=input("enter a operator ")
        if opr=="0": 
            print("final result:",exit)
            break
        if opr=="*":
            num=multiply(num)
            print("result=",(num))
        elif opr=="+":
            num=add(num)
            print("result=",(num))      
        elif opr=="-":
            num=subtract(num)
            print("result=",(num))
        elif opr=="/":
            num=division(num)
            print("final result:",num)
        elif opr=="power":
            num=power(num)
            print(" result:",num)
        elif opr=="percentage":
            num=percentage(num)
            print(" result:",num)
        elif opr=="sin":
            num=sin_func(num)
            print(" result:",num)
        elif opr=="cos":
            num=cos_func(num)
            print(" result:",num)
        elif opr=="tan":
            num=tan_func(num)  
            print(" result:",num)
        elif opr=="sqrt":
            num=sqrt(num)
            print(" result:",num)
        elif opr=="log":
            num=log(num)
            print(" result:",num)
        elif opr=="factorial":
            num=factorial(num)
            print(" result:",num)
        elif opr=="asin":
            num=asin_value(num)
            print(" result:",num)
        elif opr=="acos":
            num=acos_value(num)
            print(" result:",num)
        elif opr=="atan":
            num=atan_value(num)
            print("result=",num)
        elif opr=="decimal_toBinary":
            print("result=",decimal_toBinary(int(num)))
        elif opr=="decimal_toOctal":
            print("result=",decimal_toOctal(int(num)))
           
        elif opr=="decimal_toHexadecimal":
            print("result=",decimal_toHexadecimal(int(num)))
        else:
            print("exit")