# numbers = [2, 5, 2, 8, 5, 2, 9]
# target_2 = 2
# count_2=0
# target_5 = 5
# count_5=0
# target_8 = 8
# count_8=0
# target_9 = 9
# count_9=0

# for num in numbers:
#     if num==target_2:
#         count_2+=1

#     elif num==target_5:
#         count_5+=1
#     elif num==target_8:
#         count_8+=1

#     else:
#         count_9+=1

# print("count of 2: " ,count_2)
# print("count of 5: " ,count_5)
# print("count of 8: " ,count_8)
# # print("count of 9: " ,count_9)
    

    


numbers = [2, 5, 2, 8, 5, 2, 9]
seen = []

for num in numbers:
    if num not in seen:
        count = 0

        for other in numbers:
            if other == num:
                count += 1

        print(num, "appears", count, "times")
        seen.append(num)

        
        