#write functions here, dont add input('') statements here !
def is_prime(c):
    if c <=1: # numbers less than 1 are not prime
        return False
    for i in range (2, int(c**0.5)+ 1): # check divisors up to the square root
        if c % i == 0:
         return False 
    return True
# test cases 
print(is_prime(4)) # expected output : False
print(is_prime(5))# expected output : True
print(is_prime(11)) # expected output :True
