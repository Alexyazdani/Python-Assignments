def find_file():
    """
    Asks user for a file to check if it exists, returns filename if it does.
    If it does not, an error message is displayed and the user is prompted again for input.
    """
    while True:
        file_name = input("What is the name of the file you would like to process?  ")
        try:
            test_file = open(file_name, "r")
            return file_name
        except:
            print("That is not a valid filename, please try again.\n")



def main():
    """
    Alternate version that does not use .read()
    """
    line_count = 0
    word_count = 0
    char_count = 0
    data_filename = find_file()
    data_file = open(data_filename, "r")
    for line in data_file:
        line_count += 1
        word_count += len(line.split())
        for char in line:
            char_count += 1
    print(line_count)
    print(word_count)
    print(char_count)

if __name__ == "__main__":
    main()