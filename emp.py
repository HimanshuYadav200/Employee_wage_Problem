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

def emp_daily_wage():
    """
    description: Function calculates and prints the daily wage of an employee based on their attendance.
    parameters: Function does not take any parameters.
    return: Function does not return anything but prints the daily wage.
    """
    try:
        wage_per_hour = 20
        emp_check = check_attendance()

        if emp_check == 1:
            daily_wage = wage_per_hour * 4  
            print(f"The employee is present, so the daily wage is: {daily_wage}")
        else:
            daily_wage = 0
            print(f"The employee is absent, so the daily wage is: {daily_wage}")
    except Exception as e:
        print(f"An error occurred while calculating the daily wage: {e}")

def main():
    emp_daily_wage()

if __name__ == "__main__":
    main()
