# Based on the provided Python code, the statement print("I can, but it hurts a lot!") is indeed unreachable due to
# the way the conditional elif statements are ordered.

# When Python evaluates these conditions:

# If price > 1000, it prints "That's too expensive!" and skips the rest of the conditions. If price > 500,
# it prints "I can afford that!" and again skips the rest of the conditions. The third condition checks if price >
# 900. However, this condition is never reached because any price greater than 900 would already have been caught by
# the first condition (price > 1000) or the second condition (price > 500). Therefore, if the price is more than 500
# but less than or equal to 1000, the program will already have printed "I can afford that!" and exited the
# conditional block before it checks if price > 900. So, without code refactoring, there's no possible way for the
# code to reach the statement print("I can, but it hurts a lot!") given the current conditions. For a price to
# trigger that print statement, the order of the conditions would need to be changed or the specific condition's
# logic adjusted so it doesn't overlap unreachably with the others.


price: int = int(input("enter price here >"))  # there should be some int value
if price > 1000:
    print("That's too expensive!")
elif price > 500:
    print("I can afford that!")
elif price > 900:  # this one is not reachable
    print("I can, but it hurts a lot!")
else:
    print("That's too cheap!")

# cool syntax
name = "Zenoviy"
if name in "Artur, Olena, Melania, Vlad":
    print("It is Semikov's family!")
if name in "Artur, Olena, Melania, Vlad, Zenoviy, Vita, Angela":
    print("It is Semikov's nearest people!")
if name in "Artur, Olena":
    print("It is Semikov's married couple!")
if name in "Artur":
    print("It is Developer!")

