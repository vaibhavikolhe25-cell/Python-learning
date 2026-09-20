import random
n = random.randint(1,100)
a = -1
guesses = 0
while (a != n):
    a = int(input("guess the number: "))
    guesses += 1
    
    if(a >n):
        print("lower number please")
        

    elif(a<n):
        print("higher number please")
        
        

print(f"you have guess the number {n} correctly in {guesses}attempts")
            