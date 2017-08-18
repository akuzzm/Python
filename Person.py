class Person:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary    

    def __str__(self):
        return "Hello, my name is {}. I am {} years old. My salary is {}." \
               .format(self.name, self.age, self.salary)
