# Topic 1: Introduction to DSA
# Easy Question 1: Find the largest number

numbers = [34, 12, 89, 45, 67,12]
greatest=numbers[0]

for num in numbers:
    if num>greatest:
        greatest=num

print(greatest)
