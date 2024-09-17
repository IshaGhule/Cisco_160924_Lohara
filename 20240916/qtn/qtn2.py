def process_list():
    # Ask the user to input a list of integers
    input_str = input("Enter a list of integers separated by spaces: ")
    
    # Convert the input string to a list of integers
    num_list = list(map(int, input_str.split()))

    # Convert the list to a tuple and display it
    num_tuple = tuple(num_list)
    print(f"Tuple: {num_tuple}")

    # Convert the list to a set to remove duplicates and display it
    num_set = set(num_list)
    print(f"Set (duplicates removed): {num_set}")

    # Convert the set to a frozenset and display it
    num_frozenset = frozenset(num_set)
    print(f"Frozenset: {num_frozenset}")

    # Create a dictionary with integers as keys and their squares as values
    num_dict = {x: x**2 for x in num_list}
    print(f"Dictionary: {num_dict}")

    # Write the dictionary contents to a file
    with open("dictionary.txt", "w") as file:
        file.write(str(num_dict))

    # Read the contents of the file and display it
    with open("dictionary.txt", "r") as file:
        file_contents = file.read()
    
    print("Contents of 'dictionary.txt':")
    print(file_contents)

# Run the function
process_list()

