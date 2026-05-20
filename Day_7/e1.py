#Exercises: Day 12
#function which generates a six digit/character random_user_id.
num,b= map(int,input("Enter the number of characters to be in user_id:").split())
n = num
import random 
import string
def user_id():
    char = string.ascii_letters + string.digits + string.punctuation
    user_id = ''
    for i in range(n):
        user_id += random.choice(char)
    return user_id
for  k in range(b):
   print("User_id:", user_id())

