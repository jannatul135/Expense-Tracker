import csv
import os

#This is a simple expense tracker program that allows users to add expenses, view expenses, and calculate the total amount spent
def main():
    if os.path.exists("expenses.csv"):
        AllExpenses = LoadFromCSV()
    else:
        AllExpenses = []

    while True:
        menu = input(" 1. Add Expenses\n 2. View Expenses\n 3. Total Expenses\n 4. Exit\n 5. Save Expenses to CSV\n")

        if menu == "1":
            AddExpense(AllExpenses)
        elif menu == "2":
            ViewExpense(AllExpenses)
        elif menu == "3":
            print(TotalExpenses(AllExpenses))
        elif menu == "4":
            break
        elif menu == "5":
            SaveToCSV(AllExpenses)

        

#Takes in a list of expenses and allows the user to add more expenses, 
#ask for expenses name and amount, then return the updated list of expenses
def AddExpense(AllExpenses):
    while True:
        ExpenseName = input("What did you spend your money on? ")

        if ExpenseName == "done": 
            break

        ExpenseAmount = float(input("How much did you spend? "))

        expense = {"name" : ExpenseName, "amount": ExpenseAmount}

        AllExpenses.append(expense)

    return AllExpenses

#Takes in a list of expenses and return the total amount spent
def TotalExpenses(AllExpenses):
    TotalAmount = 0
    for expense in AllExpenses:
        TotalAmount = TotalAmount + expense["amount"]
    return ("Total amount spent: $" + str(TotalAmount))


#Takes in a list of expenses and print out each expense in the format "name: $amount"
def ViewExpense(AllExpenses):
    for expense in AllExpenses:
        print(expense["name"] +": $"+ str(expense["amount"]))

#Saves the list of expenses to a CSV file called "expenses.csv" 
def SaveToCSV(AllExpenses):
    with open("expenses.csv", mode="w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "amount"])
        writer.writeheader()
        for expense in AllExpenses:
            writer.writerow(expense)

def LoadFromCSV():
    with open("expenses.csv", mode="r", newline='') as file:
        reader = csv.DictReader(file)
        AllExpenses = list(reader)
    return AllExpenses

print("Welcome to the Expense Tracker!")
main()
