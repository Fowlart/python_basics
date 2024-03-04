with open("input_text.txt", "r") as file:
    line = "_"
    while line != "":
        line = file.readline()
        print(line)
    # end of with block will close the file by itself

print(f"is file closed: {file.closed}")
file.close()