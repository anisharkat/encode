import os 
os.system("clear")
while True :
    from hashlib import md5
    x = input("Enter your word :  ")
    y = md5 (x.encode()).hexdigest()
    print("Your code is : ", y)