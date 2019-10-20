# engrjepmanzanillo


class Solution:
    def __init__(self, string):
        self.string = []
        for i in range(len(string)):
            self.string.append(string[i])
        self.reversed_string = self.string[::-1]

    def isPalindrome(self):
        if self.string == self.reversed_string:
            if len(self.string) == 0:
                return False
            else:
                return True
        else:
            return False


s = ''
obj = Solution(s)
if obj.isPalindrome():
    print('The string, ' + s + ' is a palindrome.')
else:
    print('The string, ' + s + ' is not a palindrome.')
