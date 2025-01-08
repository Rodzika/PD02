#2.Uzd

number = int(input("Enter the number : "))

factorial = 1

if ( number < 0):
    print("cant Compute factorial for Negative Numbers")
elif (number < 2):
    print("{}! = {}".format(number, factorial))
else:
    for num in range(number, 1 -1):
        factorial = factorial * num
    
    print("{}! = {}".format(number, factorial))

#3.uzd

def factorial(n):
    
    factorial= 1
    
    for i in range(n):
        factorial*=i+i
        return factorial
    
    for i in rango(10):
        print(factorial(i))

#4.Uzd

n=int(input("Enter the number="))
while n>=0:
    print(n,end=' ')
    n=n-1

#5.Uzd

num = int(input("Enter the number of rows:"))
for i in range(num, 0,-1):
    for j in range(0, num-i):
        print(end=" ")
    for j in range(0,i):
        print("*", end =" ")
    print()
    

#6.Uzd

input random
answer = random.randrange(1, 11)
chance = 0
while chance < 5:
    guess = int(input("Guess number between 1 and 10: "))
    
    if guess == answer:
        print("Uzminēts!")
    if guess < answer :
        print("Augstāks!")
    if guess > answer:
        print("Zemāks")
        
        chance += 1
    if chance == 5:
        print("Spēle peigusies. atbilde bija:", answer)
        