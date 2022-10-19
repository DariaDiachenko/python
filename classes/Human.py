class Human():
    def __init__(self, name, sex, position, salary):
        self.name = name
        self.sex = sex
        self.position = position
        self.salary = salary

    def getName(self):
        print(self.name)

    def getSex(self):
        print(self.sex)

    def getPosition(self):
        print(self.position)

    def getSalary(self):
        print(self.salary)