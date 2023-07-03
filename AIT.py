from tkinter import ttk
import tkinter as tk
from tkinter import*


a=Tk()
a.title("AIT")
a.geometry("700x700")
a.config(bg="mediumspringgreen")
lbl=Label(a, text="AIT Instititude")
lbl.grid(row=0,column=0)
lbl.config(bg="black",fg="white",height=2,width=30,font=("times",18,"bold"))

def first():
             
             from tkinter import ttk
             import tkinter as tk
             import mysql.connector
             


             mydb=mysql.connector.connect(
                          host='localhost',
                          user='root',
                          password='',
                          database='ait',
             
             )
             '''
             mycursor=mydb.cursor()
             mycursor.execute('select * from addmission')
             myresult=mycursor.fetchall()
             for x in myresult:
                          print(x)
             '''
             
             def saverecord():
                          a=txtId.get()       
                          b=txtFullname.get()
                          c=txtDateofBirth.get()
                          d=txtAddress.get()
                          e=txtContactNo.get()
                          f=txtQualified.get()
                          g=txtCourse.get()
                          h=txtTotalfees.get()
                          i=txtCourseDuration.get()
                          j=txtPaidfees.get()
                          k=txtBalancefees.get()

                          mycursor=mydb.cursor()
                          mycursor.execute("insert into addmission (Id,Fullname,DateofBirth,Address,ContactNo,Qualified,Course,Totalfees,CourseDuration,Paidfees,Balancefees)values("+a+",'"+b+"','"+c+"','"+d+"',"+e+",'"+f+"','"+g+"',"+h+",'"+i+"',"+j+","+k+" )")
                          mydb.commit()
                          print("Record inserted")
#saverecord()

             def Delete():
                          mydb=mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="",
                                       database="ait",
             )
                          mycursor=mydb.cursor()
                          mycursor.execute("Delete from addmission where Id="+txtId.get())
                          mydb.commit()
                          print("Record Deleted")

             def update ():
                          mydb=mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="",
                                       database="ait",
             )
                          mycursor=mydb.cursor()
                          mycursor.execute("update addmission set Fullname='"+txtFullname.get()+"',ContactNo="+txtContactNo.get()+",Balancefees="+txtBalancefees.get()+" where Id="+txtId.get())
                          mydb.commit()
                          print("Record updated")
             

             def view():
                          mydb=mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="",
                                       database="ait"
             )
                          mycursor=mydb.cursor()
                          mycursor.execute("select * from addmission")
                          myresult=mycursor.fetchall()
                          a=tk.Tk()

                          tree=ttk.Treeview(a, column=("C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11"),show="headings")
                          tree.column("#1",anchor=tk.CENTER)
                          tree.heading("#1",text="Id")
                          tree.column("#1",width="50")
                          tree.column("#2",anchor=tk.CENTER)
                          tree.heading("#2",text="Fullname")
                          tree.column("#2",width="50")
                          tree.column("#3",anchor=tk.CENTER)
                          tree.heading("#3",text="DateofBirth")
                          tree.column("#4",anchor=tk.CENTER)
                          tree.heading("#4",text="Address")
                          tree.column("#5",anchor=tk.CENTER)
                          tree.heading("#5",text="ContactNo")
                          tree.column("#6",anchor=tk.CENTER)
                          tree.column("#6",width="50")
                          tree.heading("#6",text="Qualified")
                          tree.column("#6",width="50")
                          tree.column("#7",anchor=tk.CENTER)
                          tree.heading("#7",text="Course")
                          tree.column("#7",width="50")
                          tree.column("#8",anchor=tk.CENTER)
                          tree.heading("#8",text="Totalfees")
                          tree.column("#8",width="50")
                          tree.column("#9",anchor=tk.CENTER)
                          tree.heading("#9",text="CourseDuration")
                          tree.column("#10",anchor = tk.CENTER)
                          tree.heading("#10",text="Paidfees")
                          tree.column("#10",width=40)
                          tree.column("#11",anchor=tk.CENTER)
                          tree.heading("#11",text="Balancefees")
                          tree.pack()
                          
                          for x in myresult:
                                       print(x)
                                       tree.insert("",tk.END, values=x)



             def search():
                           mydb=mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="",
                                       database="ait",
             )
                           mycursor=mydb.cursor()
                           id = txtId.get()
                           sql_select_Query = "select * from addmission where id="+ txtId.get()
                           cursor=mydb.cursor()
                           cursor.execute(sql_select_Query)
                           #get all records
                           records = cursor.fetchall()




                           for row in records :
                                        #print("id=",row[0], )
                                         txtId.insert(0, row[0])
                                         txtFullname.insert(0,row[1])
                                         txtDateofBirth.insert(0,row[2])
                                         txtAddress.insert(0,row[3])
                                         txtContactNo.insert(0,row[4])
                                         txtQualified.insert(0,row[5])
                                         txtCourse.insert(0,row[6])
                                         txtTotalfees.insert(0,row[7])
                                         txtCourseDuration.insert(0,row[8])
                                         txtPaidfees.insert(0,row[9])
                                         txtBalancefees.insert(0,row[10])




             a=Tk()
             a.title("Addmission Data")
             a.geometry("700x700")
             a.config(bg="dimgray")
             lbl=Label(a, text="AIT Instititude")
             lbl.grid(row=0,column=0)
             lbl.config(bg="black",fg="wheat",height=1,width=20,font=("times",16,"bold"))


             c=Label(a, text="Id")
             c.grid(row=1, column=0)
             c.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtId=Entry(a,width=50,bg="burlywood")
             txtId.grid(row=1, column=1)

             d=Label(a, text="Fullname")
             d.grid(row=2, column=0)
             d.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtFullname=Entry(a,width=50,bg="burlywood")
             txtFullname.grid(row=2, column=1)

             e=Label(a, text="DateofBirth")
             e.grid(row=3, column=0)
             e.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtDateofBirth=Entry(a,width=50,bg="burlywood")
             txtDateofBirth.grid(row=3, column=1)

             f=Label(a, text="Address")
             f.grid(row=4, column=0)
             f.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtAddress=Entry(a,width=50,bg="burlywood")
             txtAddress.grid(row=4, column=1)

             g=Label(a, text="ContactNo")
             g.grid(row=5, column=0)
             g.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtContactNo=Entry(a,width=50,bg="burlywood")
             txtContactNo.grid(row=5, column=1)

             h=Label(a, text="Qualified")
             h.grid(row=6, column=0)
             h.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtQualified=Entry(a,width=50,bg="burlywood")
             txtQualified.grid(row=6, column=1)

             i=Label(a, text="Course")
             i.grid(row=7, column=0)
             i.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtCourse=Entry(a,width=50,bg="burlywood")
             txtCourse.grid(row=7, column=1)

             j=Label(a, text="Totalfees")
             j.grid(row=8 , column=0)
             j.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtTotalfees=Entry(a, width=50,bg="burlywood")
             txtTotalfees.grid(row=8, column=1)

             k=Label(a, text="CourseDuration")
             k.grid(row=9, column=0)
             k.config(bg="dimgray",fg="black",height=1,width=15,font=("fimly",12,"bold"))
             txtCourseDuration=Entry(a,width=50,bg="burlywood")
             txtCourseDuration.grid(row=9, column=1)

             l=Label(a, text="Paidfees")
             l.grid(row=10, column=0)
             l.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtPaidfees=Entry(a,width=50,bg="burlywood")
             txtPaidfees.grid(row=10, column=1)

             m=Label(a, text="Balancefees")
             m.grid(row=11, column=0)
             m.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",12,"bold"))
             txtBalancefees=Entry(a,width=50,bg="burlywood")
             txtBalancefees.grid(row=11, column=1)

             k=Button(a, text="Save",command=saverecord, bg="aquamarine", fg="black",height=1,width=12,font=("times",15,"bold"))
             k.grid(column=0,row=25,pady=200)

             o=Button(a, text="Delete",command=Delete, bg="aquamarine",fg="black",height=1,width=12,font=("times",15,"bold"))
             o.grid(column=1,row=25,padx=5)

             p=Button(a, text="Search" ,command=search, bg="aquamarine",fg="black",height=1,width=12,font=("times",15,"bold"))
             p.grid(column=2,row=25,padx=5)

             q=Button(a, text="Update",command=update, bg="aquamarine",fg="black",height=1,width=12,font=("times",15,"bold"))
             q.grid(column=3,row=25,padx=5)

             s=Button(a, text="Display Data",command=view,bg="aquamarine",fg="black",height=1,width=12,font=("times",15,"bold"))
             s.grid(column=4,row=25,padx=5)

             t=Button(a,text="Back",command=a.destroy,bg="aquamarine",fg="black",height=1,width=12,font=("times",15,"bold"),
                      bd=3,relief="raised")
             t.grid(column=5,row=25,padx=5)



def second():
             from tkinter import ttk
             import tkinter as tk
             import mysql.connector

             mydb=mysql.connector.connect(
                          host='localhost',
                          user='root',
                          password='',
                          database='ait',
             )

             def savedata():
                          a=txtId.get()
                          b=txtPaidAmount.get()
                          c=txtPaidDate.get()
                          d=txtPaidType.get()
             
                          mycursor=mydb.cursor()
                          mycursor.execute("insert into fees(Id,PaidAmount,PaidDate,PaidType)values("+a+","+b+",'"+c+"','"+d+"')")
                          mydb.commit()
                          print("completed")

             def Delete():
                         mydb=mysql.connector.connect(
                          host='localhost',
                          user='root',
                          password='',
                          database='ait',
             )
                         mycursor=mydb.cursor()
                         mycursor.execute("delete from fees where Id="+txtId.get())
                         mydb.commit()
                         print("Delete")

             def update():
                          mydb=mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="",
                                       database="ait",
             )
                          mycursor=mydb.cursor()
                          mycursor.execute("update fees set PaidAmount="+txtPaidAmount.get()+", PaidDate='"+txtPaidDate.get()+"',PaidType='"+txtPaidType.get()+"' where Id="+txtId.get())
                          mydb.commit()
                          print("updated")
             

             def search():
                          mydb=mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="",
                                       database="ait",
             )
                          mycursor=mydb.cursor()
                          id = txtId.get()
                          sql_select_Query = "select * from fees where id="+ txtId.get()
                          cursor=mydb.cursor()
                          cursor.execute(sql_select_Query)
                          #get all records
                          records = cursor.fetchall()

                          for row in records :
                          
                                       #print("id=",row[0], )
                                       txtId.insert(0, row[0])
                                       txtPaidAmount.insert(0,row[1])
                                       txtPaidDate.insert(0,row[2])
                                       txtPaidType.insert(0,row[3])


             def show ():
                          mydb=mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="",
                                       database="ait",
             )
             
             def show():
                          mydb=mysql.connector.connect(
                                       host="localhost",
                                       user="root",
                                       password="",
                                       database="ait"
             )
                          mycursor=mydb.cursor()
                          mycursor.execute("SELECT `Id`,`PaidAmount`,`PaidDate`,`PaidType` FROM `fees`")
                          myresult=mycursor.fetchall()
             
                          a=tk.Tk()

                          tree=ttk.Treeview(a,column=("C1","C2","C3","C4"), show="headings")
                          tree.column("#1",anchor=tk.CENTER)
                          tree.heading("#1",text="Id")
                          tree.column("#2",anchor=tk.CENTER)
                          tree.heading("#2",text="PaidAmount")
                          tree.column("#3",anchor=tk.CENTER)
                          tree.heading("#3",text="PaidDate")
                          tree.column("#4",anchor=tk.CENTER)
                          tree.heading("#4",text="PaidType")
                          tree.pack()
             
                          for x in myresult:
                                       print(x)
                                       tree.insert("",tk.END, values=x)
                                       

               
             a=Tk()
             a.title("Fees Data")
             a.geometry("700x700")
             a.config(bg="dimgray")
             lbl=Label(a, text="AIT Instititude")
             lbl.grid(row=0,column=0)
             lbl.config(bg="black",fg="wheat",height=1,width=20,font=("fimly",15,"bold"))

             c=Label(a, text="Id")
             c.grid(row=1, column=0)
             c.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",13,"bold"))
             txtId=Entry(a,width=60,bg="burlywood")
             txtId.grid(row=1, column=1)

             d=Label(a, text="PaidAmount")
             d.grid(row=2, column=0)
             d.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",13,"bold"))
             txtPaidAmount=Entry(a,width=60,bg="burlywood")
             txtPaidAmount.grid(row=2, column=1)


             e=Label(a, text="PaidDate")
             e.grid(row=3, column=0)
             e.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",13,"bold"))
             txtPaidDate=Entry(a,width=60,bg="burlywood")
             txtPaidDate.grid(row=3, column=1)

             f=Label(a, text="PaidType")
             f.grid(row=4, column=0)
             f.config(bg="dimgray",fg="black",height=1,width=10,font=("fimly",13,"bold"))
             txtPaidType=Entry(a,width=60,bg="burlywood")
             txtPaidType.grid(row=4, column=1)


             s=Button(a,text="Save",command=savedata, bg="black",fg="white", height=1,width=12,font=("Times",15,"bold"),
                      bd=3,relief="raised")
             s.grid(column=0,row=20,padx=10,pady=300)

             t=Button(a, text="Delete",command=Delete, bg="black", fg="white",height=1,width=12,font=("Times",15,"bold"),
                      bd=3,relief="raised")
             t.grid(column=1,row=20,padx=10)

             h=Button(a, text="Update",command=update,bg="black",fg="white",height=1,width=12,font=("Times",15,"bold"),
                      bd=3,relief="raised")
             h.grid(column=2, row=20,padx=10)

             i=Button(a, text="Search",command=search,bg="black",fg="white",height=1,width=12,font=("Times",15,"bold"),
                      bd=3,relief="raised")
             i.grid(column=3,row=20,padx=10)

             j=Button(a, text="Display",command=show, bg="black",fg="white",height=1,width=12,font=("Times",15,"bold"),
                      bd=3,relief="raised")
             j.grid(column=4,row=20,padx=10)

             k=Button(a,text="Back",command=a.destroy,bg="black",fg="white",height=1,width=12,font=("times",15,"bold"),
                      bd=3,relief="raised")
             k.grid(column=5,row=20,padx=10)



t=Button(a,text="Addmission",command=first,bg="darkcyan",fg="black",height=2,width=20,font=("times",15,"bold"))
t.grid(column=1,row=20,pady=300,padx=30)

s=Button(a, text="Fees",command=second,bg="darkcyan",fg="black",height=2,width=20,font=("times",15,"bold"))
s.grid(column=2,row=20)


a.mainloop()











