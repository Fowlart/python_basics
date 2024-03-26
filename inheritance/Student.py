from Person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, faculty):
        self.faculty = faculty
        Person.__init__(self, first_name, last_name, age)

    def __str__(self):
        return  f"[student]: {self.first_name}, {self.last_name}, {self.age}, {self.faculty}"

