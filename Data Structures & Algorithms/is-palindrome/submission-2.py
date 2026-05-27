class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        filtered_chars = [x for x in s.lower() if x in allowed_chars]
        i, j = 0, len(filtered_chars)-1
        while i<=j:
            if filtered_chars[i]!=filtered_chars[j]:
                return False
            i+=1
            j-=1
        return True