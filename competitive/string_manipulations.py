# Question 1 : How to Print duplicate characters in a String?
print("# Question 1 : How to Print duplicate characters in a String?")
hashmap = dict()
char = "abcdefghijklmnopqrstuvwxyz"
character = "mfeiojfierofer"

for c in list(char):
    hashmap[c] = 0

# Duplicate strings
for c in list(character):
    hashmap[c] = hashmap[c] + 1
    if hashmap[c] == 2:
        print(c)

# for key, value in hashmap.items():
#     if value > 1:
#         print(key, " : ", value)

print("===========================================================")
print("# Question 2 : How to check if two Strings are anagrams of each other?")
# Question 2 : How to check if two Strings are anagrams of each other?

ip_s1 = "top"
ip_s2 = "pot"


# Solution 1 : Using sorted
def is_anagram(ip_str1, ip_str2):
    if len(ip_str1) != len(ip_str2):
        return False
    return sorted(ip_str1) == sorted(ip_str2)


print("is anagram: {0}".format(is_anagram(ip_s1, ip_s2)))
print("is anagram: {0}".format(is_anagram("ip_s1", "ip_s2")))
print("is anagram: {0}".format(is_anagram("ram", "arm")))
print("is anagram: {0}".format(is_anagram("malayalam", "yamalamal")))
print("is anagram: {0}".format(is_anagram("sabrimala", "sabkimala")))

# Question 3 : How to reverse String using Iteration and Recursion?
mystring = "sentimenta fanta"

# 1. Using iteration
i = len(mystring) - 1
revstringarr = []
for i in range(i, 0, -1): # N
    revstringarr.append(mystring[i])
revstring = ''.join(revstringarr)  # N


# 2. Recursion
# TBD


# Question 4 : Get wrong answer. (From meta)
def getWrongAnswers(N: int, C: str) -> str:
    i = 0
    X = list()
    for x in C:
        if x == 'A':
            X.append('B')
        else:
            X.append('A')
        i = i + 1
    return ''.join(X)


print(getWrongAnswers(3, "ABA"))
