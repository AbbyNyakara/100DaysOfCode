with open("file1.txt") as file1:
    numlist1 = [int(num.strip()) for num in file1.readlines()]
    print(numlist1)

with open("file2.txt") as file2:
    numlist2 = [int(num.strip()) for num in file2.readlines()]
    print(numlist2)

common_nums = [num for num in numlist1 if num in numlist2]
print(common_nums)