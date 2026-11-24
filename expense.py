import json
import os
import datetime
filename="expenses.json"
if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename,"r") as file:
        expenses=json.load(file)
else:
    expenses=[]
def add():
    name=input("Enter the expense name: ")
    amt=int(input("Enter the expense amount: "))
    cat=input("Enter the category: ")
    date=str(datetime.date.today())
    new_expense={"Name":name,"Amount":amt,"Category":cat,"Date":date}
    expenses.append(new_expense)
    with open(filename,"w") as file:
        json.dump(expenses,file,indent=4)
    print("Expenses added successfully")
def view():
    if len(expenses)==0:
        print("No expenses recorded.")
    else:
        print("----ALL EXPENSES-----")
        for i in expenses:
            print("Name",i["Name"])
            print("Amount",i["Amount"])
            print("Catrgory",i["Category"])
            print("Date",i["Date"])
        print("End....")
def total():
    tot=sum(i["Amount"] for i in expenses)
    print("Total expenses:  Rs.",tot)
while True:
    print("\t-------EXPENSE TRACKER----------\n")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Total")
    print("4.Exit")
    n=int(input("Enter your choice: "))
    if n==1:
        add()
    elif n==2:
        view()
    elif n==3:
        total()
    elif n==4:
        print("Exiting...")
    else:
         print("Invalid choice!")
         break
        
   
