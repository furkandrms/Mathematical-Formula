
from cmath import sqrt


def summation(*number): #Toplama İşlemi Fonksiyonu 
    
    numbers = []
    equal = 0
    
    while True:
        for i in number: 
            
            numbers.append(i)
            equal += i 
        return equal
    return numbers

def extraction(a,b): #Çıkarma İşlemi Fonksiyonu 
    return a-b

def multiple(*number): #Çarpma İşlemi Fonksiyonu 
    
    numbers = []
    equal = 1
    
    while True: 
        for i in number: 
            equal *= i 
        return equal 
    return numbers

def divide(a,b):
    
    while True: 
        if ( a % b == 0): 
        
            return a // b
        
        else:
            return a / b 

def absolute_value(a): #Mutlak Değer İşlemi Fonksiyonu 
    
    while True:
        if a < 0: 
            a *= -1
            return a
        else: 
            return a 

             
def exponential_number(a,b): #Uslu Ifadeler
    return a**b    

def square_root(x): 
    return x**0.5

def rooted_expressions(a): 
    return a**1/a

def equation_second_degree(a,b,c):
    
    values = []
    while True:
        a = int(input())
        b = int(input())
        c = int(input())
        delta = (b**2 - 4(a*c))
         
        if (delta > 0):
            x1 = ((-b + sqrt(delta))/2*a)
            x2 = ((-b - sqrt(delta))/2*a)   
        elif (delta == 0):
            x1 = x2 = (-b / 2*a)
        else: 
            return "it's not any values"
    return values

         
         
    




    

            

        

 
            
            


