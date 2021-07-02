# School Assignment MVM 

#1. Swap values of two varaibles 
def swap(a,b):
    a,b = b,a 
    print(a,b)

#Example 
A = 200 
B = 2200
swap(A,B) 
print("\n")


#2. Compute Simple Interest 
def SI(p,t,r):
    SI = (p * t * r)/100
    print('The Simple Interest is :', SI)

#Example
SI(2600,8,5)
print("\n")

#3. Convert Celcius to farenheit 
def convert(num):
    num = float(num)
    f = (num*9/5) + 32
    print(num,"°C in farenheit is :",f,"°F") 
     
#Example 
convert(30.1)
print("\n")

#4. Calulate average marks 
def average(*marks):
    total = sum(marks)
    terms = len(marks)
    avg = total/terms 
    print("The average of given marks is :",avg)

#Example
average(100,50,75)
print("\n")


# Arivoli.R   
# XI-A7 
