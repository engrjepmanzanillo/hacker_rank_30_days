# https://www.hackerrank.com/challenges/30-inheritance/problem
# engrjepmanzanillo


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average = int(sum(self.scores) / len(self.scores))
        if average <= 100 and average >= 90:
            return 'O'
        elif average < 90 and average >= 80:
            return 'E'
        elif average < 80 and average >= 70:
            return 'A'
        elif average < 70 and average >= 55:
            return 'P'
        elif average < 55 and average >= 40:
            return 'D'
        else:
            return 'T'


    # line = input().split()
firstName = 'Heraldo'
lastName = 'Memelli'
idNum = 8135627
numScores = int(2)  # not needed for Python
scores = [100, 80]
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
