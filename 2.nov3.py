
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
        return f'{self.name} makes {self.calculate_payroll()}'


class salaryEmployee(Employee) :
    def __init__(self, name, id, weekly_salary) :
        super().__init__(name, id)
        self.salary = weekly_salary

    def calculate_payroll(self) :
        self.payroll = self.salary * 52
        return self.payroll

    def __str__(self) :
        return f'{self.name} makes {self.calculate_payroll()}'
        


class commissionEmployee(salaryEmployee) :
    def __init__ (self, name, id, weekly_salary, commission_fee, commissions) :
        super().__init__(name, id, weekly_salary)
        self.fee = commission_fee
        self.commissions = commissions

    def calculate_payroll(self) :
        self.payroll = super().calculate_payroll() + self.fee*self.commissions
        return self.payroll

    def __str__(self) :
        return f'{self.name} makes {self.calculate_payroll()}'
        



class payrollInterface :
    def calculate() :
        employee1 = salaryEmployee('sally',123475689, 1200)
        employee2 = hourlyEmployee('howard', 12358976, 12, 20)
        employee3 = commissionEmployee('cammy', 123465789,1200,200,4)

        print('======')
        print(employee1)
        print(employee2)
        print(employee3)
        print('======')
        

complete = payrollInterface
complete.calculate()
