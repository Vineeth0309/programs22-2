class Employee:
    def getEmployee(self):
        self.__id = input("Enter Employee Id: ")
        self.__name = input("Enter Name: ")
        self.__salary = int(input("Enter Employees Basic Salary: "))
    def printEmployeeDetails(self):
        print(self.__id, self.__name, self.__salary)
    def getSalary(self):
        return (self.__salary)
class Perks(Employee):
    def calcPerks(self):
        self.getEmployee()
        sal = self.getSalary()
        self.__da = sal * 35 / 100
        self.__hra = sal * 17 / 100
        self.__pf = sal * 12 / 100
    def putPerks(self):
        self.printEmployeeDetails()
        print(self.__da, self.__hra, self.__pf)
    def totalPerks(self):
        t = self.__da + self.__hra - self.__pf
        return (t)
class NetSalary(Perks):
    def getTotal(self):
        self.calcPerks()
        self.__ns = self.getSalary() + self.totalPerks()
    def showTotal(self):
        self.putPerks()
        print("Total Salary:", self.__ns)
empSalary = NetSalary()
empSalary.getTotal()
empSalary.showTotal()
