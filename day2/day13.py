# numbers = [-4, -3, -2, -1, 0, 2, 4, 6] 

# result=[num for num in numbers if num <= 0]
# print(result) 

# exercise 2 flattened list 

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list) 

# exercise 3  using a list comprehension create the following list of tuples 

list_of_tuples=[(x,1,x,x**2,x**4,x**5) for x in range(11)]

print(list_of_tuples)