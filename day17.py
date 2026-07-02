# # # # try:
# # # #     print(10 + '5')
# # # # except:
# # # #     print('Something went wrong')

# # # try:
# # #     name = input('Enter your name:')
# # #     year_born = input('Year you were born:')
# # #     age = 2019 - year_born
# # #     print(f'You are {name}. And your age is {age}.')
# # # except:
# # #     print('Something went wrong')

# # try:
# #     name = input('Enter your name:')
# #     year_born = input('Year you born:')
# #     age = 2019 - int(year_born)
# #     print(f'You are {name}. And your age is {age}.')
# # except TypeError:
# #     print('Type error occur')
# # except ValueError:
# #     print('Value error occur')
# # except ZeroDivisionError:
# #     print('zero division error occur')
# # else:
# #     print('I usually run with the try block')
# # finally:
# #     print('I alway run.') 

# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

# # unpacking
# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(*lst))  # 15

# for index, item in enumerate([20, 30, 40]):
#     print(index, item) 


# Challenge  zip() function Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'] 

*nordic_countries,es , rus= names 
print(nordic_countries,es,rus) # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']  
