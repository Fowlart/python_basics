# task 1 - In Feb, how many dollars you spent extra compare to January?
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
expenses = [2200, 2350, 2600, 2130, 2190]
months = ['Jan', 'Feb', 'Mar', 'April', 'May']

if __name__ == "__main__":
    expenses_in_feb = None
    expenses_in_jan = None

    for month, expense in zip(months, expenses):

        if month == 'Feb':
            expenses_in_feb = expense
        if month == 'Jan':
            expenses_in_jan = expense

    if expenses_in_feb and expenses_in_jan:
        print(expenses_in_feb - expenses_in_jan)
    else:
        print("Data for Jan or Feb expenses not found")
