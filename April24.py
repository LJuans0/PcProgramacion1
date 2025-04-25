#historial de abajo para arriba
import math

"""🧠 Problem 3: Number Puzzle
Take a number from the user.

If the number is divisible by both 3 and 5, print "FizzBuzz".

If only divisible by 3 → "Fizz".

If only by 5 → "Buzz".

If neither, but it’s a perfect square, print "Square".

If nothing matches, print "Nothing interesting"."""
def Pregunta_3(numb:int):
    if numb%3==0 and numb%5==0:
        return "FizzBuzz"
    elif numb%3==0:
        return "Fizz"
    elif numb%5==0:
        return "Buzz"
    elif math.isqrt(numb)**2==numb:
        return "Square"
    else:
        return "Nothing interesting"

"""print(Pregunta_3(15))
print(Pregunta_3(16))
print(Pregunta_3(49))
print(Pregunta_3(47))"""

"""🧠 Problem 2: Work Shift Bonus
A company pays workers based on shift and hours:

Morning shift: base $10/hr

Evening shift: base $12/hr

Night shift: base $15/hr

If the worker did more than 8 hours in a day, every extra hour is paid 1.5x the base rate.

Ask user for shift type and hours, and calculate total pay."""

def Pregunta_2(typeshift:str, hours:float):
    totalpay=0
    if typeshift=="Morning":
        if hours<=8:
            totalpay=hours*10
        else:
            totalpay = (hours-8)*1.5*10+80
    elif typeshift=="Evening":
        if hours<=8:
            totalpay=hours*12
        else:
            totalpay = (hours-8)*1.5*12+96
    elif typeshift=="Night":
        if hours<=8:
            totalpay=hours*15
        else:
            totalpay = (hours-8)*1.5*15+120
    return totalpay
"""print(Pregunta_2("Morning",6))
print(Pregunta_2("Evening",10))
print(Pregunta_2("Night",9))"""


"""🧠 Problem 1: Electric Bill Calculation
The price per kWh varies with consumption:

First 100 kWh: $0.15 per kWh

Next 100 (101–200): $0.20 per kWh

Above 200: $0.30 per kWh

Write a program that calculates the total cost based on the number of kWh consumed."""
def Pregunta_1(kwhconsumidos:int):
    dollars=0
    if kwhconsumidos<=100:
        dollars=kwhconsumidos*0.15
    elif 100<kwhconsumidos<=200:
        dollars=(kwhconsumidos-100)*0.20+15
    elif kwhconsumidos>200:
        dollars = (kwhconsumidos-200) * 0.30 + 35
    return dollars
"""print(Pregunta_1(80))
print(Pregunta_1(150))
print(Pregunta_1(250))"""