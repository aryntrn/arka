'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# this file is created by Rini Ariyanti_Arkademy_1
import json

def getBiodata(name, age):
    data = {
        "name": "Rini Ariyanti",
        "age" : 24,
        "address": "Gg Sakura No 5, Jongke Kidul RT 07 RW 24, Sendangadi, Mlati, Sleman, DIY",
        "hobbies": [
            "drawing",
            "programming",
            "travelling"
        ],
        "is_married": False,
        "list_school" : [
            {
                "name": "SMA N 4 Yogyakarta",
                "year_in": 2010,
                "year_out": 2013,
                "major" : "IPA",
            },
            {
                "name": "Universitas Gadjah Mada",
                "year_in": 2013,
                "year_out": 2016,
                "major" : "Komputer dan Sistem Informasi",
            },
            {
                "name": "Universitas Amikom Yogyakarta",
                "year_in": 2017,
                "year_out": 2019,
                "major" : "Sistem Informasi",
            },
        ],
        "skills": [
            {
                "skill_name" : "digital drawing",
                "level" : "beginner",
            },
            {
                "skill_name" : "backend programming using Java, PHP",
                "level" : "intermediate",
            },
            {
                "skill_name" : "Python programming for data science",
                "level" : "beginner",
            },
        ],
        "interest_in_coding" : True
    }
    
    if name == data.get('name') and age == data.get('age') : print(json.dumps(data))
    else : print("Sorry, I don't know about", name, ",", age, "y.o")

getBiodata("Rini Ariyanti", 24)
getBiodata("Ariyan", 22)
