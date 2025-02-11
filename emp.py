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
                

if __name__=="__main__":
    check_attendance()
    emp_daily_wage()
    emp_part_time_wage()
    
    employee_type=input("enter empoyee type(FULL_TIME OR PART_TIME): ")
    switch(employee_type)       
    
    final_wage=emp_monthly_wage()
    print(f"The total monthly wage for the employee is: {final_wage}")