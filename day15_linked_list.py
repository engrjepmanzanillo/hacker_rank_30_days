# https://www.hackerrank.com/challenges/30-linked-list/problem
# engrjepmanzanillo


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method


mylist = Solution()
#T = int(input())
T = 4
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
