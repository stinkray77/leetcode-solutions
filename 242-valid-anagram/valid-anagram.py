class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        li1 = [0] * 26
        li2 = [0] * 26

        for i, char in enumerate(s):
            li1[ord(char) - 97] += 1
        for i, char in enumerate(t):
            li2[ord(char) - 97] += 1

        return li1 == li2