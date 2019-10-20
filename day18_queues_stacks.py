# https://www.hackerrank.com/challenges/30-queues-stacks/problem
# engrjepmanzanillo

import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)
        return self.stack

    def enqueueCharacter(self, ch):
        self.queue.insert(0, ch)
        return self.queue

    def popCharacter(self):
        self.stack.pop(0)
        return self.stack

    def dequeueCharacter(self):
        self.queue.remove(self.queue[0])
        return self.queue


# read the string s
s = 'racecar'
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
