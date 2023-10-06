"""
 Given a list, find the highest number in the list
"""

num_list = [23,56,43,90, 344.55, 100]

highest_num = 0 

for num in num_list:
    if highest_num > num:
        highest_num = num

print(f"The biggest number is {highest_num}")