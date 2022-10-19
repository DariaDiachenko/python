# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import names
import random
import task2
from classes.Employee import Employee

task2.func1()
task2.func2()


emp = Employee(names.get_full_name(), "male", "QA", random.randrange(1000, 2000))
emp.getName()
emp.getSex()
emp.getPosition()
emp.getSalary()