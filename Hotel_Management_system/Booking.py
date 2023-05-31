#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
import Records
import Global
import mysql.connector
mydb = mysql.connector.connect(   
host='localhost',
user='root',
password='Hurtisaliar593@',
database='hotel1'
)
current_date = datetime.date.today()
def Booking():
    try:
        print("1. New Booking")
        print("2. Past Bookings and Upcoming booking status")
        print("0. HOME")
        b = int(input("-> "))
        if b == 1:
            print("----------------------------------------------------------------------------------------------------------")
            chk_in= str(input("Enter check-in date of the customer (yyyy-mm-dd format only): "))
            if not isinstance(chk_in, str) or not chk_in.strip():
                    raise ValueError("Please enter a valid check-in date.") 
            ci=datetime.datetime.strptime(chk_in, "%Y-%m-%d").date()
            if ci >= current_date:
                rm = input("Enter Room number of the customer: ")
                start, end = map(int,Global.rmno.split("-"))
                st, e = map(int,Global.rmno1.split("-"))
                sta, en = map(int,Global.rmno2.split("-"))
                if int(rm) in range(start, end + 1):
                    cur = mydb.cursor()
                    s = "SELECT Room_no FROM Booking WHERE ccheck_in <= %s AND ccheck_out >= %s AND Room_no = %s"
                    cur.execute(s,(ci,ci,rm))
                    myresult = cur.fetchone()
                    if myresult is None:
                        print("Room is available")
                    else:
                        print("Room is booked")
                        Booking()
                elif int(rm) in range(st, e + 1):
                    cur = mydb.cursor()
                    s = "SELECT Room_no FROM Booking WHERE ccheck_in <= %s AND ccheck_out >= %s AND Room_no = %s"
                    cur.execute(s,(ci,ci,rm))
                    myresult = cur.fetchone()
                    if myresult is None:
                        print("Room is available")
                    else:
                        print("Room is booked")
                        Booking()
                elif int(rm) in range(sta, en + 1):
                    cur = mydb.cursor()
                    s = "SELECT Room_no FROM Booking WHERE ccheck_in <= %s AND ccheck_out >= %s AND Room_no = %s"
                    cur.execute(s,(ci,ci,rm))
                    myresult = cur.fetchone()
                    if myresult is None:
                        print("Room is available")
                    else:
                        print("Room is booked")
                        Booking()
                else:
                    print("WRONG VALUE")
                    Rooms_Info()
                    Booking() 
                chk_out = str(input("\nEnter check-out date of the customer (yyyy-mm-dd format only): "))
                if not isinstance(chk_out, str) or not chk_out.strip():
                    raise ValueError("Please enter a valid check-out date.")
                co=datetime.datetime.strptime(chk_out, "%Y-%m-%d").date()
                if co>=current_date and co>=ci: 
                    cur = mydb.cursor()
                    s = "SELECT Room_no FROM Booking WHERE ccheck_in <= %s AND ccheck_out >= %s AND Room_no = %s"
                    cur.execute(s,(co,co,rm))
                    myresult = cur.fetchone()
                    if myresult is None:
                        print("Room is available")
                    else:
                        print("Room is booked")
                        Records.all_record()
                        Booking()
                else:
                    print("OOPS PAST IS PAST( YOU ENTER WRONG VALUE))")
                    print("TRY AGAIN")
                    print("--------------------------------------------------------------------------------------------------")
                    Booking()
                n = input("\nEnter name of the customer: ")
                if not isinstance(n,str) or n.isspace():
                    raise ValueError("Please enter a valid name.")
                a = input("\nEnter address of the customer: ")
                if  not all(c.isalpha() or c.isspace() for c in a):
                    raise ValueError("Please enter a valid address.")
                p = int(input("\nEnter the phone number: "))
                if not isinstance(p,int):
                    raise ValueError("Wrong Entry")     
                iid=input("\nEnter the id type(adhar card or driving license etc): ")
                if not isinstance(iid,str) :
                    raise ValueError("Please enter a valid details")
                adhar = int(input("\nEnter id number:  "))
                if not isinstance(adhar,int) : 
                    raise ValueError("Please enter correct details")
                n1=int(input("\nEnter the number of adults(Age is more than 18): "))
                if n1>2:
                    n1=n1-2
                    new_price=n1*int(Global.extpers)
                else:
                    new_price=0
                checkin_date = datetime.datetime.strptime(chk_in, "%Y-%m-%d").date()
                checkout_date = datetime.datetime.strptime(chk_out, "%Y-%m-%d").date()
                duration = checkout_date - checkin_date
                duration = duration.days                 
                start, end = map(int,Global.rmno.split("-"))
                st, e = map(int,Global.rmno1.split("-"))
                sta, en = map(int, Global.rmno2.split("-"))
                if int(rm) in range(start, end + 1):
                    print("Per night rent of room is:",Global.prm)
                    Price=new_price+int(Global.prm)
                    print("Per day rent of your room is with all members:",Price)
                    total =Price*duration
                    print("Total price pay is:",total)
                elif int(rm) in range(st, e + 1):
                    print("Per night rent is:",Global.prm1)
                    Price=new_price+int(Global.prm1)
                    print("Per day rent of your room is with all members:",Price)
                    total =Price*duration
                    print("Total price pay is:",total)
                elif int(rm) in range(sta, en + 1):
                    print("Per night rent is:",Global.prm2)
                    Price=new_price+int(Global.prm2)
                    print("Per day rent of your room is with all members:",Price)
                    total =Price*duration
                    print("Total price pay is:",total)
                else:
                    print("Wrong entry")
                    Booking()
                adv = int(input("\nAdvance collected by the customer:  "))
                left_amount = total - adv
                print("Total amount pending to collect :", left_amount)
                cur=mydb.cursor()
                s="INSERT INTO Booking(cname,caddress,cphn_number,ccheck_in,ccheck_out,Room_no,room_rent,Advance,Left_amt) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                b1=(n,a,p,ci,co,rm,total,adv,left_amount)
                cur.execute(s,b1)
                mydb.commit()
                print("CONGRATS ROOM IS BOOKED FOR ",n)
            else:
                print("OOPS PAST IS PAST( YOU ENTER WRONG VALUE))")
                print("TRY AGAIN")
                print("--------------------------------------------------------------------------------------------------")
                Booking()
        elif b == 2:
            print("1. Check upcoming bookings")
            print("2. Past Bookings status")
            print("0. Home")
            b1 = int(input("-> "))
            if b1 == 1:
                Records.upcoming_record()
                Booking()
            elif b1 == 2:
                Records.past_record()
                Booking()
            elif b==0:
                Booking()
            else:
                print("Please enter correct option")
        elif b==0:
             Booking()
        else:
            print("Please enter correct option")
    except ValueError:
        print("Invalid input! Please Enter correct Value format.")
    except Exception as e:
        print("An error occurred: ", e)
    finally:
        print("")


# In[ ]:




