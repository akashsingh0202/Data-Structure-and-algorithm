num=int(input("enter a number :"))
is_prime = True
if num>=2:
    for i in range(2,num):
        if num % i == 0:
         is_prime = False
         break
else:
    is_prime=False
        
          

if(is_prime):
    print("prime number ")

else:
    print("not a prime number")