
class Employee:
    current_code = 23123

    def __init__(self, name, employment):
        self.name = name
        self.employment = employment
        self.code = Employee.current_code
        Employee.current_code += 1

    def __str__(self):
        return "{} {} {}".format(self.name, self.employment, self.code)

class Company:
    def __init__(self):
        self.company = []

    def addEmployee(self, employee):
        self.company.append(employee)

    def showEmployees(self):
        for e in self.company:
            print(e)

    def updateEmployee(self, code, new_name, new_employment):
        for e in self.company:
            if e.code == code:
                e.name = new_name
                e.employment = new_employment
                break

    def deleteEmployee(self, code):
        for e in self.company:
            if e.code == code:
                self.company.remove(e)
                break

def main():
    company = Company()

    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Show Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            employment = input("Enter employment status: ")
            employee = Employee(name, employment)
            company.addEmployee(employee)
            print("Employee added successfully!")

        elif choice == '2':
            print("\nEmployees:")
            company.showEmployees()

        elif choice == '3':
            code = int(input("Enter employee code to update: "))
            new_name = input("Enter new name: ")
            new_employment = input("Enter new employment status: ")
            company.updateEmployee(code, new_name, new_employment)
            print("Employee updated successfully!")

        elif choice == '4':
            code = int(input("Enter employee code to delete: "))
            company.deleteEmployee(code)
            print("Employee deleted successfully!")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
