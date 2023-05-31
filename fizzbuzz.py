def fizzbuzz(arr):
    for number in arr:
        if number % 3 == 0 and number % 5 == 0:
            print("Fizzbuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")


def fizzbuzz1(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")


nums = [9, 13, 18, 20, 25, 30, 32, 33, 35, 38, 42, 46, 50, 51, 58, 67]

fizzbuzz(nums)

for num in nums:
    fizzbuzz1(num)
