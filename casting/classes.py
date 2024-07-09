
class Animal:

    def __init__(self):
        self.__data = None

    @property
    def data(self):
        return self.__data

    def bark(self):
        pass

    def count(self):
        return 0


class Dog(Animal):

    def bark(self):
     print("Wow")

if __name__ == "__main__":
 the_dog = Dog()
 if the_dog.count():
     print("count")

