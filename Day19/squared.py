numbers = [1,1,2,4,56,77,34]

squared_numbers = [num**2 for num in numbers]

#print(squared_numbers)

# filter the even numbers: 

#list_of_nums = input().split(',')
list_of_nums = ['12', "3", '4', '5']

even_nums = [num for num in list_of_nums if int(num) % 2 ==0]
print(even_nums)