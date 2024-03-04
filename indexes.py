class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

string_is_also_a_seq: str = "hello world"
# accessing elements in the String
print(string_is_also_a_seq[0])

# changing element of the list
my_edc = ["phone","knife","wallet","money","key"]
my_edc[1] = "sword"
print(my_edc)

# but strings are immutable
try:
    string_is_also_a_seq[2] = "E"
    print(string_is_also_a_seq)

except Exception as exception:
    print(f"{bcolors.WARNING}An error occurred: {exception}"+bcolors.ENDC )

# the easier way to access the elements at the end of a list or a string is to use negative indexes:
my_edc.append("gun")
print(my_edc)
print(my_edc[-1])

# len
print(len(my_edc))

name = input("Enter a string here, to analyze: ")
print(f"First letter is  {name[0]}!")
