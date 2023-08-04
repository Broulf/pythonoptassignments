# Create an employee class (id, name, hourly rate, hours worked, pay (hourly rate * hours worked)
# Create a simple program to demonstrate the usage of the above class, the user will input (id, name, hourly rate, hours worked), 
# and the class will calculate the pay per employee. Be creative in how to display the data.

# ================================================================================================================================

# EXAMPLE OUTPUT:

#Welcome to the Employee Pay Calculator!
#Enter the number of employees: 3
#
#Employee 1
#Enter Employee ID: 001
#Enter Employee Name: Anthony
#Enter Hourly Rate: $50
#Enter Hours Worked: 40
#
#Employee 2
#Enter Employee ID: 002
#Enter Employee Name: Garrett
#Enter Hourly Rate: $20
#Enter Hours Worked: 40
#
#Employee 3
#Enter Employee ID: 003   
#Enter Employee Name: Andrew
#Enter Hourly Rate: $25
#Enter Hours Worked: 40
#
#--- Employee Payroll ---
#Employee ID: 1
#Name: Anthony
#Hourly Rate: $50.00
#Hours Worked: 40.0
#Pay: $2000.00
#--------------------
#Employee ID: 2
#Name: Garrett
#Hourly Rate: $20.00
#Hours Worked: 40.0
#Pay: $800.00
#--------------------
#Employee ID: 3
#Name: Andrew
#Hourly Rate: $25.00
#Hours Worked: 40.0
#Pay: $1000.00
#--------------------

# ================================================================================================================================

class Employee:
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        self.emp_id = emp_id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

    def __str__(self):
        return f"Employee ID: {self.emp_id}\nName: {self.name}\nHourly Rate: ${self.hourly_rate:.2f}\nHours Worked: {self.hours_worked}\nPay: ${self.calculate_pay():.2f}"


def main():
    print("Welcome to the Employee Pay Calculator!")
    num_employees = int(input("Enter the number of employees: "))
    employees = []

    for i in range(num_employees):
        print(f"\nEmployee {i + 1}")
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        hourly_rate = float(input("Enter Hourly Rate: $"))
        hours_worked = float(input("Enter Hours Worked: "))

        employee = Employee(emp_id, name, hourly_rate, hours_worked)
        employees.append(employee)

    print("\n--- Employee Payroll ---")
    for emp in employees:
        print(emp)
        print("-" * 20)


if __name__ == "__main__":
    main()
