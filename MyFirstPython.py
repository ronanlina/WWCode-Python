""" The Challenge
Author:
Description: Aling Nena’s Sari-sari store wants a robot that will ask the
customer their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

# Build your code below

totalBill = input('How much is your total bill? ')
payment = input('How much is your payment? ')

change = totalBill - payment

print('Hi! Your change is {}'.format(change))