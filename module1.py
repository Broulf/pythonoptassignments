# When seperating the class and the main program, you need to import the class into the main program
# This is done by using the import statement, in this case 'import module1'
# In the main program, you can then use the class by using the syntax 'module1.class_name'

# I'd recommend making sure your class names are capitalized. 
# This makes it easier when importing inside the main program.

class EMPLOYEE:
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        self.emp_id = emp_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"Employee ID: {self.emp_id}\nName: {self.name}\nHourly Rate: ${self.hourly_rate:.2f}\nHours Worked: {self.hours_worked}\nPay: ${self.calculate_pay():.2f}"
    