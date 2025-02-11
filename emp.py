import random

print("Welcome to Employee Wage Computation")


def check_attendance():
    attendance = random.randint(0, 1)
    if attendance == 1:
        print("The employee is present.")
        return 1
    else:
        print("The employee is absent.")
        return 0



def emp_daily_wage():
    wage_per_hour = 20
    emp_check = check_attendance()
    
    if emp_check == 1:
        daily_wage = wage_per_hour * 8
        print(f"The employee is present for the full day, so the daily wage is: {daily_wage}")
    else:
        daily_wage = 0
        print(f"The employee is absent for the day, so the daily wage is: {daily_wage}")

if __name__=="__main__":
    check_attendance()
    emp_daily_wage()