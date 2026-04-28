class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set={}
        t_set={}

        for n in s:
            s_set[n] = s_set.get(n,0) + 1
        for m in t:
            t_set[m] = t_set.get(m,0) + 1

        if s_set == t_set:
            return True
        else:
            return False