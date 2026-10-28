num=int(input("enter a number :"))
original=num
digit=len(str(num))
total=0
while num>0:
    digits=num%10
    digits=digits**digit
    total=total+digits
    num=num//10

if total==original:
    print("armstrong")

else:
    print("not")


