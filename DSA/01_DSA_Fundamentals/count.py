# Count Even and Odd Numbers

numbers = [12, 7, 9, 24, 16, 5, 8]
count_even=0
count_odd=0

for num in numbers :
    if num%2==0:
        count_even+=1

    else:
        count_odd+=1

print("count of even number s :",count_even)
print("count of odd number s :",count_odd)


