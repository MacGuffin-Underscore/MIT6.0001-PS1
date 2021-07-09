# -*- coding: utf-8 -*-
"""
MIT600_ps1c.py

@author: MacGuffin_

Created on Fri Jul  2 00:16:24 2021
----------------------------------------
In Part B, you had a chance to explore how both the percentage of your salary that you save each month
and your annual raise affect how long it takes you to save for a down payment.  This is nice, but
suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.
How much should you save each month to achieve this?  In this problem, you are going to write a
program to answer that question.  To simplify things, assume:
1. Your semi­annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%) 
3. The down payment is 0.25 (25%) of the cost of the house
4. The cost of the house that you are saving for is $1M.
You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in
36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of
the required down payment.
"""
from datetime import datetime as dt

# User Input
annual_salary = float(input("Enter starting annual salary: ",))
as_reset = annual_salary
time_start = dt.now()

# Initial Values
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
portion_down_payment = total_cost * 0.25
months = 36             # 3 year time-span
minmax = [0, 10000]     # 0% to 100% of portion saved
portion_saved = 5000    # Start at 50%
current_savings = 0
tol = 100
steps = 0
not_Possible = False

# Maths
while abs(current_savings - portion_down_payment) > tol:
    # reset holding values
    current_savings = 0
    annual_salary = as_reset
    
    # calculate the savings after 36 months
    for m in range(1,months+1):
        current_savings += current_savings*r/12 + (portion_saved*.0001)*annual_salary/12
        if m % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            
    # bisection search
    if current_savings > portion_down_payment:
        minmax[1] = portion_saved
    else:
        minmax[0] = portion_saved
    portion_saved = sum(minmax) / 2
    
    # count steps in the event of a impossible case
    steps += 1
    if steps > 100:
        not_Possible = True
        break

# Output
if not_Possible == False:
    print('Best savings rate:', round(portion_saved*.01,2),'%')
    print('Steps in bisection search:', steps)
else:
    print('Impossible to afford the down payment in 3 years')

print("Time to run:",dt.now()-time_start)
      
        

