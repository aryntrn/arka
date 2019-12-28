'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# this file is created by Rini Ariyanti_Arkademy_5
from random import randint
def createMatrix(ordo):
    # create element matrix randomly
    mtx=[]
    diag1,diag2=0,0
    for i in range(0,ordo):
        mtx_row=[]
        for j in range(0,ordo):
            numran = randint(0,10)
            mtx_row.append(numran)
            if i==j: diag1+=numran
            if j==(ordo-i-1): diag2+=numran 
        mtx.append(mtx_row)
        print(mtx_row)
    print("Total:", diag1*diag2)

createMatrix(3)
    