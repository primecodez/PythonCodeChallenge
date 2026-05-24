#Writing a program that can open and read the intro file

with open("Day_11/intro.txt","r") as file :
     cont = file.read()
     print(cont)