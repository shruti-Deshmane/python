#password_generator.py
import random
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~@#$%^&*+-/,';|"
while True:
 pass_len=int(input("enter length of password  =  "))
 count=int(input("number of pass you want to generate  =  "))
 for i in range(0,count):
    password= ""
    for j in range(0,pass_len):
        pass_char=random.choice(letters)
        password=password+pass_char
    print ("password generated is ",password)
 repeat =input("want more passwords? ")

 if repeat=="no" or repeat=="NO":
   break

 



