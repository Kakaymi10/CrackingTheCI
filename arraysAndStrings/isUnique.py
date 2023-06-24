#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you 
#cannot use additional data structures?


def isUnique(string):
    #list of hashTables in the len of the ASCII
    hashSet = [False] * 128
    #loop through the string
    for i in range(len(string)):
        #get an id for every string
        id = ord(string[i])
        if hashSet[id]:
            return False
        hashSet[id] = True
    return True
        
print(isUnique('Moussq'))
print(isUnique('amigo'))
print(isUnique('amigos'))
print(isUnique('amigoss'))
print(isUnique('amigosin'))
