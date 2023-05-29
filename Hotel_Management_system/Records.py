#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='Hurtisaliar593@',
  database='hotel'
)   
def past_record():
        print('\033[1;31m' + "VISITED GUESTS: >" + '\033[0m')
        cur = mydb.cursor()
        s = "SELECT * FROM Booking WHERE ccheck_out <= curdate()"
        cur.execute(s)
        myresult = cur.fetchall()
        col_names = [i[0] for i in cur.description]
        max_lens = [len(name) for name in col_names]
        for row in myresult:
            for i, value in enumerate(row):
                max_lens[i] = max(max_lens[i], len(str(value)))
        header = ' | '.join(name.ljust(max_lens[i]) for i, name in enumerate(col_names))
        print(header)
        for row in myresult:
            row_str = ' | '.join(str(value).ljust(max_lens[i]) for i, value in enumerate(row))
            print(row_str)
        print(">>>>>>>>>>>>>>>>>>.>>>>>>>>>>>")
        
def upcoming_record():
        print('\033[1;31m' + "UPCOMING GUESTS: >" + '\033[0m')
        cur = mydb.cursor()
        s = "SELECT * FROM Booking WHERE ccheck_in >= curdate()"
        cur.execute(s)
        myresult = cur.fetchall()
        col_names = [i[0] for i in cur.description]
        max_lens = [len(name) for name in col_names]
        for row in myresult:
            for i, value in enumerate(row):
                max_lens[i] = max(max_lens[i], len(str(value)))
        header = ' | '.join(name.ljust(max_lens[i]) for i, name in enumerate(col_names))
        print(header)
        for row in myresult:
            row_str = ' | '.join(str(value).ljust(max_lens[i]) for i, value in enumerate(row))
            print(row_str)
        print(">>>>>>>>>>>>>>>>>>.>>>>>>>>>>>")
        
def all_record():
        print('\033[1;31m' + "ALL GUESTS THAT STAY TILL TODAY: >" + '\033[0m')
        cur = mydb.cursor()
        s = "SELECT * FROM Booking WHERE ccheck_in >= curdate() OR ccheck_in<= curdate()"
        cur.execute(s)
        myresult = cur.fetchall()
        print(myresult)
        col_names = [i[0] for i in cur.description]
        max_lens = [len(name) for name in col_names]
        for row in myresult:
            for i, value in enumerate(row):
                max_lens[i] = max(max_lens[i], len(str(value)))
        header = ' | '.join(name.ljust(max_lens[i]) for i, name in enumerate(col_names))
        print(header)
        for row in myresult:
            row_str = ' | '.join(str(value).ljust(max_lens[i]) for i, value in enumerate(row))
            print(row_str)
        print(">>>>>>>>>>>>>>>>>>.>>>>>>>>>>>")
        
def record():
        print("Options available:\n")
        print(" 1 Check past booking records\n")
        print(" 2 Check upcoming booking records\n")
        print("3. Check all Bookings till today")
        print("0. MAIN MENU")
        try:
            bk=int(input("Enter your Option"))
            if bk==1:
                past_record()
                record()
            elif bk==2:
                upcoming_record()
                record()
            elif bk==3:
                all_record()
                record()
            elif bk==0:
                return
            else:
                print("WRONG OPTION SELECT")
        except ValueError:
            print("Invalid input! Please Enter correct Value format.")
            Home()
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            print(" ")
            


# In[ ]:




