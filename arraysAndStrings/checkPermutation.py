'''Check Permutation: Given two strings, write a method to decide if one is a permutation of the 
other. '''
def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    hash1 = [0]*128
    hash2 = [0]*128
    for i in range(len(str1)):
        id = ord(str1[i])
        hash1[id] = int(hash1[id]) + 1
    for i in range(len(str2)):
        id = ord(str2[i])
        hash2[id] = int(hash2[id]) + 1
    
    return hash1 == hash2
    
print(checkPermutation('moussa', 'oussam'))
print(checkPermutation('minf', 'mons'))
print(checkPermutation('dhg', 'fdwwe'))
print(checkPermutation('dhg', 'gdh'))
print(checkPermutation('dhgew', 'gdhwe'))
