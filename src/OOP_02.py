MONTHS_IN_YEAR = 12


class Salary:
    def __init__(self, month_pay):
        self.month_pay = month_pay

    def get_year_salary(self):
        return self.month_pay * MONTHS_IN_YEAR

class Employee:

    def __init__(self, month_pay, bonus):
        self.pay = month_pay
        self.bonus = bonus
        self.salary = Salary(month_pay)


    def annual_salary(self):
        return self.salary.get_year_salary() + self.bonus


employee_01 = Employee(month_pay=50000, bonus=10000)
annual_salary = employee_01.annual_salary()
print(annual_salary)

