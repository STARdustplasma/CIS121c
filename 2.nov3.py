
class Employee :
    def __init__(self, name, id) :
        self.name = name
        self.id = id


class hourlyEmployee(Employee) :
    def __init__(self, name, id, wage, weakly_hours) :
        super().__init__(name, id)
        self.wage = wage
        self.hours = weakly_hours
    
    def calculate_payroll(self) :
        self.payroll = self.wage * self.hours * 52
        return self.payroll

    def __str__(self) :
        print('=== Hourly Info ===')
        print(f'Employee Name: {self.name}')
        print(f'Employee ID: {self.id}')
        print(f'Employee Hourly wage: {self.wage}')
        print(f'Employee Hours per week: {self.hours}')
        print(f'Employee Yearly Salary: {self.calculate_payroll()}')
        return '======================='


class salaryEmployee(Employee) :
    def __init__(self, name, id, weekly_salary) :
        super().__init__(name, id)
        self.salary = weekly_salary

    def calculate_payroll(self) :
        self.payroll = self.salary * 52
        return self.payroll

    def __str__(self) :
        print('=== Salary Info ===')
        print(f'Employee Name: {self.name}')
        print(f'Employee ID: {self.id}')
        print(f'Employee weekly Salary: {self.salary}')
        print(f'Employee Yearly Salary: {self.calculate_payroll()}')
        return '======================='
        


class commissionEmployee(salaryEmployee) :
    def __init__ (self, name, id, weekly_salary, commission_fee, commissions) :
        super().__init__(name, id, weekly_salary)
        self.fee = commission_fee
        self.commissions = commissions

    def calculate_payroll(self) :
        self.payroll = super().calculate_payroll() + self.fee*self.commissions
        return self.payroll

    def __str__(self) :
        print('=== Commission Info ===')
        print(f'Employee Name: {self.name}')
        print(f'Employee ID: {self.id}')
        print(f'Employee weekly Salary: {self.salary}')
        print(f'Employee Comission Fee: {self.fee}')
        print(f'Employee Comission Count: {self.commissions}')
        print(f'Employee Yearly Salary: {self.calculate_payroll()}')
        return '======================='

        


class payrollInterface :
    def calculate_sal() :
        employee1 = salaryEmployee('sally',123475689, 1200)
        print(employee1)
        return ''

    def calculate_hour() :
        employee2 = hourlyEmployee('howard', 12358976, 12, 20)
        print(employee2)
        return ''

    def calculate_com() :
        employee3 = commissionEmployee('cammy', 123465789,1200,200,4)
        print(employee3)
        return ''
        

        

complete = payrollInterface
# complete.calculate_sal()
# complete.calculate_hour()
complete.calculate_com()