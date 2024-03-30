#Solution 1 (Runtime: O(N), Space: O(N)）
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
#Solution 2 (Runtime: O(N), Space: O(1)）
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
#Solution 3 (Same algorithm as Solution 1, uses Counter)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        return counter_s == counter_t
    
# These lines use the Counter class from the Python collections module to create dictionaries
# that count the occurrences of each character in the strings s and t, respectively.
# The Counter class is a specialized dictionary subclass designed for counting hashable objects.
# Each key in the dictionary represents a unique character in the string, and the corresponding value represents the frequency of that character in the string.