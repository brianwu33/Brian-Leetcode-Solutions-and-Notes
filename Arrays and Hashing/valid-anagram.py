#Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = dict()
        for letter1 in s:
            if letter1 in counter.keys():
                counter[letter1] += 1
            else:
                counter[letter1] = 1

        for letter2 in t:
            if letter2 in counter.keys():
                counter[letter2] -= 1
                if counter[letter2] == 0:
                    counter.pop(letter2)
            else:
                return False

        return True
#Solution 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)