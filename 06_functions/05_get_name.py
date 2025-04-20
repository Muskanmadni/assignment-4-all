#Fill out the function get_name() which prompts the user for their name and returns it as a string.

def get_name():
    return input("Enter your name: ")

def main():
    name = get_name()
    print( name, "! 🤠")

if __name__ == '__main__':
    main()
