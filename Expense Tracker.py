
expenseList=[]

print("==============================")
print("WELCOME TO EXPENSE TRACKER")
print("==============================")

while True:
    print("----------MENU----------")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total Expense")
    print("4. Exit")

    choice=int(input("Enter Your Choice:"))

    if(choice==1):
        print("-------ADD NEW EXPENSE-------")
        date=input("Enter The Date:")
        category=input("Enter Category (food,travel,shopping,entertainment,education,etc):")
        description=input("Enter Description:")
        amount=float(input("Enter Amount Spend:"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }
        expenseList.append(expense)
        print("Expense Added Successfully!!")

    elif(choice==2):
        print("-------EXPENSE RECORD-------")
        if(len(expenseList)==0):
            print("No Expense found")
        else:
            count=1
            
            for i in expenseList:
                print(count,"|", i["date"],"|", i["category"],"|", i["description"],"|", i["amount"])
               # print(f"sr.no.{count}={i['date']},{i['category']},{i['description']},{i['amount']}")
                count+=1

    elif(choice==3):
        total=0
        for i in expenseList:
            total+=i["amount"]
        print("Total Spending:",total)
        
    elif(choice==4):
        print("Thank You For Using My Project")
        break
    else:
        print("Invalid Choice")
    