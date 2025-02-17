import random


def check_attendance():
    """
    description: Function checks the attendance status of an employee.
    parameters: Function does not take any parameters.
    return: Function returns 1 if the employee is present and 0 if absent.
    """
    try:
        return random.randint(0, 1)
    except Exception as e:
        print(f"An error occurred while checking attendance: {e}")
        return 0  

def emp_monthly_wage():
    """
    description: Function calculates and prints the total monthly wage of an employee based on attendance.
    parameters: Function does not take any parameters.
    return: Function does not return anything but prints the total monthly wage.
    """
    try:
        wage_per_hour = 20
        working_days_in_month = 20
        total_wage = 0

        for _ in range(working_days_in_month):
            emp_check = check_attendance()
            match emp_check:
                case 1:
                    total_wage += wage_per_hour * 8
                case _:
                    total_wage += 0

        print(f"The total monthly wage for the employee is: {total_wage}")
    except Exception as e:
        print(f"An error occurred while calculating the monthly wage: {e}")

def main():
    emp_monthly_wage()

if __name__ == "__main__":
    main()
