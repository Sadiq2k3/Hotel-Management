import mysql.connector as con
connector=con.connect(host="localhost",user="root", password= "sql2005")
sql_con=connector.cursor()
def Menu():
    print("\n======================================================================================================")
    print("\n\t\t\t\t\tWELCOME TO THE MAIN MENU")
    print("\n\t\t\t\t\tPress 1 FOR THE ENTRY")
    print("\n\t\t\t\t\tPRESS 2 FOR ROOM SELECTION")
    print("\n\t\t\t\t\tPress 3 TO CHECKIN CHECKOUT DETAILS")
    print("\n\t\t\t\t\tPRESS 4 FOR CUSTOMER DETAILS")
    print("\n\t\t\t\t\tPRESS 5 FOR RESTAURANT")
    print("\n\t\t\t\t\tPRESS 6 FOR UPDATING")
    print("\n\t\t\t\t\tPRESS 7 TO BILL")
    print("\n\t\t\t\t\tPRESS 8 TO CLOSE")
    
    ch=int(input("\n\t\t\t\t\tENTER YOUR CHOICE= "))
    if ch==1:
        Id=int(input("\n\n\t\t\t\tEnter the customer ID="))
        UserEntry(Id)
    elif ch == 2:
        Id=int(input("\n\n\t\t\t\tEnter the customer ID="))
        Roomrent(Id)
    elif ch==3:
        Id=int(input("\n\n\t\t\t\tEnter the customer ID="))
        Booking(Id)
    elif ch==4:
        searchCustomer()
    elif ch==5:
        restaurant()
    elif ch==6:
        update()
    elif ch==7:
        bill()
    elif ch==8:
        print("Thank for using")
        exit()
    else:
        print("Invalid choice")
        Menu()
def Loader():
    i=3
    while i >=0:
        print("\n\n\t\t\t\t\tWELCOME TO THE LOGIN WINDOW")
        A=input("\n\t\t\t\t\tEnter the Password= ")
        if A == "Rad123":
            D=1
            return D
        if i ==0:
                print("\n\t\t\t\t\tBetter luck next time")
                break
        else:
            print("\n\t\t\t\t\tInvalid Password")
            print("\n\t\t\t\t\tYou have", i, "tries")
            i=i-1
def UserEntry(Id):
    print("\n\n\t\t\t\t\tWELCOME TO THE ENTRY WINDOW")
    sql1=("CREATE DATABASE IF NOT EXISTS HOTEL_MANAGEMENT")
    sql_con.execute(sql1)
    connector.commit()
    sql2=("Use HOTEL_MANAGEMENT")
    sql_con.execute(sql2)
    connector.commit()
    sql3=("""CREATE TABLE IF NOT EXISTS CUSTOMER_ID(SQO int(10), C_ID int(10), C_Name CHAR(30),
            Nationality CHAR(30), C_EMAILID VARCHAR(100), C_TeleNo BIGINT(15), Tmembers Int(2))""")
    sql_con.execute(sql3)
    SQO=Id
    NAME=input("\n\t\t\t\tEnter the Customer Name= ")
    Nation=input("\n\t\t\t\tEnter the Customer Nationality= ")
    Email=input("\n\t\t\t\tEnter the email ID=")
    Tele=int(input("\n\t\t\t\tEnter the Telephone No= "))
    Tm=int(input("\n\t\t\t\tEnter the no of members= "))
    sql4=("""Insert Into CUSTOMER_ID Values({}, {},'{}','{}','{}',{},{})""").format(SQO,Id,NAME,Nation,Email,Tele,Tm)
    sql_con.execute(sql4)
    connector.commit()
    print("REMEMBER YOUR ID IS", Id)
    ch=input("\n\n\t\t\t\t\tWant to enter the Main Menu(Y/N)= ")
    if ch in "Yy":
        Menu()
    Roomrent(Id)
def Roomrent(Id):
    sql2=("Use HOTEL_MANAGEMENT")
    sql_con.execute(sql2)
    connector.commit()
    print("\n\t\t\t\tWE HAVE BEST ROOMS WITH ALL COMFORTABLE FACILITIES")
    global roomrent
    D={"1  Single bed room":1700,"2  Double bed room":2000,"3  King feel room":4500,
       "4  Quad bed room":2700,"5  Luxury Suite":3000,"6  Geminal suite":6000,"7  Rebound Suite":5000,
       "8  Apartment room":1000}
    print("\n\t\t\t\t\t No\tRooms \t\t Rent(per day)")
    for rooms in D:
        print("\t\t\t\t\t",rooms,"\t:\t", D[rooms])
    F=int(input("\n\t\t\t\tEnter the days you will stay= "))
    while True:
        ch=int(input("\n\t\t\t\tEnter the S.no of room of customer's choice="))
        if ch==1:
             roomrent=F*1700
             A="Single room"
             print("\n\t\t\t\tSingle room rent:",roomrent)
             break
        elif ch==2:
             roomrent=F*2000
             A="Double room"
             print("\n\t\t\t\tDouble room rent:",roomrent)
             break
        elif ch==3:
             roomrent=F*4500
             A="King room"
             print("\n\t\t\t\tKing room rent:",roomrent)
             break
        elif ch==4:
             roomrent=F*2700
             A="Quad room"
             print("\n\t\t\t\tQuad room rent:",roomrent)
             break
        elif ch==5:
             roomrent=F*3000
             A="Luxury Suite"
             print("\n\t\t\t\tLuxury Suite rent:",roomrent)
             break
        elif ch==6:
             roomrent=F*6000
             A="Geminal Suite"
             print("\n\t\t\t\tGeminal suite rent:",roomrent)
             break
        elif ch==7:
             roomrent=F*10000
             A="Apartment room"
             print("\n\t\t\t\tApartment room rent:",roomrent)
             break
        elif ch==8:
             roomrent=F*3000
             A="Adjoining room "
             print("\n\t\t\t\tAdjoining room rent:",roomrent)
             break
        else:
             print("\n\t\t\t\t\tSorry!!Wrong input")
    RoomNo=int(input("\n\t\t\t\tEnter the room No= "))
    sql1=("CREATE TABLE IF NOT EXISTS Room_rent(C_ID Bigint(10), RoomNo int(4), RoomType Char(30), Roomrent BIGINT(25), DAYS_of_Staying INT(5))")
    sql_con.execute(sql1)
    connector.commit()
    sql=("INSERT INTO Room_rent values({},{},'{}',{},{})").format(Id,RoomNo,A,roomrent,F)
    sql_con.execute(sql)
    connector.commit()
    print("\n\n==========================================================================================================")
    print("\n\n\t\t\t\t\t\tThank you\n \t\t\t\tYour room no is", RoomNo ,"which is booked for",F, "days" )
    print("\n\t\t\t\t\tThe total roomrent will be", roomrent)
    ch=input("\n\n\t\t\t\t\tWant to enter the Main Menu(Y/N)= ")
    if ch in "Yy":
        Menu()
    Booking(Id)
def Booking(Id):
    sql5=("CREATE TABLE IF NOT EXISTS Booking_Details(C_ID int(10), CHECK_IN VARCHAR(40), CHECK_OUT VARCHAR(40))")
    sql_con.execute(sql5)
    connector.commit()
    checkin=input("\n\t\t\t\tEnter the Checkin Date{use format(DD.MM.YYYY)}= ")
    checkout=input("\n\t\t\t\tEnter the Checkout Date{use format(DD.MM.YYYY)}= ")
    sql="INSERT INTO Booking_details VALUES({},'{}','{}')".format(Id,checkin,checkout)
    sql_con.execute(sql)
    connector.commit()
    Menu()
def searchCustomer():
    sql2=("Use HOTEL_MANAGEMENT")
    sql_con.execute(sql2)
    connector.commit()
    cid=int(input("\n\t\tEnter the customer ID[PRESSS 0 if not known]="))
    if cid==0:
        cname=input("\n\t\t\t\t\tENTER CUSTOMER NAME:")
        sql="select * FROM customer_id C, Room_rent R, Booking_details B where C.C_ID=R.C_ID=B.C_ID and C_Name='{}'".format(cname)
        sql_con.execute(sql)
        data=sql_con.fetchone()
        if data==():
            print("\n\t\t\t\t\tNo Record is Here")
        else:
            print("Customer ID=", data[1])
            print("Customer Name=", data[2])
            print("Customer Nationality=", data[3])
            print("Customer EmailID=", data[4])
            print("Customer Telephone No =", data[5])
            print("Members staying=", data[6])
            print("Customer RoomNo=", data[8])
            print("Customer RoomType=", data[9])
            print("No of days staying=", data[11])
            print("Check in Date=", data[13])
            print("Chek out Date=", data[14])
    else:
        sql="select * FROM customer_id C, Room_rent R, Booking_details B where C.C_ID=R.C_ID=B.C_ID and SQO={}".format(cid)
        sql_con.execute(sql)
        data=sql_con.fetchall()
        if data==[]:
            print("\n\t\t\t\t\tNo Record is Here")
        else:
            for i in data:
                print("Customer ID=", i[1])
                print("Customer Name=", i[2])
                print("Customer Nationality=", i[3])
                print("Customer EmailID=", i[4])
                print("Customer Telephone No =", i[5])
                print("Members staying=", i[6])
                print("Customer RoomNo=", i[8])
                print("Customer RoomType=", i[9])
                print("No of days staying=", i[11])
                print("Check in Date=", i[13])
                print("Chek out Date=", i[14])
    ch=input("\n\n\t\t\t\t\tWant to enter the Main Menu(Y/N)= ")
    if ch in "Yy":
        Menu()
    searchCustomer()
def update():
    sql2=("Use HOTEL_MANAGEMENT")
    sql_con.execute(sql2)
    connector.commit()
    print("\n\t\t\t\t\tWhich data is needed to be updated")
    print("\n\t\t\t\t\tPRESS 1 FOR Customer Id")
    print("\n\t\t\t\t\tPRESS 2 FOR Booking Details")
    print("\n\t\t\t\t\tPRESS 3 FOR Room")
    Ch=int(input("Enter the choice= "))
    if Ch==1:
        cid=int(input("\n\t\tEnter the customer ID[PRESSS 0 if not known]="))
        if cid==0:
            cname=input("\n\t\t\t\t\tENTER CUSTOMER NAME:")
            sql="select * from customer_Id where C_Name={}".format(cid)
            sql_con.execute(sql)
            record=sql_con.fetchall()
            Id=record[0][1]
            sql="delete FROM customer_id where C_Name='{}'".format(cname)
            sql_con.execute(sql)
            connector.commit()
            print("Record deleted succesfully")
            UserEntry(Id)
        else:
            sql="delete FROM customer_id where C_Id={}".format(cid)
            sql_con.execute(sql)
            connector.commit()
            print("Record deleted successfully")
            sql="select * from Booking_details where C_ID={}".format(cid)
            sql_con.execute(sql)
            record=sql_con.fetchone()
            UserEntry(Id)
    elif Ch==2:
        cid=int(input("\n\t\tEnter the customer ID="))
        sql="delete FROM Booking_details where C_Id={}".format(cid)
        sql_con.execute(sql)
        connector.commit()
        print("Record deleted successfully")
        Booking(cid)
    elif Ch==3:
        cid=int(input("\n\t\tEnter the customer ID[PRESSS 0 if not known]="))
        sql="delete FROM Room_rent where C_Id={}".format(cid)
        sql_con.execute(sql)
        connector.commit()
        print("Record deleted successfully")
        Roomrent(cid)
    else:
        print("Invalid choice")
        update()
def restaurant():
    sql2=("Use HOTEL_MANAGEMENT")
    sql_con.execute(sql2)
    connector.commit()
    print("\t\t\t\t WELCOME TO THE GRAND KITCHEN OF RADDISON BLU \t\t\t\t")
    """sql_con.execute("select * from menu")
    for dish in sql_con:
        print(dish)"""
    sql3=("CREATE TABLE IF NOT EXISTS RESTAURANT(C_ID int(10), dishchoice VARCHAR(40), qty int(10), restaurantbill INT(10))")
    sql_con.execute(sql3)
    connector.commit()
    cust_id=input("customer ID:")
    dishchoice=int(input("Enter dish or item number:"))
    qty=int(input("Enter quantity:"))
    global restaurantbill
    if dishchoice==1:
        restaurantbill=qty*150
        print("YOU ORDERED PIZZA")
    elif dishchoice==2:
        restaurantbill=qty*60
        print("YOU ORDERED BURGER")
    elif dishchoice==3:
        restaurantbill=qty*90
        print("YOU ORDERED ALFREDO PASTA")
    elif dishchoice==4:
        restaurantbill=qty*70
        print("YOU ORDERED FRENCH FRIES")
    elif dishchoice==5:
        restaurantbill=qty*200
        print("YOU ORDERED SOUTH INDIAN THALI")
    elif dishchoice==6:
        restaurantbill=qty*200
        print("YOU ORDERED NORTH INDIAN THALI")
    elif dishchoice==7:
        restaurantbill=qty*250
        print("YOU ORDERED CHINESE PLATTER")
    elif dishchoice==8:
        restaurantbill=qty*100
        print("YOU ORDERED MEXICAN TACO")
    elif dishchoice==9:
        restaurantbill=qty*90
        print("YOU ORDERED CHOLE BHATURE")
    elif dishchoice==10:
        restaurantbill=qty*60
        print("YOU ORDERED PAPDI CHAAT")
    elif dishchoice==11:
        restaurantbill=qty*40
        print("YOU ORDERED SOFT DRINK")
    elif dishchoice==12:
        restaurantbill=qty*30
        print("YOU ORDERED TEA")
    elif dishchoice==13:
        restaurantbill=qty*50
        print("YOU ORDERED COFFEE")
    elif dishchoice==14:
        restaurantbill=qty*75
        print("YOU ORDERED MILKSHAKE")
    elif dishchoice==15:
        restaurantbill=qty*45
        print("YOU ORDERED ICE CREAM")
    elif dishchoice==16:
        restaurantbill=qty*30
        print("YOU ORDERED JALEBI")
    elif dishchoice==17:
        restaurantbill=qty*50
        print("YOU ORDERED DAL HALWA")
    elif dishchoice==18:
        restaurantbill=qty*100
        print("YOU ORDERED WAFFLES")
    elif dishchoice==19:
        restaurantbill=qty*20
        print("YOU ORDERED GULAB JAMUN")
    elif dishchoice==20:
        restaurantbill=qty*80
        print("YOU ORDERED RABRI")
    else:
        print("INVALID CHOICE!! NO SUCH DISH IS AVAILABLE")
    sql="INSERT INTO RESTAURANT VALUES({},'{}',{},{})".format(cust_id,dishchoice,qty,restaurantbill)
    sql_con.execute(sql)
    connector.commit()
    print("YOU HAVE TO PAY RS.",restaurantbill)
    Menu()
def bill():
    sql2=("Use HOTEL_MANAGEMENT")
    sql_con.execute(sql2)
    connector.commit()
    print("\n\t\t\t HOPE YOU HAD A GOOD TIME!! PLEASE PAY THE BILLS")
    cid = int(input("ENTER CUSTOMER IF:"))
    sql="select * from customer_id where C_ID={}".format(cid)
    sql_con.execute(sql)
    record=sql_con.fetchall()
    print("\t\t\t\tBILL")
    print('-'*100)
    ss="select restaurantbill from restaurant where C_ID={}".format(cid)
    sql_con.execute(ss)
    resbill=sql_con.fetchall()
    C=(0,)
    for i in resbill:
        C=C+i
    Tresbill=sum(C)
    ss1="select roomrent from Room_rent where C_ID={}".format(cid)
    sql_con.execute(ss1)
    rent=sql_con.fetchall()
    Trent=rent[0][0]
    Gtotal=Tresbill+Trent
    print("\t\t RADDISON BLU HOTEL \n\t\t GRAND BILLING")
    print("\t\t CUSTOMER ID:", record[0][1])
    print("\t\t CUSTOMER NAME:",record[0][2])
    print("\t\t ROOM RENT:",Trent)
    print("\t\t RESTAURANT BILL:",Tresbill)
    print("\t\t TOTAL AMOUNT:Rs.",Gtotal)
    
    F1="delete FROM Booking_details where C_Id={}".format(cid)
    sql_con.execute(F1)
    connector.commit()
    F2="delete FROM customer_id where C_Id={}".format(cid)
    sql_con.execute(F2)
    connector.commit()
    F3="delete FROM Room_rent where C_Id={}".format(cid)
    sql_con.execute(F3)
    connector.commit()
    F4="delete FROM restaurant where C_Id={}".format(cid)
    sql_con.execute(F4)
    connector.commit()
    print("Thanks for staying with us")
    Menu()
D=Loader()
if D==1:
    Menu()
