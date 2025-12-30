from collections import Counter

def isAnagram(s1, s2) ->bool:
    if Counter(s1) == Counter(s2):
        return True
    else:
        return False

string1 = "abc"
string2 = "cba"
print(isAnagram(string1, string2))