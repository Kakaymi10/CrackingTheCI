""" Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation 
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 

EXAMPLE 
Input: Tact Coa 
Output: True (permutations: "taco cat", "atco eta", etc.) """

def palindromePermutqtion(string):
    #create Hash table to stroe the occurences of every charchter
    Hash = {}
    #odd to check if there is 0 or 1 odd occurence
    odds = 0

    #operation to stores the occurences in the Hash
    for i in string:
        Hash[i] = Hash.get(i, 0) + 1
      
    #Checking the number of odds ocurrences
    for ele in Hash:
        if Hash[ele] % 2 == 1:
            odds += 1

    #return True if it palindrome permutation, otherwise False
    return odds <= 1
    
print(palindromePermutqtion('muuss'))
print(palindromePermutqtion('muussm'))
print(palindromePermutqtion('muussma'))
print(palindromePermutqtion('muussmaj'))
