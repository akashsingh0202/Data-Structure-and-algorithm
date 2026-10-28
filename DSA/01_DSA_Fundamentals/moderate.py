numbers = [34, 12, 89, 45, 67]
greatest=numbers[0]
second_greatest=float('-inf')
for num in numbers:
    if num>greatest:
        second_greatest=greatest
        greatest=num
    elif num>second_greatest and num<greatest:
        second_greatest=num

print(second_greatest)