class Employee:

    def __init__(self):
        self._EmployeeName = ""
        self._EmployeeID = ""
        self._AmountPaidThisMonth = 0

    def SetEmployeeName(self, employeeName):
        self._EmployeeName = employeeName

    def SetEmployeeID(self, employeeId):
        self._EmployeeID = employeeId

    def SetAmountPaidThisMonth(self, amountPaidThisMonth):
        self._AmountPaidThisMonth = amountPaidThisMonth

class HourlyPaidEmployee(Employee):

    def __init__(self):
        super().__init__()
        self._HoursWorked = 0
        self._HourlyPayRate = 0

    def SetHoursWorked(self, hoursWorked):
        self._HoursWorked = hoursWorked

    def SetHourlyPayRate(self, hourlyPayRate):
        self._HourlyPayRate = hourlyPayRate

    def CalculatePay(self):
        return self._HoursWorked * self._HourlyPayRate

class SalariedEmployee(Employee):

    def __init__(self):
        super().__init__()
        self._AnnualSalary = 0

    def SetAnnualSalary(self, annualSalary):
        self._AnnualSalary = annualSalary

    def CalculatePay(self):
        return self._AnnualSalary / 12

hourlyPaidEmployee = HourlyPaidEmployee()
hourlyPaidEmployee.SetHoursWorked(5)
hourlyPaidEmployee.SetHourlyPayRate(10)

print(hourlyPaidEmployee.CalculatePay())

salariedEmployee = SalariedEmployee()
salariedEmployee.SetAnnualSalary(120000)

print(salariedEmployee.CalculatePay())
