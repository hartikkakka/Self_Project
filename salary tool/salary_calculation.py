import salary_details_backhand
from calendar import monthrange

year = int(input("Enter year : "))
month = int(input("Enter Month : "))

no_of_days_in_month = monthrange(year=2023, month=2)[1]

no_of_days_absent = {}

for absent in salary_details_backhand.view():
    no_of_days_absent[absent[1]] = int(input(f'enter 1 for full day , 0.5 for half days and add {absent[1]} LWOP:'))


def salary_calculation():
    for sal_cal in salary_details_backhand.view():
        med = 1250/no_of_days_in_month * (no_of_days_in_month - no_of_days_absent[sal_cal[1]])
        conv = 1600/no_of_days_in_month * (no_of_days_in_month - no_of_days_absent[sal_cal[1]])
        basic_and_hra = (sal_cal[2] - med - conv)
        basic1 = (basic_and_hra * 50/100)/no_of_days_in_month * (no_of_days_in_month - no_of_days_absent[sal_cal[1]])
        total_payable = basic1 + basic1 + med + conv
        print(f"{sal_cal[1]} payable salary is {int(total_payable)} after taking lwop {no_of_days_absent[sal_cal[1]]}")


salary_calculation()