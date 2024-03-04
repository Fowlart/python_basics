# Find out your total expense in first quarter (first three months) of the year.
# I assume expenses are sorted
expenses = [2200, 2350, 2600, 2130, 2190]
months = ['Jan', 'Feb', 'Mar', 'April', 'May']

if __name__ == "__main__":
    simple_sum = sum(expenses[0:3])
    print(f"The total expenses for the first 3 months are: {simple_sum}")
    print(simple_sum)
