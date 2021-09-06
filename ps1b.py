#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 05:50:32 2021

@author: vanessamsantana
"""

#Factoring in a raise every 6 months
#Have user input a semi-annual salary raise (semi_annual_raise) a decimal percentage
# After the 6th month, increase salary by that percentage. In crease by same % after 12th month, after 18th month, etc.

r = 0.04 #annual return at end of each month
portion_down_payment = 0.25
monthly_invest_return = 0
current_savings = 0



annual_salary = input("Enter your annual salary: ")
annual_salary = float(annual_salary)
#print(annual_salary)

portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
portion_saved = float(portion_saved)

total_cost = input("Enter the cost of your dream home: ")
total_cost = float(total_cost)

semi_annual_raise = input("Enter the semi-annual raise, as a decimal: ")
semi_annual_raise = float(semi_annual_raise)

downpayment_months = 0
downpayment_amount = total_cost*portion_down_payment

monthly_salary = annual_salary/12

while  (current_savings <= downpayment_amount):
    current_savings = current_savings + (monthly_salary * portion_saved)
    
    current_savings = current_savings + monthly_invest_return
    monthly_invest_return = current_savings*(r/12)
    
    downpayment_months = downpayment_months + 1
    
    if (downpayment_months%6 == 0):
        annual_salary = annual_salary + (annual_salary*semi_annual_raise)
        monthly_salary = annual_salary/12
        
downpayment_amount = str (downpayment_amount)
downpayment_months = str(downpayment_months)
current_savings  = str(current_savings)

print()
print("Number of months: " + downpayment_months)
print("Down payment amount: $" + downpayment_amount)
print("Current savings: " + current_savings)



# Enter your annual salary: 120000

# Enter the percent of your salary to save, as a decimal: 0.05

# Enter the cost of your dream home: 500000

# Enter the semi-annual raise, as a decimal: 0.03

# Number of months: 142
# Down payment amount: $125000.0
# Current savings: 125788.54396654214



# Enter your annual salary: 80000

# Enter the percent of your salary to save, as a decimal: 0.1

# Enter the cost of your dream home: 800000

# Enter the semi-annual raise, as a decimal: 0.03

# Number of months: 159
# Down payment amount: $200000.0
# Current savings: 201556.58809733373



# Enter your annual salary: 75000

# Enter the percent of your salary to save, as a decimal: 0.05

# Enter the cost of your dream home: 1500000

# Enter the semi-annual raise, as a decimal: 0.05

# Number of months: 261
# Down payment amount: $375000.0
# Current savings: 378291.88049863355