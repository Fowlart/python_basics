from collections import namedtuple

if __name__ == "__main__":

    # The main advantage is that the Object is immutable, right?
    Point = namedtuple('Point', ['x', 'y'])
    point1 = Point(x=10,y=20)
    print(point1)
    print(type(point1)) # <class '__main__.Point'>
    print('-' * 50)


    Person = namedtuple('Person',['name','age','income','weight'])
    person1 = Person(name='Artur',age=37,income=5,weight=82)
    print(person1)
    print(type(person1))
    print(person1.age)
    print(person1.income)
    print(person1.weight)
    #person1.income = 6000 # can't set attribute
    print(person1)
    print('-' * 50)

