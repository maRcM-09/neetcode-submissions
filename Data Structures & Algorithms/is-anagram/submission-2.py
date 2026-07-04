class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # initialize a frequency table for both
        s_table = {}
        t_table = {}
        for char_t in t:
            t_table[char_t] = 1 + t_table.get(char_t , 0)
        for char_s in s:
            s_table[char_s] = 1 + s_table.get(char_s , 0)
        for character in s_table:
            if character not in t_table or t_table[character] != s_table[character]:
                return False
        return True