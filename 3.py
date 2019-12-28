'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# this file is created by Rini Ariyanti_Arkademy_3
def printWords(param):
    vocal = ['a','i','u','e','o','A','I','U','E','O']
    vlist = [s for s in param if s in vocal]
    clist = [s for s in param if s not in vocal]
    rlist = vlist + clist
    for r in range(0,len(rlist)): print(rlist[r])
    

printWords("ARKADEMY")