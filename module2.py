# When seperating the class and the main program, you need to import the class into the main program
# This is done by using the import statement, in this case 'import module2'
# In the main program, you can then use the class by using the syntax 'module2.class_name'

# I'd recommend making sure your class names are capitalized. 
# This makes it easier when importing inside the main program.

class FINALGRADE:
    def __init__(self, weekly_grades):
        self.weekly_grades = weekly_grades

    def calculate_final_grade(self):
        total_percentage = sum(self.weekly_grades)
        average_percentage = total_percentage / len(self.weekly_grades)
        return average_percentage
