# -*- coding: utf-8 -*-
"""
MIT600_ps1b.py

@author: MacGuffin_

Created on Fri Jul  2 00:11:48 2021
----------------------------------------
In Part A, we unrealistically assumed that your salary didn’t change.  But you are an MIT graduate, and
clearly you are going to be worth more to your company over time! So we are going to build on your
solution to Part A by factoring in a raise every six months.
In ​ps1b.py​​, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify
your program to include the following
1. Have the user input a semi-annual salary raise ​semi_annual_raise​​ (as a decimal percentage)
2. After the 6​ th​  month, increase your salary by that percentage.  Do the same after the 12th
​month, the 18​th month, and so on.
Write a program to calculate how many months it will take you save up enough money for a down
payment.  LIke before, assume that your investments earn a return of ​r​​ = 0.04 (or 4%) and the
required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
1. The starting annual salary (annual_salary)
2. The percentage of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
4. The semi­annual salary raise (semi_annual_raise)
"""
# User Input
annual_salary = float(input("Enter starting annual salary: ",))
portion_saved = float(input("Enter portion of salary to be saved, as a decimal: ",))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal"))

# Maths
portion_down_payment = total_cost * 0.25
current_savings = 0                         # Starting savings = 0
month = 0
r = 0.04                                    # investment rate [yearly]

while current_savings < portion_down_payment:
    month += 1
    current_savings += current_savings*r/12 + portion_saved*annual_salary/12
    if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

# Output
print("Number of months: ",month)
