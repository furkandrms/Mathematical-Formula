
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
        
        
def exponential_number(a,b): #Uslu Ifadeler
    return a**b    

def absolute_value(a): #Mutlak Değer İşlemi Fonksiyonu 
    
    while True:
        if a < 0: 
            a *= -1
            return a
        else: 
            return a 


    

            

        

 
            
            


