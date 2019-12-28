'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# this file is created by Rini Ariyanti_Arkademy_4
def sortNumber(param):
    numlist = [s for s in param if s.isdigit()]
    if not numlist: print("No number found in parameter!")
    else:
        result=""
        numlist.sort()
        for r in range(0,len(numlist)): result+=numlist[r]
        print(result)

sortNumber("jsuad738298")
