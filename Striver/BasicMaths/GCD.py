def gcd(n1, n2):
    
    gcd = 1
    
    for i in range(1, min(n1, n2) + 1):
        
        if n1 % i == 0 and n2 % i == 0:
            
            gcd = i
            
    return gcd
    


n1 = 12
n2 = 6

call = gcd(n2 , n1)
print(call)





def find_the_gcd(h1,h2):
    
    # intnlize a gcd = 1 because 1 is all num are divided 
    
    gcdh = 1
    
    
    # for loop to chek both num h1 and h2
    for i in range(1, min(h1, h2) + 1):
        
        # chek the codition both are divided or not both are divided then show a one similer num other wise show a 1
        if h1 % i == 0 and h2 % i == 0:
            
            gcdh = i
            
            
    return gcdh
            
    
    

h1, h2 = 11, 21

call = find_the_gcd(h1, h2)
print(call)



def gcd_find(s1,s2):
    
    # intli gcd 1 
    
    gcd = 1
    
    # for loops
    
    
    for i in range(1, min(s1,s2) +1):
        
        if s1 % i == 0 and s2 % i == 0:
            
            gcd = i
            
    return gcd
    

s1,s2 = 22 ,12

call = gcd_find(s1, s2)

print(call)



# LMC and GCD

import math
def lmc_gcd(a,b):
    
    gcd_value = math.gcd(a,b)
    
    
    lcm_value = abs(a * b ) // gcd_value
    
    return [lcm_value, gcd_value]
    
    
    
    
    
    
a, b = 10 , 5
print(lmc_gcd(a,b))