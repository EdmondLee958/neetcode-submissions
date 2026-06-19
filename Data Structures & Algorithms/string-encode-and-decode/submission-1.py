class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s + str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index('#', i)   # find the '#'
            length = int(s[i:j])  # read the number before '#'
            word = s[j+1 : j+1+length]  # slice exactly 'length' chars after '#'
            res.append(word)
            i = j + 1 + length    # move i to the start of the next word
        return res