'''
String Rotation: Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring 
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one 
call to i5Sub5tring (e.g., "waterbottle" is a rotation of"erbottlewat"). 
'''
def isSubstring(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return (s2 in s1s1)
    return False
        
print(isSubstring('waterbottle', 'waterbottle'))
print(isSubstring('waterbottle', 'waterbottler'))
print(isSubstring('waterbottle', 'terbottlewa'))
