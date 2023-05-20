"""
Assignment 5: Spelling Numbers

Author: Alex Yazdani
CWID: 20399751
Date: 11/1/2022

This file uses four functions provided by Mike Murphy that are useful for converting numbers between 0 and 1000 to spelled out words.
The spell() function, created by myself, takes an input between -999,999,999 and 999,999,999, and converts it into words.
It will produce an error if the number is out of range and will round any floats to the nearest int.
The main() of this file acts as a test program, which prints multiple test points returned by the spell() function.
"""

def digitName(digit):
    """
    Returns a string containing the English word naming "digit".
    "digit" must be between 1 and 9, inclusive
    """
    if digit == 1: return "one"
    if digit == 2: return "two"
    if digit == 3: return "three"
    if digit == 4: return "four"
    if digit == 5: return "five"
    if digit == 6: return "six"
    if digit == 7: return "seven"
    if digit == 8: return "eight"
    if digit == 9: return "nine"
    return ""

def teenName(number):
    """
    Returns a string containing the English word naming "number".
    "number" must be between 10 and nineteen inclusive.
    """
    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    if number == 13: return "thirteen"
    if number == 14: return "fourteen"
    if number == 15: return "fifteen"
    if number == 16: return "sixteen"
    if number == 17: return "seventeen"
    if number == 18: return "eighteen"
    if number == 19: return "nineteen"
    return ""

def tensName(number):
    """
    Returns a string containing the English word for just the tens part of "number".
    "number" must be an integer between 20 and 99 inclusive.
    """
    if number >= 90: return "ninety"
    if number >= 80: return "eighty"
    if number >= 70: return "seventy"
    if number >= 60: return "sixty"
    if number >= 50: return "fifty"
    if number >= 40: return "forty"
    if number >= 30: return "thirty"
    if number >= 20: return "twenty"
    return ""

def spellNumberLessThanThousand(number):
    """
    Returns a string containing the English words that spell out "number".
    "number" must be between 0 and 1000, exclusive.
    """
    part = number    # the part that still needs to be converted
    name = ""        # the name of the number
    if part >= 100:
        name = digitName(part //100) + " hundred"
        part = part % 100
    if part >= 20:
        name = name + " " + tensName(part)
        part = part % 10
    elif part >= 10 :
        name = name + " " + teenName (part)
        part = 0
    if part > 0:
        name = name + " " + digitName (part)
    return name

def spell(number):
    """
    Uses the above functions to take an integer number between -999,999,999 and 999,999,999, and return the number spelled out in words.
    If the magnitude of the number is too large the function returns an error.
    If a float is provided, it is rounded to nthe nearest int.
    """
    part = round(abs(number))
    if part > 999999999:
        errmessage = "Magnitude of value is too large.  Accepted range: -999,999,999 to 999,999,999."
        return errmessage
    if number == 0:
        name = "zero"
    elif number > 0:
        name = ""
    else:
        name = "negative "
    if part >= 1000000:
        for size in [100000000, 10000000, 1000000]:
            if part >= size:
                name = name + spellNumberLessThanThousand(part // 1000000) + " million "
                part = part % 1000000
    if part >= 1000:
        for size in [100000, 10000, 1000]:
            if part >= size:
                name = name + spellNumberLessThanThousand(part // 1000) + " thousand "
                part = part % 1000
    name = name + spellNumberLessThanThousand(part)
    return name

def main():
    """
    Test program for spell() function
    """
    print(spell(1234567890)) 
    print(spell(3345.768))
    print(spell(123123))
    print(spell(123456789)) 
    print(spell(456678))  
    print(spell(66))      
    print(spell(-123456789))
    print(spell(-456678) )     
    print(spell(-418))     
    print(spell(0))
    print(spell(10004))

if __name__ == "__main__":
    main()

r"""
PS C:\Users\ayazdani\PythonProjects\CSLab5>  c:; cd 'c:\Users\ayazdani\PythonProjects\CSLab5'; & 'C:\Users\ayazdani\AppData\Local\Programs\Python\Python310\python.exe' 'c:\Users\ayazdani\.vscode\extensions\ms-python.python-2022.16.1\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher' '51148' '--' 'c:\Users\ayazdani\PythonProjects\CSLab5\spellNumber.py' 
Magnitude of value is too large.  Accepted range: -999,999,999 to 999,999,999.
 three thousand three hundred forty six
one hundred twenty three thousand one hundred twenty three
one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
four hundred fifty six thousand six hundred seventy eight
 sixty six
negative one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
negative four hundred fifty six thousand six hundred seventy eight
negative four hundred eighteen
zero
 ten thousand  four
"""