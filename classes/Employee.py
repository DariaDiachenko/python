from classes.Human import Human

class Employee(Human):
    def __init__(self, name, sex, position, salary):
        super().__init__(name, sex, position, salary)



    def get_up(self):
        print(self.name, "Get up")

    def sit_down(self):
        print(self.name, "Sit down")

    def lie_down(self):
        print(self.name, "Lie down")

    def go_to_work(self):
        print(self.name, "Go to work")

    def log_time(self):
        print(self.name, "Log time")
