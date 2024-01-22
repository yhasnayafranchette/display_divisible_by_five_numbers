# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

#List numbers and check if divisible by 5
def print_divisible_by_5(number_list):
    for number in number_list:
        if number % 5 == 0:
            print(number)

#Display numbers divisible by 5
numbers = 10, 20, 33, 46, 55
print ("Given list is", numbers)
print("Numbers divisible by 5:")
print_divisible_by_5(numbers)