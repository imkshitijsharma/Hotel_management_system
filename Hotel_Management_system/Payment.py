#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector
mydb = mysql.connector.connect(   
  host='localhost',
  user='root',
  password='Hurtisaliar593@',
  database='hotel'
)
def clear_pay():
        try:
            R=int(input("Enter the Room number to check the left balance"))
            ch=str(input("Enter the checkout date of the room"))
            cur = mydb.cursor()
            s = "SELECT Left_amt FROM Booking WHERE ccheck_out = %s AND Room_no=%s"
            cur.execute(s,(ch,R))
            myresult = cur.fetchall()
            result=int(myresult[0][0])
            print("Left amount payable :",result) 
            print("1.TO clear the Left balance")
            print("2.To update the left balance")
            print("0.Home")
            R1=int(input("Enter the Option "))
            if R1==1:
                cur = mydb.cursor()
                s = "UPDATE Booking SET Left_amt = NULL WHERE Room_no=%s AND ccheck_out = %s"
                cur.execute(s,(R,ch))
                mydb.commit() 
                clear_pay()
            elif R1==2:
                money=int(input("Enter the amount to add"))
                cur = mydb.cursor()
                s = "UPDATE Booking SET Left_amt =%s WHERE Room_no=%s AND ccheck_out = %s"
                cur.execute(s,(money,R,ch))
                mydb.commit() 
                clear_pay()
            elif R1==0:
                return
            else:
                print("OOPS WRONG ENTRY")
                return
        except ValueError:
            print("Invalid input! Please Enter correct Value format.")
            clear_pay()
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            print("")
                
                
def pending_pay():
    print("1. See pending payments of rooms")
    print("2. Update and clear the payment ")
    print("0. HOME")
    try:
        pay=int(input("->"))
        if pay==1:
            d=str(input('Enter Checkout date to check the payments pending (yyyy-mm-dd format only): '))
            cur = mydb.cursor()
            s = "SELECT Room_no,Left_amt FROM Booking WHERE Left_amt IS NOT NULL AND ccheck_out=%s "
            cur.execute(s,(d,))
            myresult = cur.fetchall()
            print(myresult)
        elif pay==2:
            clear_pay()
        elif pay==0:
             return
        else:
            print("OOPS WRONG ENTRY")
    except ValueError:
        print("Invalid input! Please Enter correct Value format.")
        pending_pay()
    except Exception as e:
        print("An error occurred: ", e)
    finally:
        print("")
        


# In[ ]:




