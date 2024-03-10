print("Input the number of cards:")
number_of_cards = int(input())
terms = {}
definitions = {}

for num in range(number_of_cards):
    print(f"The term for card #{num+1}:")
    terms[num] = input()
    print(f"The definition for card #{num+1}")
    definitions[num] = input()

for num in terms.keys():
    print(f"Print the definition of \"{terms[num]}\":")
    user_answer = input()
    if user_answer == definitions[num]:
        print(f"Correct!")
    else:
        print(f"Wrong. The right answer is \"{definitions[num]}\".")
