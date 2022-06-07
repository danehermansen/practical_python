#  get the loan details 
from unittest.mock import patch


money_owed = float(input("how much money do you owe?\n"))
apr = float(input("what is the annual percentage rate?\n"))
payment = float(input("what will your monthly payment be?\n"))
months = int(input("how many months do you want to see results?\n"))

monthly_rate = apr/100/12

for i in range(months):


    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("the last payment is", money_owed)
        print("you paid off the last loan in", i+1, "months") 

    money_owed = money_owed - payment

    print("paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("now i owe", money_owed)
