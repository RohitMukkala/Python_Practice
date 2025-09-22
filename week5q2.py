"""Write a Python program to find sum of all odd numbers between 1 to n."""


n = int(input("Enter a number: "))
int =1
sum=0
while int<=n:
    if(int%2==1):
        sum+=int
    int=int+1
print(sum)
