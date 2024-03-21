theString: str = 'The quick brown fox jumps over the lazy frogs'
# reassigning is very much possible
print(type(theString))
theString = 1
print(theString)
print(type(theString))  # <class 'int'>

theString = 'The quick brown fox jumps over the lazy frogs'
print(theString.upper())
print(theString.lower().capitalize())
print(theString.center(50))
print("1".center(3, "_"))
print(theString.count("the"))

print("endswith, startswith:".rjust(50))
print(theString.endswith("lazy frogs"))
print(theString.startswith("The"))

print("isalpha:".rjust(50))
print(theString.isalpha())
print("onlyLetters".isalpha())
print("only Letters".isalpha())

print("isdigit:")
print("123987".isdigit())
decimal = "123.987"
print(decimal.isdigit())
print(decimal.isalnum())
print(decimal.isdecimal())
theNewString = theString.replace("lazy", "sleepy")
print(theNewString.lower().islower())

print("Sometimes, it pays to stay in bed on Monday ".rjust(100))
print("rather than spending the rest of the week debugging Monday's code.".rjust(100))
