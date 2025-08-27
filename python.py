def modify_content(text):
    """
    Modify the content. You can change this function to do what you want.
    For now, we'll convert the text to uppercase.
    """
    return text.upper()

def read_and_write_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()

        modified_content = modify_content(content)

        new_filename = 'modified_' + filename
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Run the function
read_and_write_file()
