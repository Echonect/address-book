## Tutorial copied from NeuralNine https://youtu.be/rHTwjV1ORUQ ##

import random

upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXZY"

lowerCaseLetters = upperCaseLetters.lower()

digits = "0123456789"

symbols = "-_,!@#$%^&*()[]+=<>./?"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += upperCaseLetters

if lower:
    all += lowerCaseLetters

if nums:
    all += digits

if syms:
    all += symbols

length = 20

amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)