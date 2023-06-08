class Employee:
    def __init__(self, name, employment, code):
        self.name = name
        self.employment = employment
        self.code = code
        print("An Employee Has Been Created Successfully")

    def __del__(self):
        print("An Employee Has Been Deleted Successfuly")

    def __str__(self):
        return "{} {} {}".format(self.name, self.employment, self.code)

class Company:
    company = []

    def __init__(self, company=[]):
        self.company = company

    def addEmployee(self, employee):
        self.company.append(employee)

    def showEmployee(self):
        for e in self.company:
            print(e)

