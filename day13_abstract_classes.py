# https://www.hackerrank.com/challenges/30-abstract-classes/problem
# engrjepmanzanillo


from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass

# Write MyBook class


class MyBook(Book):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print('Title: {}'.format(self.title))
        print('Author: {}'.format(self.author))
        print('Price: {}'.format(self.price))


#title = input()
title = 'The Alchemist'
#author = input()
author = 'Paulo Coelho'
#price = int(input())
price = 248
new_novel = MyBook(title, author, price)
new_novel.display()
