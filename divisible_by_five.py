# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

def print_divisible_by_5(number_list):
    for number in number_list:
        if number % 5 == 0:
            print(number)
   
