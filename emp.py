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
        
        
        
def emp_part_time_wage():
    wage_per_hour = 20
    emp_check = check_attendance()
    
    if emp_check == 1:
        daily_wage = wage_per_hour * 4
        print(f"The employee is present for part time, so the daily wage is: {daily_wage}")
    else:
        daily_wage = 0
        print(f"The employee is absent for the day, so the daily wage is: {daily_wage}")        
        
        

def switch(emp_type):
    daily_wage=20
    full_time_hours=8
    part_time_hours=4
    
    if emp_type=="FULL_TIME":
        emp_wage=daily_wage*full_time_hours
        print(f"employee wage is {emp_wage}")
    elif emp_type=="PART_TIME":
        emp_wage=daily_wage*part_time_hours  
        print(f"employee wage is {emp_wage}")  
        
        
        
def emp_monthly_wage():
    wage_per_hour = 20
    working_days_in_month = 20
    total_wage = 0
    
    for i in range(working_days_in_month):
        emp_check = check_attendance()
        if emp_check == 1:
            total_wage += wage_per_hour * 8
        else:
            total_wage += 0
    return total_wage     



def wages_total_working_hours():
    
    wage_per_hour = 20
    max_work_days = 20
    max_work_hours = 100

    total_wage = 0
    total_hours = 0
    total_days = 0

    while total_hours < max_work_hours and total_days < max_work_days:
        total_days += 1
        emp_check = check_attendance()

        if emp_check == 1:
           
            work_hours = random.choice([8, 4])
            print(f"Day {total_days}: Employee PRESENT, worked {work_hours} hours.")
        else:
            work_hours = 0
            print(f"Day {total_days}: Employee ABSENT, worked 0 hours.")

        total_hours += work_hours
        total_wage += work_hours * wage_per_hour

    print(f"\nTotal Wage for {total_days} days and {total_hours} hours: {total_wage}")



           
                

if __name__=="__main__":
    check_attendance()
    emp_daily_wage()
    emp_part_time_wage()
    
    employee_type=input("enter empoyee type(FULL_TIME OR PART_TIME): ")
    switch(employee_type)       
    
    final_wage=emp_monthly_wage()
    print(f"The total monthly wage for the employee is: {final_wage}")
    
    wages_total_working_hours()