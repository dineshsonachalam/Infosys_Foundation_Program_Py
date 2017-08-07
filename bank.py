import cx_Oracle
con = cx_Oracle.connect("system/dinesh@localhost/xe")
cur = con.cursor()

class Bank:

    def statistics(self):

        cur.execute(
            """
            SELECT COUNT(*) FROM Bank
            """
        )
        data = str(cur.fetchall()) #Now forms list object


        no = ""
        for i in data:
            if(i!="[" and i!="," and i!="]" and i!="(" and i!=")"):
                no+=i

        print("No of Records Present:",no)

        cur.execute("SELECT *from Bank")
        print("S.No     Full Name   Balance")
        for row in cur:
            print(row[0]," ",row[2]," ",row[3],"-------->",row[5],"[Balance]")




    def withdrawal(self,money,AccountNo,Password):

        cur.execute("""
        SELECT *from Bank WHERE AccountNo=:1 AND Password=:2""",(AccountNo,Password)

        )
        oldmoney = 0
        for row in cur:
          oldmoney = int((row[5])) #Balance
        print("\n")
        print("Oldmoney:",oldmoney)

        newmoney = oldmoney - int(money)
        if(newmoney>0):

                # Update operation of the money
                # newmoney = oldmoney + money_deposited
                print("New Money:",newmoney)
                cur.execute(""" UPDATE Bank SET Balance=:1
                WHERE AccountNo=:2 AND Password=:3""",(newmoney,AccountNo,Password))



        else:
                print("You dont have sufficient amount to Withdraw!")

    def deposit(self,money,AccountNo,Password):

        cur.execute("""
        SELECT *from Bank WHERE AccountNo=:1 AND Password=:2""",(AccountNo,Password)

        )
        oldmoney = 0
        for row in cur:
          oldmoney = int((row[5])) #Balance
        print("\n")
        print("Oldmoney:",oldmoney)

        newmoney = oldmoney + int(money)

        # Update operation of the money
        # newmoney = oldmoney + money_deposited
        print("New Money:",newmoney)

        cur.execute(""" UPDATE Bank SET Balance=:1
        WHERE AccountNo=:2 AND Password=:3""",(newmoney,AccountNo,Password))




    def insert(self):
        First_Name = input("Enter First Name:")
        Second_Name = input("Enter Second Name:")
        Address = input("Enter Address:")
    #    Account_No = input("Enter Account_No:") # It must be unique
        Password = input("Enter Password:")

        Admin = input("Are you a admin:")
        if(Admin== "yes"):

            Admin = int(1)

        else:

            Admin = int(0)

        #print("Your Account No is:")

        cur.execute(
            """
            SELECT COUNT(*) FROM Bank
            """
        )
        data = str(cur.fetchall()) #Now forms list object
        print(data)

        no = ""
        for i in data:
            if(i!="[" and i!="," and i!="]" and i!="(" and i!=")"):
                no+=i

        print("No of records present",no)
        AccountNo = int(no) + 1
        print("Your AccountNo:",AccountNo)

        balance = int(0)

        # Inserting datas into the database
        cur.execute(
            """
            Insert into Bank values(:1,:2,:3,:4,:5,:6,:7)
            """
            ,
            (AccountNo,Password,First_Name,Second_Name,Address,balance,Admin)

            )
        print("Your Filled out details:\n")

        cur.execute("""
        SELECT *from Bank WHERE AccountNo=:1 AND Password=:2""",(AccountNo,Password)

        )
        for row in cur:
            print("Account No:",int(row[0])) #Contact No
            print("Password:",str(row[1])) #Password
            print("First_Name:",str(row[2])) #First_Name
            print("Second_Name:",str(row[3])) #Second_Name
            print("Address:",str(row[4])) #Address
            print("Balance:",str(row[5])) #Balance
        print("\n")



obj = Bank()
print("Enter 1 for new user")
print("Enter 2 for old user")
n = int(input())

if n == 1:
        # Insert Signup Details
    print("Insert")
    obj.insert()
else:
    # Authenticate
    AccountNo = int(input("Enter AccountNo:"))
    Password = input("Enter Password:")

    cur.execute("""SELECT count(1) from Bank WHERE AccountNo=:1 AND Password=:2""",(AccountNo,Password))

    ### Storing the result of the query

    data = str(cur.fetchall()) #Now forms list object
    Element_Present = 0
    for i in data:
        if(i=="1"):
            Element_Present = 1
    print("No is present",Element_Present)


    # Now if Element_Present ==1
    if Element_Present == 1:
        cur.execute("""
        SELECT *from Bank WHERE AccountNo=:1 AND Password=:2""",(AccountNo,Password)

        )
        if(AccountNo==1):
            print("Hello Administrator!")
            obj.statistics()

        else:
            for row in cur:
                print("\nHello ",str(row[2])," ",str(row[3]))
                print("\nYour Current Balance:",str(row[5])) #Balance
            print("\n")

            # Choose option
            print("Enter 1 to Withdrawl amount:")
            print("Enter 2 to Deposit amount:")
            print("Enter 3 to exit")
            no = int(input())

            if(no==2):
                #Depositing money
                money = int(input("Enter money to be deposited: "))
                obj.deposit(money,AccountNo,Password)
            elif(no==1):
                #Withdraw money
                money = int(input("Enter the money to be withrawl"))
                obj.withdrawal(money,AccountNo,Password)
            else:
                print("Your Password and Account No does not match")

            cur.execute("""
            SELECT *from Bank WHERE AccountNo=:1 AND Password=:2""",(AccountNo,Password)

            )
            for row in cur:
                print("\nYour Current Balance:",str(row[5])) #Balance
            print("\n")

    ### Admin can view the entire changes


con.commit() #saves changes to the database
con.close()
