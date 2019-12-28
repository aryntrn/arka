'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# this file is created by Rini Ariyanti_Arkademy_2
import re

def is_name_valid(name_param):
    pattern = '[A-Z]{3,}'
    if re.search(pattern, name_param): 
        return True 
    else: 
        return False
    
def is_age_valid(age_param):
    pattern = '[+]?[0-9]?\d{2}'
    if re.match(pattern, str(age_param)): 
        return True 
    else: 
        return False
    
def is_username_valid(username_param):
    pattern = '[a-z]{4}[\_\.][0-9]{3}$'
    if re.match(pattern, username_param): 
        return True 
    else: 
        return False
    

print(is_name_valid("RIN"))
print(is_name_valid("RI"))

print(is_age_valid(19))
print(is_age_valid(1))

print(is_username_valid("rini_290"))
print(is_username_valid("rini.20"))
print(is_username_valid("rini.290"))