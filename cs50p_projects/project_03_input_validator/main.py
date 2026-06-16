import re
def main():
    # Ask for name
    while True:
        name = input("What is your full name(first and last)?: ").strip().lower()

        if re.fullmatch("[a-zA-Z]+ [a-zA-Z]+", name):
            first, last = name.split(" ")
            break
        else:
            print("Please enter a first and last name separated by a space.")
        
    # Ask for age
    while True:
        try:
            age = int(input("What is your age(in years)?: "))
            if age in range(18,100):
                break
            else:
                print("Please enter a valid age.")
        except:
            print("Please enter a whole number.")

    # Ask for GPA
    while True:
        try:
            gpa = float(input("What is your unweighted GPA?: "))
            if 0.0 <= gpa <= 4.0:
                break
            else:
                print("Please enter a valid GPA.")
        except ValueError:
            print("Please enter a number as your GPA.")

    # Ask for desired salary
    while True:
        try:
            salary = int(input("What is your desired salary? Please enter a whole number.")
                         .replace(",", "")
                         .replace(".", "")
                         .replace(" ", ""))
            if salary in range(30000, 250000):
                break
            else:
                print("Please enter a velid salary (30k to 250k).")
        except ValueError:
            print("Please enter a valid number.")
    
    # Print out all applicant info
    print("Applicant info:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"GPA: {gpa}")
    print(f"Desired salary: {salary}")


main()