# List comprehension:

#synatx
#new_list = [new_item for item in list]
numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)


name = "Abby"
name_list = [letter for letter in name]
print(name_list)


num_range = range(1,6)
range_list = [num*2 for num in range(1,6)]
print(range_list)

# conditional list comprehension:

# new_list = [new_item for item in list if test]

nums = [1,2,3,4,5]
even_nos = [n for n in nums if n % 2 == 0]
print(even_nos)