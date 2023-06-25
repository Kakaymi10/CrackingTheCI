''' One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away. 
EXAMPLE 
pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bake -> false  '''

def oneWay(str1, str2):
    Hash = {}
    odds = 0
    insert = len(str1) + 1
    remove = len(str1) - 1
    edit = len(str1)
    
    for i in str1:
        Hash[i] = Hash.get(i, 0) + 1

    for i in str2:
        Hash[i] = Hash.get(i, 0) + 1

    for key in Hash:
        if  Hash[key]  % 2 == 1:
            odds += 1
    
    if len(str2) == edit or len(str2) == insert or len(str2) == remove:
        return odds <= 2
    return False
    

print(oneWay('pale', 'ple'))
print(oneWay('pale', 'pales'))
print(oneWay('pale', 'bale'))
print(oneWay('pale', 'bake'))
print(oneWay('pale', 'bakes'))
print(oneWay('pale', 'pa'))
