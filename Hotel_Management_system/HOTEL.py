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
## MODULES importing:
import datetime
import getpass
import Room_info
import Global
from Booking import Booking
current_date = datetime.date.today() ### fetching system date 
import Records
import Payment

def Home():#### main home function
    try:
        print('\t\t\t\t\t\033[1;31m' + "WELCOME TO HOTEL MANAGEMENT SYSTEM" + '\033[0m')
        print('\t\t\t\t\t\t\t\t\t\t\t\t\033[1;34m' + "BY: KGMSoft.." + '\033[0m.\n')
        print('\033[1;32m' + "LOGIN AS:->" + '\033[0m.\n')
        print('\033[1;32m' + "1.OWNER" + '\033[0m.\n')
        print('\033[1;32m' + "2.MANAGER" + '\033[0m.\n')
        print('\033[1;37m' +"0.INFO" + '\033[0m.\n')
        log=int(input('\nEnter your choice: \n'))
        if log==1:
            start=0
            limit=3
            while start<limit:
                name=input("Username: ")
                password = getpass.getpass(prompt="Password: ")
                if name==Global.NAME1 and password==Global.PASS1:
                    Global.admin='OWNER'
                    login()
                else:
                    print("Sorry you have entered wrong password or name")
                    start += 1
                    print(f'you have {limit-start} limit left')
        elif log==2:
            start=0
            limit=3
            while start<limit:
                name=input("Username: ")
                password= getpass.getpass(prompt="Password: ")
                if name==Global.NAME and password==Global.PASS:
                    Global.admin='MANAGER'
                    loginn()
                else:
                    print("Sorry you have entered wrong password or name")
                    start += 1
                    print(f'you have {limit-start} limit left')
        elif log==0:
             read_me()
        else:
            print("OOPS Wrong entry")
    except ValueError:
        print("Invalid input! Please Enter correct Value format.")
    
    finally:
        print("")
        
def login():## owner login
    print("-------------------------------------------------------------------------------------------------------------------")
    print('\t\t\t\t\t\033[1;31m' + "HOTEL MANAGEMENT SYSTEM" + '\033[0m')
    print('\t\t\t\t\t\033[1;31m' + " OF HOTEL " + Global.hotel + '\033[0m.')
    print('\033[1;36m' + "LOGIN AS:" +'\033[0m.',Global.admin,'\t\t\t\t\t\t\t\t\t\033[1;36m' + "ADDRESS:" + '\033[0m.',Global.address)
    print('\033[1;36m' + "CONTACT NUMBER:" +'\033[0m.',Global.phone_numb,'\t\t\t\t\t\t\t\t\033[1;36m' + "EMAIL:" + '\033[0m.',Global.email)
    print("\n")
    print('\033[1;32m' + "MAIN MENU" + '\033[0m.')
    print("1. Booking\n")
    print("2. Check booking record\n")
    print("3. Pending Payment status of rooms\n")
    print("4. Settings\n")
    print("0. Home \n")
    try:
        ch=int(input("ENTER NUMBER TO PERFORM THAT ACTION ->: "))
        if ch == 1:
            Booking()
            
        elif ch==2:
            Records.record()
            
        elif ch == 3:
            Payment.pending_pay()
     
        elif ch == 4:
            setting1()
     
        elif ch==0:
            Home()
        else:
            Print("OOPSYou Enter a wrong value ")
            Home()
    except ValueError:
        print("Invalid input! Please Enter correct Value format.")
        Home()
    except Exception as e:
        print("An error occurred: ", e)
        Home()
    
    finally:
            print(" ")
                
def loginn():### manager login
    print("-------------------------------------------------------------------------------------------------------------------")
    print('\t\t\t\t\t\033[1;31m' + "HOTEL MANAGEMENT SYSTEM" + '\033[0m')
    print('\t\t\t\t\t\033[1;31m' + " OF HOTEL " + Global.hotel + '\033[0m.')
    print('\033[1;36m' + "LOGIN AS:" +'\033[0m.',Global.admin,'\t\t\t\t\t\t\t\t\t\033[1;36m' + "ADDRESS:" + '\033[0m.',Global.address)
    print('\033[1;36m' + "CONTACT NUMBER:" +'\033[0m.',Global.phone_numb,'\t\t\t\t\t\t\t\t\033[1;36m' + "EMAIL:" + '\033[0m.',Global.email)
    print("\n")
    print('\033[1;32m' + "MAIN MENU" + '\033[0m.')
    print("1. Booking\n")
    print("2. Rooms Info\n")
    print("3. Check Future booking record\n")
    print("4. Pending Payment status of rooms\n")
    print("5. Settings\n")
    print("0. Home\n")
    try:
        ch=int(input("ENTER NUMBER TO PERFORM THAT ACTION ->: "))
        if ch == 1:
            Booking()
     
        elif ch == 2:
            print(" ")
            Room_info.Rooms_Info()
     
        elif ch == 3:
            print(" ")
            Records.upcoming_record()
        elif ch == 4:
            print(" ")
            Payment.pending_pay()
     
        elif ch == 5:
            print(" ")
            Setting()
     
        elif ch==0:
            Home()
        else:
            print("YOU ENTER A WRONG INPUT")
    except ValueError:
        print("Invalid input! Please Enter correct Value format.")
    except Exception as e:
        print("An error occurred: ", e)
    
    finally:
        print("")
            
def Setting(): ## manager setting
    try:
        print("1. CHANGE ROOM NUMBERS ")
        print("2. CHANGE ROOM RATES ")
        print("0. MAIN MENU ")
        r=int(input("->"))
        if r==1:
            print("1.For change room no of STANDARD NON-AC:")
            print("2.For change room no of 3-Bed NON-AC:") 
            print("3.For change room no of 3-Bed AC:") 
            r1=int(input("->"))
            if r1==1:
                rmno=input("Enter the Room number range(101-104 etc): ")
                Global.rmno=str(rmno)
                print("Congrats Room numbers now updated")
                Setting()
            elif r1==2:
                rmno1=input("Enter the Room number range(101-104 etc): ")
                Global.rmno1=str(rmno1)
                print("Congrats Room numbers now updated")
                Setting()
            elif r1==3:
                rmno2=input("Enter the Room number range(101-104 etc): ")
                Global.rmno2=str(rmno2)
                print("Congrats Room numbers now updated")
                Setting()
            else:
                print("OOPS YOU ENTER A WRONG CHOICE TRY AGAIN")
                Setting()
        elif r==2:
            print("1.For change Price for STANDARD NON-AC")
            print("2.For change Price for 3-Bed NON-AC") 
            print("3.For change Price for 3-Bed AC") 
            rr2=int(input("->"))
            if rr2 == 1:
                prm =input("Enter the Price for STANDARD NON-AC")
                Global.prm=prm
                print("Congrats Room Price now updated")
                Setting()
            elif rr2 == 2:
                prm1=input("Enter the Price for 3-Bed NON-AC ")
                Global.prm1=prm1
                print("Congrats Room Price now updated")
                Setting()
            elif rr2 == 3:
                prm2=input("Enter the Price for 3-Bed AC")
                Global.prm2=prm2
                print("Congrats Room Price now updated")
                Setting()
            else:
                print("Enter number between 1 to 3")
        elif r==0:
            loginn()
        else:
            print("OOPS YOU ENTER A WRONG CHOICE TRY AGAIN")
            Setting()
    except ValueError:
            print("Invalid input! Please Enter correct Value format.")
    finally:
            print("")

def setting1(): ## owner settings
    print("1. CHANGE HOTEL NAME")
    print("2. CHANGE ROOM NUMBERS")
    print("3. CHANGE ROOM RATES")
    print("4. CHANGE ADDRESS")
    print("5. CHANGE PHONE NUMBER")
    print("6. CHANGE EMAIL ADDRESS")
    print("0. MAIN MENU ")
    r=int(input("Enter the option to perform task ->"))
    try:
        if r==1:
            h = input("Enter the hotel name to change: ")
            if h.replace(" ", "").isalpha():
                Global.hotel = h.upper()
                print("Congrats Hotel name  now updated")
                setting1()
            else:
                raise ValueError("Please enter a valid name")
                setting1()
        elif r==2:
            print("1.For change room no of STANDARD NON-AC")
            print("2.For change room no of 3-Bed NON-AC") 
            print("3.For change room no of 3-Bed AC") 
            r1=int(input("->"))
            if r1==1:
                rmno=int(input("Enter the Room number range(101-104 etc):"))
                Global.rmno=str(rmno)
                print("Congrats Room numbers now updated")
                setting1()
            elif r1==2:
                rmno1=int(input("Enter the Room number range(101-104 etc): "))
                Global.rmno1=str(rmno1)
                print("Congrats Room numbers now updated")
                setting1()
            elif r1==3:
                rmno2=int(input("Enter the Room number range(101-104 etc): "))
                Global.rmno2=str(rmno2)
                print("Congrats Room numbers now updated")
                setting1()
            else:
                print("OOPS YOU ENTER A WRONG CHOICE TRY AGAIN")
                setting1()
        elif r==3:
            print("1.For change Price for STANDARD NON-AC")
            print("2.For change Price for 3-Bed NON-AC") 
            print("3.For change Price for 3-Bed AC") 
            rr2=int(input("->"))
            if rr2 == 1:
                prm =int(input("Enter the Price for STANDARD NON-AC: "))
                Global.prm=prm
                print("Congrats Room Price now updated")
                setting1()
            elif rr2 == 2:
                prm1=int(input("Enter the Price for 3-Bed NON-AC: "))
                Global.prm1=prm1
                print("Congrats Room Price now updated")
                setting1()
            elif rr2 == 3:
                prm2=int(input("Enter the Price for 3-Bed AC: "))
                Global.prm2=prm2
                print("Congrats Room Price now updated")
                setting1()
            else:
                print("OOPS YOU ENTER A WRONG CHOICE TRY AGAIN")
                setting1()
        elif r==4:
            addr=input("Enter the address to change: ")
            if addr.strip():
                Global.address=addr
                print("Congrats Address now updated")
                setting1()
            else:
                print("OOPS TRY AGAIN YOU MISS SOMETHING>>")
                setting1()
        elif r==5:
            phn=int(input("Enter new number: "))
            Global.phone_numb=phn
            
        elif r==6:
            em = input("Enter the new email: ")
            if em.strip():
                Global.email =em
                print("Congrats email now updated")
                setting1()
            else:
                print("OOPS TRY AGAIN YOU MISS SOMETHING>>")
                setting1() 
        elif r==0:
            login()
        else:
            print("YOU ENTER A WRONG INPUT")
            Home()
    except ValueError:
            print("Invalid input! Please Enter correct Value format.")
            setting1()
    finally:
            print("")
            
def read_me(): ### info about company
    try:
        with open('README.txt', 'r') as file:
            content = file.readlines()
            for line in content:
                print(line.strip()) 
            Home()
    except FileNotFoundError:
        print("README file not found.")
    finally:
        print("")
Home()


# In[ ]:




