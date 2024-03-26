from Person import Person
from Student import Student

if __name__ == "__main__":
    p = Person("Artur","Semikov",35)
    s = Student(first_name="Artur",last_name="Semikov",age=35,faculty="Big Data")
    print(p)
    print(s)