from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="Nandhana9585", database="mypro_t")


def insert(id,name, age,phoneno,address):
    res = con.cursor()
    sql = "insert into stuudent  (id,name,age,phoneno,address) values (%s,%s,%s,%s,%s)"
    user = (id,name, age,phoneno,address)
    res.execute(sql, user)
    con.commit()
    print("Data Insert Success")


def update(name, age, phoneno,address,id):
    res = con.cursor()
    sql = "update stuudent set name=%s,age=%s,phoneno=%s,address=%s where id=%s"
    user = (name, age, phoneno, address,id)
    res.execute(sql, user)
    con.commit()
    print("Data update Success")


def select():
    res = con.cursor()
    sql = "SELECT id,name,age,phoneno,address from stuudent"
    res.execute(sql)
    #result=res.fetchmany(2)
    result = res.fetchall()
    print(tabulate(result,headers=["id","name","age","phoneno","address"]))


def delete(id):
    res = con.cursor()
    sql = "delete from stuudent where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data delete Success")



while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        id= input("Enter idnum : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        phoneno=input("Enter phoneno : ")
        address=input("Enter address : ")
        insert(id,name, age,phoneno,address)
    elif choice == 2:
        id = input("Enter The Id : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        phoneno = input("Enter phoneno : ")
        address = input("Enter address : ")
        update(name, age, phoneno, address,id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter The Id to Delete : ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection . Please Try Again !")