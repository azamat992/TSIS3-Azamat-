#1 Grams to Ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams
grams_amount = float(input("Enter grams: "))
print(f"{grams_amount:.2f} grams is {grams_to_ounces(grams_amount):.2f} ounces.")

#2 Fahrenheit to celsium
def faren_to_cent(faren):
    return (faren-32)*(5/9)
faren_amount = float(input("Enter amount of fahrenheit: "))
print(f"{faren_amount:.2f} fahrenheit is {faren_to_cent(faren_amount):.2f} celsium.")

#3 Rabits and chickens
def solve(heads, legs):
    chickens = heads
    rabbits = 0
    while chickens >= 0:
        total_legs = chickens * 2 + rabbits * 4
        if total_legs == legs:
            return chickens, rabbits
        chickens -= 1
        rabbits += 1
    return None
result = solve(35, 94)
if result is not None:
    chickens, rabbits = result
    print(f"There are {chickens} chickens and {rabbits} rabbits.")
else:
    print("No solution found.")

#4 Prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = list(map(int, input_numbers.split()))
prime_numbers = filter_prime(numbers_list)
print(f"Input numbers: {numbers_list}")
print(f"Prime numbers: {prime_numbers}")

#5 Permutation 
from itertools import permutations
def print_permutations():
    user_input = input("Enter a string: ")
    perms = permutations(user_input)
    print("All permutations:")
    for perm in perms:
        print(''.join(perm))
print_permutations()

#6 Reversed sentence
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print("Reversed sentence:", result)

#7 3 to 3 Somewhere
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False
user_input = input("Enter a list of integers separated by spaces: ")
nums_list = list(map(int, user_input.split()))
result = has_33(nums_list)
print(f"The list {nums_list} contains a 3 next to a 3: {result}")

#8 007 in Order
def spy_game(nums):
    spy_code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == spy_code[index]:
            index += 1
            if index == len(spy_code):
                return True
    return False
user_input = input("Enter a list of integers separated by spaces: ")
nums_list = list(map(int, user_input.split()))
result = spy_game(nums_list)
print(f"The list {nums_list} contains 007 in order: {result}")

#9 Volume of sphere
import math
def sphere_volume(radius):
    if radius < 0:
        return "Radius should be non-negative."
    else:
        volume = (4/3) * math.pi * radius**3
        return volume
user_radius = float(input("Enter the radius of the sphere: "))
result = sphere_volume(user_radius)
print(f"The volume of the sphere with radius {user_radius} is: {result}")

#10 Unique elements in list
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
user_input = input("Enter a list of elements separated by spaces: ")
input_list = list(map(int, user_input.split()))
result = unique_elements(input_list)
print(f"The list with unique elements: {result}")

#11 Polindrome or not
def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]
user_input = input("Enter a word or phrase: ")
result = is_palindrome(user_input)
if result:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")

#12 Histogram
def histogram(numbers):
    for num in numbers:
        print('*' * num)
user_input = input("Enter a list of integers separated by spaces: ")
numbers_list = [int(x) for x in user_input.split()]
histogram(numbers_list)

#13 Guess KBTU
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_the_number()
