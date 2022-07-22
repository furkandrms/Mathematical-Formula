
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

def equation_second_degree():
    
    a=int(input())
    b=int(input())
    c=int(input())
     
    while True: 
        
        delta = (b**2 -4*(a*c))
        if (delta > 0):
            x1 = (-b + (delta**0.5))/2*a
            x2 = (-b- (delta**0.5))/2*a
            return x1,x2
        elif delta == 0:
            x1 = (-b/2*a)
            return x1
        else:
            print("It's not values in this equation")
        return equation_second_degree

def arithmetic_average(*x): 
    
    sum = 0
    values = [] 
    
    while True:
        for i in (x): 
            values.append(i)
            sum += i
        sum /= len(values) 
        return sum
    return values

def measure_meter(): 
    x = int(input())
    y = input()
    
    for i in y:
        x *= 100 
        if ( y == "inch"):
            
            x /= 2.54
            return x
        elif ( y == "foot"):
            x /= (2.54*12)
            return x
        elif ( y == "yard"):
            x /= (2.54*12*3)
            return x
        elif (y == "mil"):
            x /= (2.54*12*3*1760)
            return x
        else:
            return x, print("centimeter")
        return y
    return measure_meter()
             

            
    
           
    




    

            

        

 
            
            


