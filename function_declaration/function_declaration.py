def options(**opts):
    for k in opts:
        print(f" {k} |  {opts[k]}")


def some_function():
    print("This is an example function!")


def some_function_with_return() -> str:
    return "This is another example function!"


def some_function_with_params(first: str, second: int, third: float) -> str:
    return f"First: {first}, Second: {second}, Third: {third}"


def an_empty_function():
    pass

# v = some_function()
# v2: str = some_function_with_return()
# print(type(v))
# print(v)
# print(v2)
# print(some_function_with_params(first="some string", second=3, third=55.5))
# print(an_empty_function())
# print(an_empty_function())


dictionary = {"one": 1, "two": 2, "three": 3}

options(opts=dictionary)
