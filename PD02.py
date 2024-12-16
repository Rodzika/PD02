#2.Uzd

int main()

int num, count = 1, sum = 0;

print f("Enter a positive number\n");
scanf("%d" , &num);

printf("um of natural numbes from 1 to%d is:\n", num)
while(count <= num)
{
 
 sum = sum + count;
 printf("%d ", count);
 count++;
 
 if(count > num)
 {
  printf(" = %d\n", sum);
  }
 else
 {
  printf("+ ");
  }
 
 }

return 0;

#3.uzd

int main()

int num, count, fact = 1;

print("Enter a number to find its Factorial\n");
scanf("%d", &num);

for(count = 1; count <= num; count++)
{
 fact = fact * count;
 }

printf("Factorial of %d is %d\n", num, fact);

return 0;

#4.Uzd

void main()
{
 int n;
 clrscr()
 printf("\n Enter the number: ");
 scanf("\n xd", &n);
while(n>0)
{
 printf("xd,",n)
 --n;
 }
 {
  printf("=xd",num[i]);
  }
 getch();
 }

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
        