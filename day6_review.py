# https://www.hackerrank.com/challenges/30-review-loop/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
class Words:
    def __init__(self, string):
        self.string = string

    def even_char(self):
        new_list = []
        for i in range(len(self.string)):
            if i % 2 == 0:
                new_list.append(self.string[i])
        return ''.join(new_list)

    def odd_char(self):
        new_list = []
        for i in range(len(self.string)):
            if i % 2 != 0:
                new_list.append(self.string[i])
        return ''.join(new_list)


w = Words('Hacker')
print(w.even_char() + ' ' + w.odd_char())

w = Words('Rank')
print(w.even_char() + ' ' + w.odd_char())
