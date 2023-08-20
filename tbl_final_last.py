import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root',database='library',password='password')
cursor=mycon.cursor()

##sf='''CREATE TABLE SCI_FI
##           (BOOK_NAME VARCHAR(50),
##           BOOK_ID VARCHAR(20) PRIMARY KEY,
##           AUTHOR_NAME VARCHAR(20),
##           DESCRIPTION VARCHAR(5000),
##           PRICE INT);'''
##cursor.execute(sf)
##sf= ''' INSERT INTO SCI_FI VALUES
##            ('2001: A Space Odyssey','SF04','Arthur C. Clarke','Two astronauts find their journey into space and their very lives jeopardized by the jealousy of an extraordinary computer named HAL.',550),
##            ('The Time Machine','SF05','H.G. Wells','A British inventor who creates a device that sends him hurtling into the far future where subterranean Morlocks prey upon the childlike Eloi.',550),
##            ('Dune','SF07','Frank Herbert','Set in the distant future, where life revolves around the use and exchange of the spice melange, Dune follows young Paul Atreides, heir of House Atreides, and explores the complex politics, religion, etc among the many factions vying for control of the spice trade.',550),
##            ('1984','SF08','George Orwel','A futuristic society where a totalitarian government watches over all citizens and orchestrates all activities.',550);'''    
##cursor.execute(sf)
##mycon.commit()

##mystery_adv='''CREATE TABLE mystery_adv
##                          (BOOK_NAME VARCHAR(50),
##                          BOOK_ID VARCHAR(20) PRIMARY KEY,
##                          AUTHOR_NAME VARCHAR(20),
##                          DESCRIPTION VARCHAR(5000),
##                          PRICE INT);'''my brother is the sweetest
##cursor.execute(mystery_adv)
##mystery_adv= ''' INSERT INTO mystery_adv VALUES
##                              ('Nancy Drew 2','MA01','Carolyn Keene',"The Hidden Staircase.Nancy Drew relocates to River Heights with her father after her mother's death. Soon, she finds herself investigating a supernatural presence at an old woman's mansion",550),
##                              ("The girl with the dragon tattoo",'MA03','Stieg Larsson','It combines murder mystery, family saga, love story, and financial intrigue into one satisfyingly complex and entertainingly atmospheric novel',550),
##                              ('Nancy Drew 1','MA06',' Carolyn Keene',"The secret of the old clock. Sixteen-year-old Nancy Drew wishes to help the Turners, who are struggling relatives of the recently deceased Josiah Crowley, by finding a missing will that can give them claim to Crowely's estate.",550),
##                              ('Rebecca','MA08','Daphne du Maurier','The unnamed protagonist of the tale becomes the wife of a widowed, wealthy man, Mr. de Winter, and moves into the Manderly, his stately home.The grand house holds the shadow of the first Mrs. de Winter over the new lady, and threatens not just her happiness but her life.',550);'''
##cursor.execute(mystery_adv)
##mycon.commit()

##biopic='''CREATE TABLE BIOPIC
##       (BOOK_NAME VARCHAR(100),
##        BOOK_ID VARCHAR(20) PRIMARY KEY,
##        AUTHOR_NAME VARCHAR(20),
##        DESCRIPTION VARCHAR(5000),
##        PRICE INT);'''
##cursor.execute(biopic)
##biopic='''INSERT INTO BIOPIC VALUES
##       ("A Beautiful Mind","B001","Sylvia Nasar","This biography of esteemed mathematician John Nash was both a finalist for the 1998 Pulitzer Prize and the basis for the award-winning film of the same name.",550),
##       ("Eisenhower in War and Peace","B002","Jean Edward Smith","Korea, kept us (mostly) out of Vietnam, twice prevented the use of nuclear weapons. He was a master of making it all look easy–which is why I think we forget to study him.",550),
##       ("Alan Turing:The Enigma","B003","Andrew Hodges","'Hodges’ 1983 biography of Alan Turing sheds light on the inner workings of this brilliant mathematician, cryptologist, and computer pioneer.",550),
##       ("Alexander Hamilton","B004","Ron Chernow","Ron Chernow’s Alexander Hamilton is not only the inspiration for a hit Broadway musical, but also a work of creative genius itself.",550);'''
##cursor.execute(biopic)
##mycon.commit()

##romance='''CREATE TABLE ROMANCE
##       (BOOK_NAME VARCHAR(100),
##        BOOK_ID VARCHAR(20) PRIMARY KEY,
##        AUTHOR_NAME VARCHAR(20),
##        DESCRIPTION VARCHAR(5000),
##          PRICE INT);'''
##cursor.execute(romance)
##romance='''INSERT INTO ROMANCE VALUES
##       ("Pride and Prejudice","R001","Jane Austen","Pride and Prejudice is an 1813 romantic novel of manners written by Jane Austen. Its humour lies in its honest depiction of manners, education, marriage, and money during the Regency era in Great Britain.",550),
##       ("Jane Eyre","R003","Charlotte Brontë","'Jane Eyre, an orphan and an outcast, accepts a governess position for a young girl in a somewhat mysterious situation with a dark and brooding master, Edward Rochester. ",550),
##       ("Sense and Sensibility","R004","Jane Austen","It shows us two women in love. Marianne Dashwood is impulsive in her love for the charming Willoughby, and Elinor Dashwood is sensible but struggles to conceal her angst with her love for Edward Ferras.",550),
##       ("Flowers from the Storm","R010","Laura Kinsale","The Duke of Jervaulx was brilliant—and dangerous. Considered dissolute, reckless, and extravagant, he was transparently referred to as the 'D of J' in scandal sheets. Maddy knows it is her destiny to help him and her only chance to find the true man behind the wicked facade",550);'''
##cursor.execute(romance)
##mycon.commit()
 
##comedy='''CREATE TABLE COMEDY
##           (BOOK_NAME VARCHAR(500),
##           BOOK_ID VARCHAR(20) PRIMARY KEY,
##           AUTHOR_NAME VARCHAR(20),
##           DESCRIPTION VARCHAR(5000),
##            PRICE INT);'''
##cursor.execute(comedy)
##comedy= ''' INSERT INTO COMEDY VALUES
##            ("Based on a True Story","C006","Norm Macdonald","Stand-up veteran and former Saturday Night Live cast member Norm Macdonald inspires cultish devotion in the US",550),
##            ("A Confederacy of Dunces","C007","John Kennedy Toole","If you can swallow the tragedy of its publication, then A Confederacy of Dunces is a comedic masterpiece whose pages sing with one of the greatest fictional creations in literature. ",550),
##            ("Hyperbole and a Half","C008","Allie Brosh","Brutally honest blogger and web-comic creator Allie Brosh built up a huge following with her witty meditations on depression.",550),
##            ("White Teeth","C010","Zadie Smith" ,"White Teeth’s subtle humour is found in the mundane flaws and absurd fates of two multicultural families as they navigate the complex realities of race, roots and religion in post-war London",550);'''
##cursor.execute(comedy)
##mycon.commit()

##cust_details='''CREATE TABLE CUST_DETAILS
##                (FIRST_NAME VARCHAR(20) ,
##                LAST_NAME VARCHAR(20),
##                EMAIL_ID VARCHAR(70) PRIMARY KEY,
##                PASSWORD VARCHAR(20));'''
##cursor.execute(cust_details)

##cart_details='''CREATE TABLE CART_DETAILS
##                (EMAIL_ID VARCHAR(100) PRIMARY KEY,
##                PHONE_NUMBER varchar(100),
##                RETURN_DATE DATE,
##                ADDRESS VARCHAR(500));'''
##cursor.execute(cart_details)
sql='''TRUNCATE TABLE cart_details;'''
cursor.execute(sql)
mycon.commit()
cart_list=[]

import datetime
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import os
import smtplib
class App:
    def __init__(self,root,*args,**kwargs):
        self.root=root
        self.root.title("The Book Lounge")
        self.root.geometry("1366x700+0+0")
        self.loginform()
       
    def loginform(self):
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)
        self.img=ImageTk.PhotoImage(file="bg_image.jpg")
        img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
        frame_input=Frame(self.root,bg="white")
        frame_input.place(x=320,y=130,height=450,width=350)
        label1=Label(frame_input,text="Login",font=('Algerian',32,'bold',"underline"),fg="black",bg="white")
        label1.place(x=75,y=20)
        label2=Label(frame_input,text="Email id",font=("Comfortaa",20),fg='orangered',bg='white')
        label2.place(x=30,y=95)
        self.email_txt=Entry(frame_input,font=("Comfortaa",15),bg='lightgray')
        self.email_txt.place(x=30,y=145,width=270,height=35)
        label3=Label(frame_input,text="Password",font=("Comfortaa",20),fg='orangered',bg='white')
        label3.place(x=30,y=195)
        self.password=Entry(frame_input,font=("Comfortaa",15),bg="lightgray")
        self.password.place(x=30,y=245,width=270,height=35)
        self.password.config(show="*")
        btn1=Button(frame_input,text="forgot password?",command=self.forgot_password,cursor="hand2",font=("Calibri",10),bg="white",fg='black',bd=0)
        btn1.place(x=125,y=305)
        btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",font=("Comfortaa",15,"bold"),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=90,y=340)
        btn3=Button(frame_input,command=self.Register,text="Not Registered?Register Now",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
        btn3.place(x=110,y=390)
        self.profilemail()

    def login(self):
        if self.email_txt.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                cursor.execute("select * from cust_details where EMAIL_ID=%s and PASSWORD=%s",(self.email_txt.get(),self.password.get()))
                row=cursor.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Username And Password',parent=self.root)
                    self.loginclear()
                    self.email_txt.focus()
                else:
                    self.appscreen()
                    #mycon.close()
            except Exception as es:
                messagebox.showerror('Error',f'Error Due to:{str(es)}',parent=self.root)
                
    def profilemail(self):
        global pmail
        pmail=self.email_txt.get()
        global password
        password=self.password.get()
                        
    def Register(self):
        Frame_login1=Frame(self.root,bg="white")
        Frame_login1.place(x=0,y=0,height=700,width=1366)
        self.img=ImageTk.PhotoImage(file="bg_image.jpg")
        img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)
        frame_input=Frame(self.root,bg="white")
        frame_input2=Frame(self.root,bg="white")
        frame_input2.place(x=320,y=130,height=450,width=630)
        label1=Label(frame_input2,text="Signup Now",font=("Algerian",32,"bold","underline"),fg="black",bg="white")
        label1.place(x=45,y=20)
        label2=Label(frame_input2,text="First Name",font=("Comfortaa",20),fg='orangered',bg='white')
        label2.place(x=30,y=95)
        self.entry=Entry(frame_input2,font=("Comfortaa",15),bg='lightgray')
        self.entry.place(x=30,y=145,width=270,height=35)
        label3=Label(frame_input2,text="Email id**",font=("Comfortaa",20),fg='orangered',bg='white')
        label3.place(x=30,y=195)
        self.entry2=Entry(frame_input2,font=("Comfortaa",15),bg='lightgray')
        self.entry2.place(x=30,y=245,width=270,height=35)
        btn3=Label(frame_input2,text="**Please enter a valid email id ",font=("Calibri",10),fg='red',bg="white",bd=0)
        btn3.place(x=30,y=280)
        label4=Label(frame_input2,text="Last name",font=("Comfortaa",20),fg='orangered',bg='white')
        label4.place(x=330,y=95)
        self.entry3=Entry(frame_input2,font=("Comfortaa",15),bg='lightgray')
        self.entry3.place(x=330,y=145,width=270,height=35)
        label5=Label(frame_input2,text="Password*",font=("Comfortaa",20),fg='orangered',bg='white')
        label5.place(x=330,y=195)
        self.entry4=Entry(frame_input2,font=("Comfortaa",15),bg='lightgray')
        self.entry4.place(x=330,y=245,width=270,height=35)
        self.entry4.config(show="*")
        label6=Label(frame_input2,text="*Should have minimum 8 characters",font=("Calibri",10),fg="red",bg="white")
        label6.place(x=330,y=280)
        btn2=Button(frame_input2,command=self.register,text="Signup",cursor="hand2",font=("Comfortaa",15),fg='white',bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=90,y=340)
        btn3=Button(frame_input2,command=self.loginform,text="Already Registered?Login",cursor="hand2",font=("Calibri",10),fg='black',bg="white",bd=0)
        btn3.place(x=110,y=390)
        
    def register(self):
        if self.entry.get()=="" or self.entry2.get()=="" or self.entry3.get()=="" or self.entry4.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                cursor.execute("select * from cust_details where email_id='%s'",(self.entry2.get()))
                row=cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exists","Please try with a new id",parent=self.root)
                    self.regclear()
                    self.entry.focus()
            
                else:
                    cursor.execute("insert into cust_details values(%s,%s,%s,%s,'-','-')",(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get()))
                    mycon.commit()
                    messagebox.showinfo("Success !! ","Welcome to The Book Lounge.Your account has been created",parent=self.root)
                    self.regclear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)

    def profile(self):
        profileframe=Frame(self.root,bg="lightgoldenrod")
        profileframe.place(x=0,y=0,height=700,width=1366)
        label1=Label(profileframe,text="PROFILE",font=('Algerian',30,'bold',"underline"),fg="black",bg="lightgoldenrod")
        label1.place(x=500,y=20)
        self.profilemail()
        s=pmail
        label2=Label(profileframe,text="LAST NAME:",font=("Comfortaa",20),fg='black',bg='lightgoldenrod')
        label2.place(x=30,y=155)
        self.lastname=Entry(profileframe,font=("Comfortaa",15),bg='lightgray')
        self.lastname.place(x=270,y=155,width=600,height=35)
        label2=Label(profileframe,text="FIRST NAME:",font=("Comfortaa",20),fg='black',bg='lightgoldenrod')
        label2.place(x=30,y=95)
        self.firstname=Entry(profileframe,font=("Comfortaa",15),bg='lightgray')
        self.firstname.place(x=270,y=95,width=600,height=35)
        label3=Label(profileframe,text="PHONE NUMBER:",font=("Comfortaa",20),fg='black',bg='lightgoldenrod')
        label3.place(x=30,y=215)
        self.phonenumber=Entry(profileframe,font=("Comfortaa",15),bg='lightgray')
        self.phonenumber.place(x=270,y=215,width=600,height=35)
        label3=Label(profileframe,text="ADDRESS:",font=("Comfortaa",20),fg='black',bg='lightgoldenrod')
        label3.place(x=30,y=275)
        self.address=Entry(profileframe,font=("Comfortaa",15),bg='lightgray')
        self.address.place(x=270,y=275,width=600,height=35)
        p=password
        label4=Label(profileframe,text="PASSWORD:",font=("Comfortaa",20),fg='black',bg='lightgoldenrod')
        label4.place(x=30,y=335)
        self.password=Entry(profileframe,font=("Comfortaa",15),bg='lightgray')
        self.password.place(x=270,y=335,width=600,height=35)
        self.password.insert(END,p)
        label5=Label(profileframe,text="EMAIL ID:",font=("Comfortaa",20),fg='black',bg='lightgoldenrod')
        label5.place(x=30,y=395)
        self.emailid=Entry(profileframe,font=("Comfortaa",15),bg='lightgray')
        self.emailid.place(x=270,y=395,width=600,height=35)
        self.emailid.insert(END,s)
        btn1=Button(profileframe,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"underline","bold"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=20,y=20)
        btn1=Button(profileframe,text="Update",command=self.update,cursor="hand2",font="Comfortaa",bg="orangered",width=10,fg="black")
        btn1.place(x=30,y=450)
        label5=Label(profileframe,text="NOTE-EMAIL CANNOT BE UPDATED",font=("Comfortaa",10),fg='red',bg='lightgoldenrod')
        label5.place(x=30,y=500)
        self.profiledetailsget()
        
    def profiledetailsget(self):
        cursor.execute("select first_name from cust_details where EMAIL_ID=%s and PASSWORD=%s",(self.emailid.get(),self.password.get()))
        row=cursor.fetchone()
        for i in row:
            self.firstname.insert(END,i)
        cursor.execute("select last_name from cust_details where EMAIL_ID=%s and PASSWORD=%s",(self.emailid.get(),self.password.get()))
        row=cursor.fetchone()
        for i in row:
            self.lastname.insert(END,i)
        cursor.execute("select phone_number from cust_details where EMAIL_ID=%s and PASSWORD=%s",(self.emailid.get(),self.password.get()))
        row=cursor.fetchone()
        for i in row:
            self.phonenumber.insert(END,i)
        cursor.execute("select ADDRESS from cust_details where EMAIL_ID=%s and PASSWORD=%s",(self.emailid.get(),self.password.get()))
        row=cursor.fetchone()
        for i in row:
            self.address.insert(END,i)
            
    def update(self):
        cursor.execute("UPDATE CUST_DETAILS SET FIRST_NAME=%s,LAST_NAME=%s,PASSWORD=%s,PHONE_NUMBER=%s,ADDRESS=%s where EMAIL_ID=%s",(
        self.firstname.get(),
        self.lastname.get(),
        self.password.get(),
        self.phonenumber.get(),
        self.address.get(),
        self.emailid.get()))
        mycon.commit()
        messagebox.showinfo("Success !! ","Your account details have been updated",parent=self.root)
                
    def appscreen(self):
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1366)
        Frame_login.configure(background="lightgoldenrod")
        label1=Label(Frame_login,text='***Welcome to the Book Lounge***',fg='black',bg='lightgoldenrod',font=("Algerian",30,"underline"))
        label1.place(x=375,y=50)         
        mycon=mysql.connector.connect(host='localhost',user='root',database='library',password='password')
        cursor=mycon.cursor()
        label2=Label(text='Science fiction',fg='black',bg='lightgoldenrod',font=("Calibri",25))
        label2.place(x=75,y=120)
        sql="SELECT * FROM sci_fi"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frm=Frame(root)
        frm.place(x=75,y=170)
        tv=ttk.Treeview(frm,columns=(1,),show="headings",height="7")
        tv.pack()
        tv.heading(1,text="Book Name")
        for i in rows:
            tv.insert('','end',values=i)
            btn2=Button(command=self.sc,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn2.place(x=240,y=197)
            btn3=Button(command=self.sc1,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=240,y=217)
            btn3=Button(command=self.sc2,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=240,y=237)
            btn3=Button(command=self.sc3,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=240,y=256)                
        label3=Label(Frame_login,text='Mystery & adventure',fg='black',bg='lightgoldenrod',font=("Calibri",25))
        label3.place(x=475,y=120)
        sql="SELECT * FROM mystery_adv"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frm=Frame(root)
        frm.place(x=475,y=170)
        tv=ttk.Treeview(frm,columns=(1,),show="headings",height="7")
        tv.pack()
        tv.heading(1,text="Book Name")
        for i in rows:
            tv.insert('','end',values=i)
            btn2=Button(command=self.ma,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn2.place(x=650,y=197)
            btn3=Button(command=self.ma1,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=650,y=217)
            btn3=Button(command=self.ma2,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=650,y=237)
            btn3=Button(command=self.ma3,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=650,y=256)                       
        label4=Label(Frame_login,text='Romance',fg='black',bg='lightgoldenrod',font=("Calibri",25))
        label4.place(x=875,y=120)
        sql="SELECT * FROM romance"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frm=Frame(root)
        frm.place(x=875,y=170)
        tv=ttk.Treeview(frm,columns=(1,),show="headings",height="7")
        tv.pack()
        tv.heading(1,text="Book Name")
        for i in rows:
            tv.insert('','end',values=i)
            btn2=Button(command=self.ro,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn2.place(x=1050,y=197)
            btn3=Button(command=self.ro1,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=1050,y=217)
            btn3=Button(command=self.ro2,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=1050,y=237)
            btn3=Button(command=self.ro3,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=1050,y=256)            
        label5=Label(Frame_login,text='Biopic',fg='black',bg='lightgoldenrod',font=("Calibri",25))
        label5.place(x=275,y=400)
        sql="SELECT * FROM biopic"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frm=Frame(root)
        frm.place(x=275,y=450)
        tv=ttk.Treeview(frm,columns=(1,),show="headings",height="7")
        tv.pack()
        tv.heading(1,text="Book Name")
        for i in rows:
            tv.insert('','end',values=i)
            btn2=Button(command=self.bi,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn2.place(x=450,y=480)
            btn3=Button(command=self.bi1,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=450,y=500)
            btn3=Button(command=self.bi2,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=450,y=520)
            btn3=Button(command=self.bi3,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=450,y=540)                        
        label6=Label(Frame_login,text='Comedy',fg='black',bg='lightgoldenrod',font=("Calibri",25))
        label6.place(x=775,y=400)
        sql="SELECT * FROM comedy"
        cursor.execute(sql)
        rows=cursor.fetchall()
        frm=Frame(root)
        frm.place(x=775,y=450)
        tv=ttk.Treeview(frm,columns=(1,),show="headings",height="7")
        tv.pack()
        tv.heading(1,text="Book Name")
        for i in rows:
            tv.insert('','end',values=i)
            btn2=Button(command=self.co,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn2.place(x=930,y=480)
            btn3=Button(command=self.co1,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=930,y=500)
            btn3=Button(command=self.co2,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=930,y=520)
            btn3=Button(command=self.co3,text="View",cursor="hand2",font=("Comfortaa",6),fg='red',bg="white",bd=0)
            btn3.place(x=930,y=540)
        profilebtn=Button(Frame_login,text="Profile",command=self.profile,cursor="hand2",font=("Comfortaa",13),fg="white",bg="orangered",bd=0,width=10,height=1)
        profilebtn.place(x=800,y=10)
        btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",font=("Comfortaa",13),fg="white",bg="orangered",bd=0,width=10,height=1)
        btn2.place(x=900,y=10)
        cartbtn=Button(Frame_login,text='Cart',command=self.Cart,bg='orangered',font=("Comfortaa",13),fg="white",bd=0,width=10,height=1)
        cartbtn.place(x=1000,y=10)
        searchbtn=Button(Frame_login,text='Search',command=self.Search,bg='orangered',font=("Comfortaa",13),fg="white",bd=0,width=10,height=1)
        searchbtn.place(x=1100,y=10)


    
    def deliveryCart(self):
        ask=messagebox.askyesno('Confirmation','Do you want to proceed to checkout')
        if ask:
            cartframe=Frame(self.root,bg="lightgoldenrod")
            cartframe.place(x=0,y=0,height=700,width=1366)
            label1=Label(cartframe,text="Delivery details",font=('Algerian',30,'bold',"underline"),fg="black",bg="lightgoldenrod")
            label1.place(x=500,y=20)
            label2=Label(cartframe,text="Email Address",font=("Comfortaa",25),fg='black',bg='lightgoldenrod')
            label2.place(x=30,y=95)
            self.emailaddress=Entry(cartframe,font=("Comfortaa",15),bg='lightgray')
            self.emailaddress.place(x=30,y=145,width=670,height=35)
            label3=Label(cartframe,text="Phone number",font=("Comfortaa",25),fg='black',bg='lightgoldenrod')
            label3.place(x=30,y=195)
            self.phone_number=Entry(cartframe,font=("Comfortaa",15),bg="lightgray")
            self.phone_number.place(x=30,y=245,width=670,height=35)
            label4=Label(cartframe,text="Return date(yyyy-mm-dd)",font=("Comfortaa",25),fg='black',bg='lightgoldenrod')
            label4.place(x=30,y=295)
            self.return_date=Entry(cartframe,font=("Comfortaa",15),bg="lightgray")
            self.return_date.place(x=30,y=345,width=670,height=35)
            label5=Label(cartframe,text="Delivery Address",font=("Comfortaa",25),fg='black',bg='lightgoldenrod')
            label5.place(x=30,y=395)
            self.delivery_details=Entry(cartframe,font=("Comfortaa",15),bg="lightgray")
            self.delivery_details.place(x=30,y=445,width=670,height=35)
            btn1=Button(cartframe,text="Back",command=self.Cart,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
            btn1.place(x=10,y=30)
            btn3=Label(cartframe,text="Payment method:Cash on delivery",font=("Comfortaa",20),fg="black",bg="lightgoldenrod",bd=0)
            btn3.place(x=30,y=490)
            btn2=Button(cartframe,text="Proceed with payment",command=self.cart,cursor="hand2",font=("Comfortaa",15),fg='black',bg="orangered",bd=0,width=30,height=1)
            btn2.place(x=30,y=550)
            self.details()
        else:
            print()
        
    def Cart(self):
        global t
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
##        ask=messagebox.askyesno('Confirmation','Do you want to proceed to cart?') 
##        if ask:              
        cartfinalFrame=Frame(self.root,bg="lightgoldenrod")
        cartfinalFrame.place(x=0,y=0,height=700,width=1366)
        label1=Label(cartfinalFrame,text=Spaces(60)+'CART'+Spaces(60),font=('Algerian',20,'bold',"underline"),fg="black",bg="lightgoldenrod")
        label1.place(x=85,y=50)
        label1=Label(cartfinalFrame,text="Book Name"+Spaces(50)+"Quantity"+Spaces(45),font=('Algerian',20,'bold',"underline"),fg="black",bg="lightgoldenrod")
        label1.place(x=70,y=95)
        profilebtn=Button(cartfinalFrame,text="Refresh",command=self.adminpage,cursor="hand2",font=("Comfortaa",13),fg="white",bg="orangered",bd=0,width=10,height=1)
        profilebtn.place(x=90,y=20)
        t=40
        for i in cart_list:
            def add():
                i[4]+=1
                messagebox.showinfo('','Quantity of the book has been increased')
                self.Cart()
            def subtract():
                i[4]-=1
                messagebox.showinfo('','Quantity of the book has been decreased or deleted')
                self.Cart()
            if i[4]>0:
                t+=40
                label=Label(cartfinalFrame,text=i[0]+Spaces(60)+str(i[4])+Spaces(10),font=("Comfortaa",20),fg="black",bg="lightgoldenrod")
                label.place(x=70,y=105+t)
                btnadd=Button(cartfinalFrame,text="+",command=add,cursor="hand2",font=("Calibri",15),fg='black',bg="orangered",bd=3)
                btnadd.place(x=1000,y=105+t)
                btnsubtract=Button(cartfinalFrame,text="-",command=subtract,cursor="hand2",font=("Calibri",15),fg='black',bg="orangered",bd=3)
                btnsubtract.place(x=1050,y=105+t)
                
            else:
                print()

        btn2=Button(cartfinalFrame,text="Continue",command=self.deliveryCart,cursor="hand2",font=("Comfortaa",15),fg='black',bg="orangered",width=20,height=1)
        btn2.place(x=1000,y=495)
        btn1=Button(cartfinalFrame,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=30,y=20)
##        else:
##            self.appscreen()
    def adminpage(self):
        self.Cart()
            
    def details(self):
        global address
        global phonenumber
        global emailidcart
        global returndate
        emailidcart=self.emailaddress.get()
        phonenumber=self.phone_number.get()
        returndate=self.return_date.get()
        address=self.delivery_details.get()
        
    def cart(self):
        if self.emailaddress.get()=="" or self.phone_number.get()=="" or self.return_date.get()=="" or self.delivery_details.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            cursor.execute("insert into cart_details values(%s,%s,%s,%s)",(self.emailaddress.get(),self.phone_number.get(),self.return_date.get(),self.delivery_details.get()))
            mycon.commit()
            billframe=Frame(self.root,bg="grey75")
            billframe.place(x=0,y=0,height=700,width=1366)
            self.billgen()
            self.pmailget()
            
    def pmailget(self):
        global pmail
        pmail=self.emailaddress.get()
        
    def billgen(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        book_price=0
        for i in range(len(cart_list)):
            book_price+=cart_list[i][1]
        billframe=Frame(self.root,bg="gray76")
        billframe.place(x=0,y=0,height=700,width=1366)
        bill_title=Label(billframe,text="BILL",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
        bill_txt_area=Text(billframe)
        bill_txt_area.pack(fill=BOTH,expand=1)
        bill_txt_area.insert(END,Spaces(75)+"THE BOOK LOUNGE\n"+Spaces(170,'*')+"\n")
        if len(cart_list)>0:
                bill_txt_area.insert(END,"Book(s)\n\nBook Name"+Spaces(42)+"Price"+Spaces(25)+"Quantity\n")
                for i in cart_list:
                    if i[4]>0:
                        bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+str(i[4])+"\n")
                bill_txt_area.insert(END,"\nTotal Book Price : Rs."+str(book_price)+"\n"+Spaces(170,'*')+"\n")
        bill_txt_area.insert(END,'DELIVERY DETAILS\n')
        self.details()
        bill_txt_area.insert(END,'Delivery Address:'+Spaces(46)+address+'\n')
        bill_txt_area.insert(END,'Return Date:'+Spaces(51)+returndate+'\n')
        bill_txt_area.insert(END,'Phone Number:'+Spaces(50)+phonenumber+'\n')
        bill_txt_area.insert(END,'Email for confirmation:'+Spaces(40)+emailidcart+'\n')
        bill_txt_area.insert(END,Spaces(170,'*'))
        try:
            sender_email="thebooklounge2K21@gmail.com"
            self.details()
            rec_email=emailidcart
            password="TBL_MNA_BGS"
            message = 'Subject: {}\n\n{}'.format("Order Confirmation",'Dear Customer,\nYour order has been confirmed and it will be shipped soon.Hope you enjoyed your experience at THE BOOK LOUNGE.We hope to see you soon')
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender_email,password)
            server.sendmail(sender_email,rec_email,message)
        except:
            messagebox.showerror("Error","Email invalid",parent=self.root)
            self.appscreen()
        save_button=Button(root,text="Save Invoice",font="times",bd=6,bg="grey66",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
        save_button.place(x=1120,y=600)

        def save_invoice(text):
            op=messagebox.askyesno("Invoice Saving Confirmation","Do you want to save the invoice in a file?")
            if op:
                t=datetime.datetime.now()
                s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
                f=open("Invoice"+s+".txt","w")
                f.write(text)
                f.close()
                messagebox.showinfo("Invoice Saving Status","Invoice is saved successfully as a text document with name "+s+".txt")
            else:
                messagebox.showinfo("Invoice Saving Status","The invoice is not saved into a file.")
                
    def Search(self):
        Frame_search=Frame(self.root,bg="lightgoldenrod")
        Frame_search.place(x=0,y=0,height=700,width=1366)
        self.img=ImageTk.PhotoImage(file="lavendersearch.png")
        img=Label(Frame_search,image=self.img).place(x=200,y=100,width=300,height=300)
        btn1=Button(Frame_search,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),bg="lightgoldenrod",fg='red',bd=0)
        btn1.place(x=20,y=30)
        label1=Label(Frame_search,text="Search",font=('Algerian',30,'bold',"underline"),fg="black",bg="lightgoldenrod")
        label1.place(x=800,y=50)
        label2=Label(Frame_search,text="Book Name",font=("Calibri",20),fg="black",bg="lightgoldenrod")
        label2.place(x=700,y=120)
        self.bookentry=Entry(Frame_search,font=("Comfortaa",18),bg='lightgray')
        self.bookentry.place(x=700,y=175,width=350,height=35)
        btnbooksearch=Button(Frame_search,text="search",command=self.booksearch,font=("Calibri",15),relief='raised',activebackground="lavender",bg="lightgoldenrod",fg='black',width=10,height=1)
        btnbooksearch.place(x=1100,y=175)
        label3=Label(Frame_search,text="Author's Name",font=("Calibri",25),fg="black",bg="lightgoldenrod")
        label3.place(x=700,y=250)
        self.authorentry=Entry(Frame_search,font=("Comfortaa",15),bg='lightgray')
        self.authorentry.place(x=700,y=305,width=350,height=35)
        btnauthorsearch=Button(Frame_search,text="search",command=self.authorsearch,font=("Calibri",15),relief='raised',activebackground="lavender",bg="lightgoldenrod",fg='black',width=10,height=1)
        btnauthorsearch.place(x=1100,y=305)
        label4=Label(Frame_search,text="*NOTE*                                                                         ",font=('Comfortaa',20,'bold',"italic"),fg="red",bg="lightgoldenrod")
        label4.place(x=50,y=460)
        label4=Label(Frame_search,text="The book names and the authors' names should be capitalised               ",font=('Calibri',16),fg="red",bg="lightgoldenrod")
        label4.place(x=50,y=500)
        label4=Label(Frame_search,text="Prefixes like 'Dr.' and 'Prof.' should not included in the name                    ",font=('Calibri',16),fg="red",bg="lightgoldenrod")
        label4.place(x=50,y=530)
        
    def booksearch(self):
        if self.bookentry.get()=="2001:A SPACE ODYSSEY" or self.bookentry.get() in "2001:A SPACE ODYSSEY":
            self.sc()
        elif self.bookentry.get()=="THE TIME MACHINE" or self.bookentry.get() in "TIME MACHINE":
            self.sc1()
        elif self.bookentry.get()=="DUNE":
            self.sc2()
        elif self.bookentry.get()=='1984':
            self.sc3()
        elif self.bookentry.get()=='NANCY DREW:THE HIDDEN STAIRCASE' or self.bookentry.get() in 'THE HIDDEN STAIRCASE':
            self.ma()
        elif self.bookentry.get()=='NANCY DREW':
            asknancy=messagebox.askyesno('Confirmation','the book you are searching for has two parts, would you like to search for PART I')
            if asknancy:
                self.ma()
            else:
                ask2=messagebox.askyesno('Confirmation','Are you looking for PART II?')
                if ask2:
                    self.ma2()
                else:
                    print()
        elif self.bookentry.get()=="THE GIRL WITH DRAGON TATTOO" or self.bookentry.get() in 'THE GIRL WITH DRAGON TATTOO':
            self.ma1()
        elif self.bookentry.get()=="NANCY DREW:THE SECRET OF THE OLD CLOCK" or self.bookentry.get() in 'SECRET OF THE OLD CLOCK':
            self.ma2()
        elif self.bookentry.get()=="REBECCA":
            self.ma3()
        elif self.bookentry.get()=="PRIDE AND PREJUDICE" or self.bookentry.get() in 'PRIDE AND PREJUDICE':
            self.ro()
        elif self.bookentry.get()=="JANE EYRE" or self.bookentry.get() in "JANE EYRE":
            self.ro1()
        elif self.bookentry.get()=="SENSE AND SENSIBILITY" or self.bookentry.get() in "SENSE AND SENSIBILITY":
            self.ro2()
        elif self.bookentry.get()=="FLOWERS FROM THE STORM" or self.bookentry.get() in "FLOWERS FROM THE STORM":
            self.ro3()
        elif self.bookentry.get()=="A BEAUTIFUL MIND" or self.bookentry.get() in "A BEAUTIFUL MIND":
            self.bi()
        elif self.bookentry.get()=="EISENHOWER IN WAR AND PEACE" or self.bookentry.get() in "EISENHOWER IN WAR AND PEACE":
            self.bi1()
        elif self.bookentry.get()=="ALAN TURING:THE ENIGMA" or self.bookentry.get() in "ALAN TURING:THE ENIGMA":
            self.bi2()
        elif self.bookentry.get()=="ALEXANDER HAMILTON" or self.bookentry.get() in "ALEXANDER HAMILTON":
            self.bi3()
        elif self.bookentry.get()=="BASED ON A TRUE STORY" or self.bookentry.get() in "BASED ON A TRUE STORY":
            self.co()
        elif self.bookentry.get()=="A CONFEDERACY OF DUNCES" or self.bookentry.get() in "A CONFEDERACY OF DUNCES":
            self.co1()
        elif self.bookentry.get()=="HYPERBOLE AND A HALF" or self.bookentry.get() in "HYPERBOLE AND A HALF":
            self.co2()
        elif self.bookentry.get()=="WHITE TEETH" or self.bookentry.get() in "WHITE TEETH":
            self.co3()
        else:
            messagebox.showerror("Error",'Book not found',parent=self.root)
            
    def authorsearch(self):
        if self.authorentry.get()=='ARTHUR.C.CLARKE' or self.authorentry.get() in 'ARTHUR.C.CLARKE':
            self.sc()
        elif self.authorentry.get()=='H.G.WELLS' or self.authorentry.get() in 'H.G.WELLS':
            self.sc1()
        elif self.authorentry.get()=='FRANK HERBERT' or self.authorentry.get() in 'FRANK HERBERT':
            self.sc2()
        elif self.authorentry.get()=='GEORGE ORWELL' or self.authorentry.get() in 'GEORGE ORWELL':
            self.sc3()
        elif self.authorentry.get()=='CAROLYN KEENE' or self.authorentry.get() in 'CAROLYN KEENE':
            asknancy=messagebox.askyesno('Confirmation','THE BOOK LOUNGE has two books written by this author,would you want to search PART I')
            if asknancy:
                self.ma()
            else:
                askii=messagebox.askyesno('Confirmation', 'Are you looking for PART II?')
                if askii:
                    self.ma2()
                else:
                    print()
        elif self.authorentry.get()=='STEIG LARSSON' or self.authorentry.get() in 'STEIG LARSSON':
            self.ma1()
        elif self.authorentry.get()=='DAPHNE DU MAURIER' or self.authorentry.get() in 'DAPHNE DU MAURIER':
            self.ma3()
        elif self.authorentry.get()=='JANE AUSTEN' or self.authorentry.get() in 'JANE AUSTEN':
            askjane=messagebox.askyesno('Confirmation','THE BOOK LOUNGE has two books written by this author,would you want to search PRIDE AND PREJUDICE ?')
            if askjane:
                self.ro()
            else:
                aski=messagebox.askyesno('Confirmation', 'Are you looking for SENSE AND SENSIBILITY?')
                if aski:
                    self.ro2()
                else:
                    messagebox.showerror("error",'No other book found by this author',parent=self.root)
        elif self.authorentry.get()=='CHARLOTTE BRONTE' or self.authorentry.get() in 'CHARLOTTE BRONTE':
            self.ro1()
        elif self.authorentry.get()=='LAURA KINASALE' or self.authorentry.get() in 'LAURA KINASALE':
            self.ro3()
        elif self.authorentry.get()=='SYLVIA NASAR' or self.authorentry.get() in 'SYLVIA NASAR':
            self.bi()
        elif self.authorentry.get()=='JEAN EDWARD SMITH' or self.authorentry.get() in 'JEAN EDWARD':
            self.bi1()
        elif self.authorentry.get()=='LAURA KINASALE' or self.authorentry.get() in 'LAURA KINASALE':
            self.bi2()
        elif self.authorentry.get()=='ANDREW HODGES' or self.authorentry.get() in 'ANDREW HODGES':
            self.bi3()
        elif self.authorentry.get()=='NORM MACDONALD' or self.authorentry.get() in 'NORM MACDONALD':
            self.co()
        elif self.authorentry.get()=='JOHN KENNEDY TOOLE' or self.authorentry.get() in 'JOHN KENNEDY TOOLE':
            self.co1()
        elif self.authorentry.get()=='ALLIE BROSH' or self.authorentry.get() in 'ALLIE BROSH':
            self.co2()
        elif self.authorentry.get()=='ZADIE SMITH' or self.authorentry.get() in 'ZADIE':
            self.co3()
        elif self.authorentry.get()=='SMITH':
            asksmith=messagebox.askyesno('Confirmation','THE BOOK LOUNGE has two authors by this name,are you looking for JEAN EDWARD SMITH?')
            if asksmith:
                self.bi1()
            else:
                aski=messagebox.askyesno('Confirmation', 'Are you looking for author named ZADIE SMITH')
                if aski:
                    self.co3()
                else:
                    messagebox.showerror("Error",'No other author found',parent=self.root)
        else:
            messagebox.showerror("Error",'No author found',parent=self.root)
    cart_list=[]

    def sc(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="2001 A Space Odyssey",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Arthur.C.Clarke",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Two astronauts find their journey into space and their very lives jeopardized by the jealousy of an extraordinary computer named HAL.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=280)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addsc1,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="2001 A SPACE ODYSSEY.jpg")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)
        
    def sc1(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="The Time Machine",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY H.G. Wells",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="A British inventor who creates a device that sends him hurtling into the far future where subterranean Morlocks prey upon the childlike Eloi.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=290)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addsc2,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="THE TIME MACHINE.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def sc2(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Dune",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Frank Herbert",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Set in the distant future, where life revolves around the use and exchange of the spice melange, Dune follows young Paul Atreides, heir of House Atreides, and explores the complex politics, religion, etc among the many factions vying for control of the spice trade.",fg="black",bg="white",font=("Calibri",15),aspect=600)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=320)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addsc3,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="DUNE.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def sc3(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="1984",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="By George Orwell",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="A futuristic society where a totalitarian government watches over all citizens and orchestrates all activities.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=280)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='white')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addsc4,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="1984.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)
        
    def addsc1(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['2001 A Space Odyssey',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('2001 A Space Odyssey')),int(self.quantity.get())])
            messagebox.showinfo('Product status','2001 A Space Odyssey has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','2001 A Space Odyssey has not been added to cart')
            
    def addsc2(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['The Time Machine',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('The Time Machine')),int(self.quantity.get())])
            messagebox.showinfo('Product status','The Time Machine has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','The Time Machine has not been added to cart')
            
    def addsc3(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Dune',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Dune')),int(self.quantity.get())])
            messagebox.showinfo('Product status','Dune has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','Dune has not been added to cart')
            
    def addsc4(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['1984',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('1984')),int(self.quantity.get())])
            messagebox.showinfo('Product status','1984 has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','1984 has not been added to cart')

    def ma(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Nancy Drew :The hidden staircase",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Carolyn Keene",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Nancy Drew relocates to River Heights with her father after her mother's death. Soon, she finds herself investigating a supernatural presence at an old woman's mansion.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=290)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addma,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="NANCY DREW AND THE HIDDEN STAIRCASE.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)
        
    def ma1(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="The girl with the dragon tattoo",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Stieg Larsson",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="It combines murder mystery, family saga, love story, and financial intrigue into one satisfyingly complex and entertainingly atmospheric novel.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=290)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addma1,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="The girl with the dragon tattoo.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def ma2(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Nancy Drew:The secret of the old clock",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Carolyn Keene",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Sixteen-year-old Nancy Drew wishes to help the Turners, who are struggling relatives of the recently deceased Josiah Crowley, by finding a missing will that can give them claim to Crowely's estate.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=290)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addma2,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="NANCY DREW AND THE SECRET OF THE OLD CLOCK.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def ma3(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Rebecca",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Daphne du Maurier",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="The unnamed protagonist of the tale becomes the wife of a widowed, wealthy man, Mr. de Winter, and moves into the Manderly, his stately home.The grand house holds the shadow of the first Mrs. de Winter over the new lady, and threatens not just her happiness but her life. ",fg="black",bg="white",font=("Calibri",15),aspect=600)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addma3,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="REBECCA.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)
        
    def addma(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Nancy Drew :The hidden staircase',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Nancy Drew:The hidden staircase')),int(self.quantity.get())])
            messagebox.showinfo('Product status','Nancy Drew :The hidden staircase has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','Nancy Drew :The hidden staircase has not been added to cart')
            
    def addma1(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['The girl with the dragon tattoo',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('The girl with the dragon tattoo')),int(self.quantity.get())])
            messagebox.showinfo('product status','The girl with the dragon tattoo has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('product status','The girl with the dragon tattoo has not been added to cart')
            
    def addma2(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Nancy Drew(II)',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Nancy Drew(II)')),int(self.quantity.get())])
            messagebox.showinfo('Product status','Nancy Drew(II) has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','Nancy Drew:The secret of the old clock has not been added to cart')
            
    def addma3(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Rebecca',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Rebecca')),int(self.quantity.get())])
            messagebox.showinfo('product status','Rebecca has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('product status','Rebecca has not been added to cart')

    def ro(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Pride and Prejudice",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Jane Austen",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Pride and Prejudice is an 1813 romantic novel of manners written by Jane Austen. Its humour lies in its honest depiction of manners, education, marriage, and money during the Regency era in Great Britain.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addro,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="PRIDE AND PREJUDICE.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def ro1(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Jane Eyre",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Charlotte Brontë",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Jane Eyre, an orphan and an outcast, accepts a governess position for a young girl in a somewhat mysterious situation with a dark and brooding master, Edward Rochester.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addro1,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="JANE EYRE.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def ro2(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Sense and Sensibility",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Jane Austen",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="It shows us two women in love. Marianne Dashwood is impulsive in her love for the charming Willoughby, and Elinor Dashwood is sensible but struggles to conceal her angst with her love for Edward Ferras.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addro2,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="SENSE AND SENSIBILITY.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def ro3(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text=" Flowers from the Storm ",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Laura Kinsale",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="The Duke of Jervaulx was brilliant—and dangerous. Considered dissolute, reckless, and extravagant, he was transparently referred to as the 'D of J' in scandal sheets. Maddy knows it is her destiny to help him and her only chance to find the true man behind the wicked facade.",fg="black",bg="white",font=("Calibri",15),aspect=600)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addro3,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="FLOWERS FROM STORM.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def addro(self):
         def Spaces(n,s1=" "):
             s=""
             for i in range(n):
                 s+=s1
             return s
         global cart_list
         op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
         if op:
             cart_list.append(['Pride and Prejudice',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Pride and Prejudice')),int(self.quantity.get())])
             messagebox.showinfo('product status','Pride and Prejudice has been succesfully added to cart')
             self.appscreen()
         else:
             messagebox.showinfo('product status','Pride and Prejudice has not been added to cart')
    
    def addro1(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Jane Eyre',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Jane Eyre')),int(self.quantity.get())])
            messagebox.showinfo('product status','Jane Eyre hs been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('product status','Jane Eyre has not been added to cart')
            
    def addro2(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Sense and Sensibility',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Sense and Sensibility')),int(self.quantity.get())])
            messagebox.showinfo('product status','Sense and Sensibility has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('product status','Sense and Sensibility has not been added to cart')
            
    def addro3(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Flowers from the Storm',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Flowers from the Storm')),int(self.quantity.get())])
            messagebox.showinfo('product status','Flowers from the Storm has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('product status','Flowers from the Storm has not been added to cart')
            
    def bi(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text=" A Beautiful Mind",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Sylvia Nasar",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="This biography of esteemed mathematician John Nash was both a finalist for the 1998 Pulitzer Prize and the basis for the award-winning film of the same name.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Callibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addbi,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="A BEAUTIFUL MIND.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)
    
    def bi1(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Eisenhower in War and Peace",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Jean Edward Smith",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="He won WWII, ended Korea, kept us (mostly) out of Vietnam, twice prevented the use of nuclear weapons. He was a master of making it all look easy–which is why I think we forget to study him",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addbi1,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="EISENHOWER IN WAR AND PEACE.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def bi2(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Alan Turing: The Enigma",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Andrew Hodges",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Hodges’ 1983 biography of Alan Turing sheds light on the inner workings of this brilliant mathematician, cryptologist, and computer pioneer.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addbi2,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="ALAN TURNING_THE ENIGMA.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def bi3(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Alexander Hamilton",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Ron Chernow",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Ron Chernow’s Alexander Hamilton is not only the inspiration for a hit Broadway musical, but also a work of creative genius itself.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addbi3,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="ALEXANDER HAMILTON.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)
        
    def addbi(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['A Beautiful Mind',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('A Beautiful Mind')),int(self.quantity.get())])
            messagebox.showinfo('Product status','A Beautiful Mind has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','A Beautiful Mind has not been added to cart')

    def addbi1(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Eisenhower in War and Peace',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Eisenhower in War and Peace')),int(self.quantity.get())])
            messagebox.showinfo('Product status','Eisenhower in War and Peace has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','Eisenhower in War and Peace has not been added to cart')
            
    def addbi2(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Alan Turing:The Enigma',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Alan Turing:The Enigma')),int(self.quantity.get())])
            messagebox.showinfo('Product status','Alan Turing: The Enigma has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','Alan Turing:The Enigma has not been added to cart')
            
    def addbi3(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Alexander Hamilton',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Alexander Hamilton')),int(self.quantity.get())])
            messagebox.showinfo('Product status','Alexander Hamilton has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','Alexander Hamilton has not been added to cart')

    def co(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Based on a True Story",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Norm Macdonald",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Stand-up veteran and former Saturday Night Live cast member Norm Macdonald inspires cultish devotion in the US",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addco,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="BASED ON A TRUE STORY.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)
        
    def co1(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="A Confederacy of Dunces",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY John Kennedy Toole",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="If you can swallow the tragedy of its publication, then A Confederacy of Dunces is a comedic masterpiece whose pages sing with one of the greatest fictional creations in literature. ",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addco1,cursor="hand2",font=("Comfortaa",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="A CONFEDERACY OF DUNCES.jpg")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)

    def co2(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="Hyperbole and a Half",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY Allie Brosh",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="Brutally honest blogger and web-comic creator Allie Brosh built up a huge following with her witty meditations on depression.",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addco2,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="HYPERBOLE AND A HALF.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)
        
    def co3(self):
        f3=Frame(self.root,bg="white")
        f3.place(x=0,y=0,height=700,width=1366)
        f3.configure(background="lightgoldenrod")
        l1=Label(f3,text="White Teeth",fg="black",bg="lightgoldenrod",font=("Algerian",20))
        l1.place(x=650,y=100)
        label2=Label(f3,text="BY  Zadie Smith",fg="black",bg="lightgoldenrod",font=("Calibri",15))
        label2.place(x=650,y=150)
        label3=Message(f3,text="White Teeth’s subtle humour is found in the mundane flaws and absurd fates of two multicultural families as they navigate the complex realities of race, roots and religion in post-war London",fg="black",bg="white",font=("Calibri",15),aspect=800)
        label3.place(x=650,y=200)
        label4=Label(f3,text="Rs.550",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label4.place(x=650,y=310)
        label5=Label(f3,text="Quantity",fg="black",bg="lightgoldenrod",font=("Calibri",20))
        label5.place(x=650,y=350)
        self.quantity=Entry(f3,font=("Comfortaa",15),bg='lightgray')
        self.quantity.place(x=760,y=350,width=50,height=35)
        btn=Button(f3,text="Add to cart",command=self.addco3,cursor="hand2",font=("Calibri",15),fg="black",bg="lightgoldenrod")
        btn.place(x=650,y=400)
        self.img=ImageTk.PhotoImage(file="WHITE TEETH.png")
        img=Label(f3,image=self.img).place(x=150,y=100,width=400,height=550)
        btn1=Button(f3,text="Back",command=self.appscreen,cursor="hand2",font=("Calibri",15,"bold","underline"),fg="red",bg="lightgoldenrod",bd=0)
        btn1.place(x=55,y=50)
        
    def addco(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Based on a True Story',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Based on a True Story')),int(self.quantity.get())])
            messagebox.showinfo('product status','Based on a True Story has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('product status','Based on a True Story has not been added to cart')

    def addco1(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['A Confederacy of Dunces',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('A Confederacy of Dunces')),int(self.quantity.get())])
            messagebox.showinfo('product status','A Confederacy of Dunces has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('product status','A Confederacy of Dunces has not been added to cart')
            
    def addco2(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['Hyperbole and a Half',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('Hyperbole and a Half')),int(self.quantity.get())])
            messagebox.showinfo('Product status','Alan Turing: The Enigma has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','Hyperbole and a Half has not been added to cart')
            
    def addco3(self):
        def Spaces(n,s1=" "):
            s=""
            for i in range(n):
                s+=s1
            return s
        global cart_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this book to the cart?")
        if op:
            cart_list.append(['White Teeth',int(self.quantity.get())*550,str(int(self.quantity.get())*550),Spaces(50-len('White Teeth')),int(self.quantity.get())])
            messagebox.showinfo('Product status','White Teeth has been succesfully added to cart')
            self.appscreen()
        else:
            messagebox.showinfo('Product status','White Teeth has not been added to cart')
        
    def regclear(self):
        self.entry.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)

    def loginclear(self):
        self.email_txt.delete(0,END)
        self.password.delete(0,END)

    def fpclear(self):
        self.email_txt.delete(0,END)
        self.password.delete(0,END)
        self.cpassword.delete(0,END)

    def forgot_password(self):
        Frame_fp=Frame(self.root,bg="white")
        Frame_fp.place(x=0,y=0,height=700,width=1366)
        self.img=ImageTk.PhotoImage(file="bg_image.jpg")
        img=Label(Frame_fp,image=self.img).place(x=0,y=0,width=1366,height=700)
        frame_input=Frame(self.root,bg="white")
        frame_input=Frame(self.root,bg="white")
        frame_input.place(x=320,y=130,height=480,width=500)
        label1=Label(frame_input,text="New Password",font=('Algerian',32,'bold',"underline"),fg="black",bg="white")
        label1.place(x=75,y=20)
        label2=Label(frame_input,text="Email id",font=("Comfortaa",20),fg='orangered',bg='white')
        label2.place(x=30,y=95)
        self.email_txt=Entry(frame_input,font=("Comfortaa",15),bg='lightgray')
        self.email_txt.place(x=30,y=145,width=270,height=35)
        label3=Label(frame_input,text="Password*",font=("Comfortaa",20),fg='orangered',bg='white')
        label3.place(x=30,y=195)
        self.password=Entry(frame_input,font=("Comfortaa",15),bg="lightgray")
        self.password.place(x=30,y=245,width=270,height=35)
        label5=Label(frame_input,text="*Should have minimum 8 characters",font=("Calibri",10),fg="red",bg="white")
        label5.place(x=30,y=280)
        label4=Label(frame_input,text="Confirm Password",font=("Comfortaa",20),fg='orangered',bg='white')
        label4.place(x=30,y=300)
        self.cpassword=Entry(frame_input,font=("Comfortaa",15),bg="lightgray")
        self.cpassword.place(x=30,y=345,width=270,height=35)
        btn2=Button(frame_input,text="Change",command=self.fp,cursor="hand2",font=("Comfortaa",15,"bold"),fg="white",bg="orangered",bd=0,width=15,height=1)
        btn2.place(x=90,y=400)
        btn3=Button(frame_input,command=self.loginform,text="Password changed?Go back to login page",cursor="hand2",font=("Calibri",10),fg='black',bg="white",bd=0)
        btn3.place(x=90,y=440)

    def fp(self):        
        if self.email_txt.get()=="" or self.password.get()=="" or self.cpassword.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.password.get()!=self.cpassword.get():
            messagebox.showerror("Error","Password and confirm password should be same",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host='localhost',user='root',database='library',password='password')
                cur=con.cursor()
                cur.execute("update cust_details set password=%s where email_id=%s",(self.password.get(),self.email_txt.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success !! ","Your password has been changed",parent=self.root)
                self.fpclear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)
              
root=Tk()
ob=App(root)
root.mainloop




