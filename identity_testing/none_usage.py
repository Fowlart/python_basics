def say_hello(name=None):
    if name is None:
        print('Hello!')
    else:
        print(f'Hello, {name}!')


say_hello("Olena")
say_hello()
