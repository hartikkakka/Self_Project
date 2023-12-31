import salary_backend as sb
import salary_calculation as sc

User_choice = """
Type A to add employee,
Type V to View all employee,
Type S to search any employee,
Type D to delete any employee,
Type U to update any employee,
Type C to Calculate Salary of all employee
Type Q to Quit the program.
"""


def add_employee():
    name = input("Enter Employee name: ")
    ctc = input("Enter Employee CTC : ")
    Ac_number = input("Enter Bank A/c number of employee: ")
    IFSC = input("Enter Bank IFSC Number of employee: ")
    sb.insert(name, ctc, Ac_number, IFSC)


def view_all_books():
    for salary_man in sb.view():
        print(f"{salary_man[1]} has salary of {salary_man[2]} and bank details are {salary_man[3]} and {salary_man[4]}")


def search_employee():
    salary_man = input("Enter Employee name: ")
    for salary_man in sb.search(salary_man):
        print(f"{salary_man[1]} has salary of {salary_man[2]} and bank details are {salary_man[3]} and {salary_man[4]}")


def delete_employee():
    delete = input("Entre Employee name : ")
    sb.delete(delete)


def update_employee():
    name = input("Enter Employee name: ")
    ctc = input("Enter Employee CTC : ")
    Ac_number = input("Enter Bank A/c number of employee: ")
    IFSC = input("Enter Bank IFSC Number of employee: ")
    sb.update(name, ctc, Ac_number, IFSC)


def salary_cal():
    sc.salary_calculation()


def menu():
    sb.connect()
    user_input = input(User_choice).upper()
    while user_input != "Q":
        if user_input == "A":
            add_employee()
        elif user_input == "V":
            view_all_books()
        elif user_input == "S":
            search_employee()
        elif user_input == "D":
            delete_employee()
        elif user_input == "U":
            update_employee()
        elif user_input == "C":
            salary_cal()

        user_input = input(User_choice).upper()


menu()
