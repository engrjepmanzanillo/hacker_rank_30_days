class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self.initialAge = 0

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialAge < 13:
            return print('You are young.')
        elif self.initialAge >= 13 and self.initialAge < 18:
            return print('You are a teenager.')
        else:
            return print('You are old.')

    def yearPasses(self):
        self.initialAge = self.initialAge + 1
        return self.initialAge


t = int(4)
for i in range(0, t):
    age = int(18)
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
