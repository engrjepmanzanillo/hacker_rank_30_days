class Difference:

    def __init__(self, a):
        self.__elements = a
        # Add your code here
        self.maximumDifference = 0

    def computeDifference(self):
        diff = []
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                diff.append(abs(self.__elements[i] - self.__elements[j]))
        print(diff)
        self.maximumDifference = max(diff)
        return self.maximumDifference


# End of Difference class


#_ = input()
a = [8, 19, 3, 2, 7]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
