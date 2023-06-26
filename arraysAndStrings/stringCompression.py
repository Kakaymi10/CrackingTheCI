'''
String Compression: Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the 
"compressed" string would not become smaller than the original string, your method should return 
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

input=aabcccccaaa
output=a2blc5a3
'''

def compression(string):
    Hash = {}
    compressed = ''
    count = 0
    while count < len(string):
        if (count + 1) < len(string) and string[count] == string[(count + 1)]:
            Hash[string[count]] = Hash.get(string[count], 0) + 1
        else:
            Hash[string[count]] = Hash.get(string[count], 0) + 1
            compressed += string[count] + str(Hash[string[count]])
            Hash = {}
        count += 1
    if len(string) < len(compressed):
        return string
    return compressed

print(compression('aabcccccaaa'))
print(compression('abca'))
print(compression('aabcccccaaadkaaapp'))
print(compression('aabcccccaaawwwweerr'))
