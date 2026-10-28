numbers = [4, 7, 2, 7, 9, 2, 4]
seen = []

for num in numbers:
    if num in seen:
        print("First duplicate:", num)
        break
    seen.append(num)