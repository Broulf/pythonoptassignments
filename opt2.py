# 1)	Create a final grade class that will accept the weekly percentage grade to calculate the final grade.
# 2)	Create a simple program to demonstrate the usage of the above class, the user will input the weekly percentage grades 
#       and the program will calculate the final grade (use the "average equation" to calculate the final)
# 3)	Create a Python Dictionary with corresponding letter grade and use them as the output.

# ================================================================================================================================

# Final Grade Calculator!
#Enter the number of weekly grades: 9
#Enter Week 1 Percentage Grade: 76
#Enter Week 2 Percentage Grade: 87
#Enter Week 3 Percentage Grade: 93
#Enter Week 4 Percentage Grade: 95
#Enter Week 5 Percentage Grade: 95
#Enter Week 6 Percentage Grade: 64
#Enter Week 7 Percentage Grade: 87
#Enter Week 8 Percentage Grade: 97
#Enter Week 9 Percentage Grade: 99
#
#Final Percentage Grade: 88.11%
#Letter Grade: B

# ================================================================================================================================

class FinalGrade:
    def __init__(self, weekly_grades):
        self.weekly_grades = weekly_grades

    def calculate_final_grade(self):
        total_percentage = sum(self.weekly_grades)
        average_percentage = total_percentage / len(self.weekly_grades)
        return average_percentage

def get_letter_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def main():
    print("Final Grade Calculator!")
    num_weeks = int(input("Enter the number of weekly grades: "))
    weekly_grades = []

    for i in range(num_weeks):
        week_grade = float(input(f"Enter Week {i + 1} Percentage Grade: "))
        weekly_grades.append(week_grade)

    final_grade_calculator = FinalGrade(weekly_grades)
    final_percentage = final_grade_calculator.calculate_final_grade()

    letter_grade = get_letter_grade(final_percentage)

    print(f"\nFinal Percentage Grade: {final_percentage:.2f}%")
    print(f"Letter Grade: {letter_grade}")

main()
