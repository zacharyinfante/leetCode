import re

# class Solution(object):
#     def isPalindrome(self, s):
#         new_s = re.sub(r"[^a-zA-Z0-9\\s+]", "", s).lower()
#         return new_s == new_s[::-1]

# class Solution(object):
#     def isPalindrome(self, s):
#         s_list = []

#         for char in s:
#             if char.isalnum():
#                 char = char.lower()
#                 s_list.append(char)

#         return s_list == s_list[::-1]

#two pointer solution

# NOTE: isalnum()
                
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        left, right = (0, len(s)-1)

        while (right > left):
            while right > left and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            
            left += 1
            right -=1
        return True


            