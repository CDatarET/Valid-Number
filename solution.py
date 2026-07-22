class Solution:
    def isNumber(self, s):
        if 'i' in s or 'I' in s or 'n' in s:
            return False
        try:
            s = float(s)
            return True
        except:
            return False
