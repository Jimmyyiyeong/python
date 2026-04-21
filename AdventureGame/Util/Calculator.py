#Calculator class that can take in arguments to solve simple math

import math

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a,*args):
    total = a
    for num in args:
        total -= num
    return total

def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total

def divide(a,b):
    total = a / b
    return total

def remainder(a,b):
    remainder_of_sum = a % b
    return remainder_of_sum

def calculate_area_of_circle(r):
    area = r * r * math.pi
    return area

def calculate_area_of_triangle(b,h):
    return b * h / 2

def calculate_height_of_triangle(a,b,c):
    return a * b / c

def pythagoras_theorem(a,b):
    return math.sqrt(a**2 + b**2)

def percent(part, whole):
    if whole == 0:
        return 0
    return round((part / whole) * 100, 2)

def celsius_to_farenheit(celsius):
    return (celsius * 9 / 5) + 32

def farenheit_to_celsius(farenheit):
    return (farenheit - 32) * 5 / 9