import pymysql
mydb=pymysql.connect(host="localhost",user="root",passwd="1")

mycursor=mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")

while True:
    print("""L.O.L. MEDICINE STORE
1:Sign up
2:Log in""")

    ch=int(input("SIGN UP/LOG IN(CHOOSE FROM 1,2):"))

#SIGN UP
    if ch==1:

        username=input("USERNAME:")
        pw=input("PASSWORD:")

        mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
        mydb.commit()

#LOG IN
    elif ch==2:

        username=input("USERNAME:")

        mycursor.execute("select username from signup where username='"+username+"'")
        oof=mycursor.fetchone()

        if oof is not None:
            print("VALID USERNAME")

            pw=input("PASSWORD:")

            mycursor.execute("select password from signup where password='"+pw+"'")
            a=mycursor.fetchone()

            if a is not None:
                print("""---LOGIN SUCCESSFUL!!!---""")

                print("""=============================================
                L.O.L. MEDICINE STORE
=============================================""")

                mycursor.execute("create table if not exists Available_Meds(MedName varchar(30) primary key ,Quantity int(3),Company varchar(30),Price int(4))")
                mycursor.execute("create table if not exists Sell_rec(CustomerName varchar(20),PhoneNumber char(10) unique key, MedName varchar(30),Quantity int(100),Price int(4),foreign key (MedName) references Available_Meds(MedName))")
                mycursor.execute("create table if not exists Staff_details(Name varchar(30), Gender varchar(10),Age int(3), PhoneNumber char(10) unique key , Address varchar(40))") 
                mydb.commit()

                while(True):
                    print("""1:Add Medicines
2:Delete Medicines
3:Search Medicines
4:Staff Details
5:Sell Record
6:Available Medicines
7:Total Income after the Latest Reset 
8:Exit""")

                    a=int(input("Enter your choice:"))

    #ADDING MEDICINES
                    if a==1:

                        print("All information prompted are mandatory to be filled")
                    
                        meds=str(input("Enter Medicine Name:"))
                        quantity=int(input("Enter quantity:"))
                        company=str(input("Enter Company name:"))
                        price=int(input("Enter the price:"))

                        mycursor.execute("select * from Available_Meds where Medname='"+meds+"'")
                        row=mycursor.fetchone()

                        if row is not None:
                            mycursor.execute("update Available_Meds set quantity=quantity+'"+str(quantity)+"' where Medname='"+meds+"'")
                            mydb.commit()

                            print("""---SUCCESSFULLY ADDED!!---""")
                        
                        
                        else:
                            mycursor.execute("insert into Available_Meds(Medname,quantity,company,price) values('"+meds+"','"+str(quantity)+"','"+company+"','"+str(price)+"')")
                            mydb.commit()

                            print("""---SUCCESSFULLY ADDED!!---""") 
                   

    #DELETE MEDICINES
                    elif a==2:                

                        print("AVAILABLE MEDICINES...")

                        mycursor.execute("select * from Available_Meds ")
                        for x in mycursor:
                            print(x)
                      
                        cusname=str(input("Enter customer name:"))
                        phno=int(input("Enter phone number:"))
                        meds=str(input("Enter Medicine Name:"))
                        price=int(input("Enter the price:"))
                        n=int(input("Enter quantity:"))

                        mycursor.execute("select quantity from available_Meds where Medname='"+meds+"'")
                        tf=mycursor.fetchone()

                        if max(tf)<n:
                            print(n,"Medicines are not available!!!!")

                        else:
                            mycursor.execute("select Medname from available_Meds where Medname='"+meds+"'")
                            log=mycursor.fetchone()

                            if log is not None:
                                mycursor.execute("insert into Sell_rec values('"+cusname+"','"+str(phno)+"','"+meds+"','"+str(n)+"','"+str(price)+"')")
                                mycursor.execute("update Available_Meds set quantity= quantity-("+str(n)+") where MedName=('"+meds+"')")
                                mydb.commit()

                                print("""---MEDICINE HAS BEEN SOLD!!!---""")

                            else:
                                print("---MEDICINE IS NOT AVAILABLE!!!---")

    #SEARCH MEDICINES ON THE BASIS OF GIVEN OPTIONS
                    elif a==3:

                        print("""1:Search by name
2:Search by company""")

                        l=int(input("Search by?:"))

        #BY MEDICINE NAME
                        if l==1:
                            o=input("Enter Medicine to search:")

                            mycursor.execute("select medname from available_meds where medname='"+o+"'")
                            tree=mycursor.fetchone()

                            if tree!=None:
                                print("""---MEDICINE IS IN STOCK!!!---""")

                            else:
                                print("---MEDICINE IS NOT IN STOCK!!!---")


        #BY COMPANY NAME
                        elif l==2:
                            com=input("Enter company to search:")

                            mycursor.execute("select company from available_meds where company='"+com+"'")
                            home=mycursor.fetchall()

                            if home is not None:
                                print("""---MEDICINE BY THIS COMPANY IS IN STOCK!!!---""")

                                mycursor.execute("select * from available_meds where company='"+com+"'")

                                for z in mycursor:
                                    print(z)

                            else:
                                print("---MEDICINES OF THIS COMPANY ARE NOT AVAILABLE!!!---")
                        mydb.commit()

    #STAFF DETAILS
                    elif a==4:
                        print("1:New staff entry")
                        print("2:Remove staff")
                        print("3:Existing staff details")

                        ch=int(input("Enter your choice:"))

        #NEW STAFF ENTRY
                        if ch==1:
                            fname=str(input("Enter Fullname:"))
                            gender=str(input("Gender(M/F/O):"))
                            age=int(input("Age:"))
                            phno=int(input("Staff phone no.:"))
                            add=str(input("Address:"))

                            mycursor.execute("insert into Staff_details(name,gender,age,phonenumber,address) values('"+fname+"','"+gender+"','"+str(age)+"','"+str(phno)+"','"+add+"')")
                            print("""---STAFF IS SUCCESSFULLY ADDED!!!---""")
                            mydb.commit()

        #REMOVE STAFF
                        elif ch==2:
                            nm=str(input("Enter staff name to remove:"))
                            mycursor.execute("select name from staff_details where name='"+nm+"'")
                            toy=mycursor.fetchone()

                            if toy is not None:
                                mycursor.execute("delete from staff_details where name='"+nm+"'")
                                print("""---STAFF IS SUCCESSFULLY REMOVED---""")
                                mydb.commit()

                            else:
                                print("---STAFF DOESNOT EXIST!!!---")

        #EXISTING STAFF DETAILS
                        elif ch==3:
                            mycursor.execute("select * from Staff_details")
                            run=mycursor.fetchone()
                            for t in mycursor:
                                print(t)
                            if run is not None:
                                print("EXISTING STAFF DETAILS...")                        
                                for t in mycursor:
                                    print(t)

                            else:
                                print("---NO STAFF EXISTS!!!---")
                            mydb.commit()

    #SELL HISTORY                                
                    elif a==5:
                        print("1:Sell history details")
                        print("2:Reset Sell history")

                        ty=int(input("Enter your choice:"))

                        if ty==1:
                            mycursor.execute("select * from sell_rec")
                            for u in mycursor:
                                print(u)

                        if ty==2:
                            bb=input("Are you sure(Y/N):")

                            if bb=="Y":
                                mycursor.execute("delete from sell_rec")
                                mydb.commit()

                            elif bb=="N":
                                pass

    #AVAILABLE MEDICINES
                    elif a==6:
                        mycursor.execute("select * from available_meds order by medname")
                        for v in mycursor:
                            print(v)

    #TOTAL INCOME AFTER LATEST UPDATE
                    elif a==7:
                        mycursor.execute("select sum(price) from sell_rec")
                        for x in mycursor:
                            print(x)
    #EXIT                    
                    elif a==8:
                        break

#LOGIN ELSE PART
            else:
                print("""---INCORRECT PASSWORD---""")


        else:
            print("""---INVALID USERNAME---""")

    else:
        break
