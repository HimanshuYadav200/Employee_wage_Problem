import random

def check_attendance():
    attendance = random.randint(0, 1)
    if attendance == 1:
        print("The employee is present.")
    else:
        print("The employee is absent.")

print("Welcome to Employee Wage Computation")

if __name__=="__main__":
    check_attendance()