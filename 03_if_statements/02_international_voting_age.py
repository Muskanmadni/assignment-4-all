PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    user_age : int = int(input("Enter your age: "))

    if user_age >= PETURKSBOUIPO_AGE:
        print("You are eligible to vote in Peturksbouipo.")
    if user_age >= STANLAU_AGE:
        print("You are eligible to vote in Stanlau.")
    if user_age >= MAYENGUA_AGE:
        print("You are eligible to vote in Mayengua.")
    else:
        print("You are not eligible to vote")

if __name__ == "__main__":
    main()
