def super_function() -> str:
    return "super_function"

super_variable = super_function()

print(f"the name of the module is {__name__}")
print("If this going to execute?")

if __name__ == "__main__":
    print("This peace of code not going to be executed!")