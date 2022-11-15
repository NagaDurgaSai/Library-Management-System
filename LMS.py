
from tkinter import*
from tkinter import ttk
import random
import time
import tkinter.messagebox

class Library:

    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='white')

        MemberType=StringVar()
        BookID=StringVar()
        Ref=StringVar()
        BookTitle=StringVar()
        Title=StringVar()
        FirstName=StringVar()
        LastName=StringVar()
        Address=StringVar()
        PostCode=StringVar()
        PhoneNo=StringVar()
        Author=StringVar()
        DateofIssued=StringVar()
        DueDate=StringVar()
        ReturnFine=StringVar()
        ReturnDate=StringVar()
        Price=StringVar()

        def Reset():
            MemberType.set("")
            BookID.set("")
            Ref.set("")
            BookTitle.set("")
            Title.set("")
            FirstName.set("")
            LastName.set("")
            Address.set("")
            PostCode.set("")
            PhoneNo.set("")
            Author.set("")
            DateofIssued.set("")
            DueDate.set("")
            ReturnFine.set("")
            ReturnDate.set("")
            Price.set("")
            self.txtDisplayR.delete("1.0",END)
        def Delete():
            self.txtDisplayR.delete("1.0",END)
        
        def Exit():
        	Exit=tkinter.messagebox.askyesno("Library Management System","Confirm Do You Want To Exit")
        	if Exit>0:
        		root.destroy()
        		return
        def DisplayData():
           
           self.txtFrameDetail.insert(END,"\t"+MemberType.get()+"\t\t"+Ref.get()+"\t"+BookTitle.get()+"\t"+
           Title.get()+"\t"+FirstName.get() +"\t"+Address.get()+"\t\t"+BookTitle.get()+"\t"+PostCode.get()+"\t"+
           PhoneNo.get()+"\t"+Author.get()+"\t"+DateofIssued.get()+"\t\t"+DueDate.get()+ReturnDate.get()+ "\n")

        def Receipt():
            self.txtDisplayR.insert(END,'MemberType: \t\t'+MemberType.get() + "\n")
            self.txtDisplayR.insert(END,'BookID: \t\t'+BookID.get() + "\n")
            self.txtDisplayR.insert(END,'Ref: \t\t' +Ref.get() + "\n")
            self.txtDisplayR.insert(END,'FirstName: \t\t' + FirstName.get() + "\n")
            self.txtDisplayR.insert(END,'BookTitle: \t\t' + BookTitle.get() + "\n")
            self.txtDisplayR.insert(END,'PhoneNo: \t\t' + PhoneNo.get() + "\n")
            self.txtDisplayR.insert(END,'Author: \t\t' + Author.get() + "\n")
            self.txtDisplayR.insert(END,'DateofIssued: \t\t' + DateofIssued.get() + "\n")
            self.txtDisplayR.insert(END,'DueDate: \t\t' + DueDate.get() + "\n")
            self.txtDisplayR.insert(END,'ReturnFine: \t\t' + ReturnFine.get() + "\n")
            self.txtDisplayR.insert(END,'Price: \t\t' + Price.get() + "\n") 

        

        #------------------------------------------------Frames--------------------------------------------------------#
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame =Frame(MainFrame,width=1450,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle =Label(TitleFrame,width=39,font=('Times New Roman',40,'bold'),text="\tLibrary Management System\t",bg="cadetblue",fg='Crimson',padx=12)
        self.lblTitle.grid()
        
        ButtonFrame =Frame(MainFrame,bd=20,width=1250,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail =Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame,bd=20,width=1300,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame,bd=10,width=900,height=300,padx=20,relief=RIDGE,font=('Times New Roman',12,'bold'),text="Library Membership Info:",fg="cadetblue")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,font=('Times New Roman',12,'bold'),text="BookDetails",fg="Crimson")
        DataFrameRIGHT.pack(side=RIGHT)
        #======================================widget============================================================================================================================
        self.lblMemberType = Label(DataFrameLEFT, font=('Times New Roman',12),text="MemberType:",padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0,sticky=W)
        
        self.cboMemberType = ttk.Combobox(DataFrameLEFT, state='readonly',textvariable = MemberType,
                                        font=('Times New Roman',12), width=20)
        self.cboMemberType['value']=('--select--','Student','Lecturer','AdminStaff','MembershipNo','Purchase Id','AadharCardNo',
        'DrivingLicense','Govt.ID')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column=1)

        self.lblBookID =Label(DataFrameLEFT, font=('Times New Roman',12),text="BookID:",padx=2,pady=2)
        self.lblBookID.grid(row=0,column=2,sticky=W)
        self.lblBookID=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=BookID,width=25)
        self.lblBookID.grid(row=0,column=3)

        self.lblRef =Label(DataFrameLEFT, font=('Times New Roman',12),text="Ref:",padx=2,pady=2)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.lblRef=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=Ref,width=22)
        self.lblRef.grid(row=1,column=1)

        self.lblBookTitle =Label(DataFrameLEFT, font=('Times New Roman',12),text="BookTitle:",padx=2,pady=2)
        self.lblBookTitle.grid(row=1,column=2,sticky=W)
        self.lblBookTitle=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=BookTitle,width=25)
        self.lblBookTitle.grid(row=1,column=3)

        self.lblTitle = Label(DataFrameLEFT, font=('Times New Roman',12),text="Title:",padx=2,pady=2)
        self.lblTitle.grid(row=2,column=0,sticky=W)
        self.cboTitle = ttk.Combobox(DataFrameLEFT, state='readonly',textvariable = Title,
                                        font=('Times New Roman',12), width=20)
        self.cboTitle['value']=('--select--','Mr.','Mrs.','Ms')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2,column=1)


        self.lblFirstName = Label(DataFrameLEFT,font=('Times New Roman',12),text="FirstName:",padx=2,pady=2)
        self.lblFirstName.grid(row=3,column=0,sticky=W)
        self.lblFirstName=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=FirstName,width=25)
        self.lblFirstName.grid(row=3,column=1)
        
        self.lblLastName = Label(DataFrameLEFT,font=('Times New Roman',12),text="LastName:",padx=2,pady=2)
        self.lblLastName.grid(row=4,column=0,sticky=W)
        self.lblLastName=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=LastName,width=25)
        self.lblLastName.grid(row=4,column=1)

        self.lblAddress = Label(DataFrameLEFT,font=('Times New Roman',12),text="Address:",padx=2,pady=2)
        self.lblAddress.grid(row=5,column=0,sticky=W)
        self.lblAddress=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=Address,width=25)
        self.lblAddress.grid(row=5,column=1)
        
        self.lblPostCode = Label(DataFrameLEFT,font=('Times New Roman',12),text="PostCode:",padx=2,pady=2)
        self.lblPostCode.grid(row=6,column=0,sticky=W)
        self.lblPostCode=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=PostCode,width=25)
        self.lblPostCode.grid(row=6,column=1)
        
        self.lblPhoneNo = Label(DataFrameLEFT,font=('Times New Roman',12),text="PhoneNo:",padx=2,pady=2)
        self.lblPhoneNo.grid(row=7,column=0,sticky=W)
        self.lblPhoneNo=Entry(DataFrameLEFT,font=('Times New Roman',12),textvariable=PhoneNo,width=25)
        self.lblPhoneNo.grid(row=7,column=1)

        self.lblAuthor =Label(DataFrameLEFT, font=('Times New Roman',12),text="Author:",padx=2,pady=2)
        self.lblAuthor.grid(row=2,column=2,sticky=W)
        self.lblAuthor=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=Author,width=25)
        self.lblAuthor.grid(row=2,column=3)

        self.lblDateIssued =Label(DataFrameLEFT, font=('Times New Roman',12),text="DateofIssued:",padx=2,pady=2)
        self.lblDateIssued.grid(row=3,column=2,sticky=W)
        self.lblDateIssued=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=DateofIssued,width=25)
        self.lblDateIssued.grid(row=3,column=3)
        
        self.lblDueDate =Label(DataFrameLEFT, font=('Times New Roman',12),text="DueDate:",padx=2,pady=2)
        self.lblDueDate.grid(row=4,column=2,sticky=W)
        self.lblDueDate=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=DueDate,width=25)
        self.lblDueDate.grid(row=4,column=3)

        self.lblReturnFine =Label(DataFrameLEFT, font=('Times New Roman',12),text="ReturnFine:",padx=2,pady=2)
        self.lblReturnFine.grid(row=5,column=2,sticky=W)
        self.lblReturnFine=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=ReturnFine,width=25)
        self.lblReturnFine.grid(row=5,column=3)

        self.lblReturnDate  =Label(DataFrameLEFT, font=('Times New Roman',12),text="ReturnDate:",padx=2,pady=2)
        self.lblReturnDate.grid(row=6,column=2,sticky=W)
        self.lblReturnDate=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=ReturnDate,width=25)
        self.lblReturnDate.grid(row=6,column=3)

        self.lblPrice =Label(DataFrameLEFT, font=('Times New Roman',12),text="Price:",padx=2,pady=2)
        self.lblPrice.grid(row=7,column=2,sticky=W)
        self.lblPrice=Entry(DataFrameLEFT, font=('Times New Roman',12),textvariable=Price,width=25)
        self.lblPrice.grid(row=7,column=3)
        #=======================================Widget=================================================================
        self.txtDisplayR=Text(DataFrameRIGHT,font=('Times New Roman',12,'bold'),width=32,height=13,padx=8,pady=20)
        self.txtDisplayR.grid(row=0,column=2)
        #======================================ListBox==================================================================
        
        ListofBooks = ['Lets Do Epic Shit ','Desi Gaming','Programming in C','Ancient LPU','Made in Phagwaraa','Dr.B.R.Ambedkar','London','Hello Law gate','PythonDeveloper']
        
        def SelectedBook(evt):
            value =str(booklist.get(booklist.curselection()))
            print(value)
            w=value

            if (w == "Lets Do Epic Shit"):
                BookID.set("ISBN 7654321204")
                BookTitle.set("God is King")
                Author.set("Avigo varikarr")

                ReturnFine.set("Rs.59")
                Price.set("Rs.1000")
                Receipt()
                

                import datetime
                
                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                ReturnDate.set(d1)
                DueDate.set(d3)
                DateofIssued.set("datetime")

            elif(w == "Desi Gaming"):
                 BookID.set("ISBN 098765432")
                 BookTitle.set("Art of Game")
                 Author.set("Shivaram Harari")

                 ReturnFine.set("Rs.60")
                 Price.set("Rs.800")
                 Receipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 ReturnDate.set(d1)
                 DueDate.set(d3)
                 DateofIssued.set("No")   

            elif(w == "Programming in C"):
                 BookID.set("ISBN 87654321")
                 BookTitle.set("Programming Books")
                 Author.set("RsSalaria")

                 ReturnFine.set("Rs.30")
                 Price.set("Rs.349")
                 Receipt()

                 import datetime

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 ReturnDate.set(d1)
                 DueDate.set(d3)
                 DateofIssued.set('No')        

            elif(w == "Ancient LPU"):
            	 BookID.set("ISBN 198765323")
            	 BookTitle.set("Consul")
            	 Author.set("Virgil")

            	 ReturnFine.set("Rs.20")
            	 Price.set("Rs.400")
            	 Receipt()

            	 import random

            	 d1=datetime.date.today()
            	 d2=datetime.timedelta(days=10)
            	 d3=(d1+d2)
            	 ReturnDate.set(d1)
            	 DueDate.set(d3)
            	 DateofIssued.set('No')

            elif(w == "Made in Phagwaraa"):
            	 BookID.set("ISBN-87645643")
            	 BookTitle.set("About Africa")
            	 Author.set("Chinua Achebe")

            	 ReturnFine.set("Rs.25")
            	 Price.set("Rs.780")
            	 Receipt()

            	 import random

            	 d1=datetime.date.today()
            	 d2=datetime.timedelta(days=10)
            	 d3=(d1+d2)
            	 ReturnDate.set(d1)
            	 DueDate.set(d3)
            	 DateofIssued.set(d1)

            elif(w == "Dr.B.R.Ambedkar"):
                 BookID.set("BR90876599")
                 BookTitle.set("Life Journey")
                 Author.set("Babasaheb")

                 ReturnFine.set("Rs.20")
                 Price.set("Rs.880")
                 Receipt()

                 import random

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 ReturnDate.set(d1)
                 DueDate.set(d3)
                 DateofIssued.set(d1)

            elif(w == "London"):
                 BookID.set("LN87654322")
                 BookTitle.set("London Street")
                 Author.set("Manu Rajput")

                 ReturnFine.set("Rs.20")
                 Price.set("Rs.950")
                 Receipt()

                 import random

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 ReturnDate.set(d1)
                 DueDate.set(d3)
                 DateofIssued.set(d1)

            elif(w == "Hello Law gate"):
                 BookID.set("IHI987654")
                 BookTitle.set("India")
                 Author.set("Yashvardhan Rajput")

                 ReturnFine.set("Rs.20")
                 Price.set("Rs.900")
                 Receipt()

                 import random

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 ReturnDate.set(d1)
                 DueDate.set(d3)
                 DateofIssued.set(d1)
            elif(w == "PythonDeveloper"):
                 BookID.set("PYDV98765")
                 BookTitle.set("Programming Language")
                 Author.set("Guido van Rossum")

                 ReturnFine.set("Rs.50")
                 Price.set("Rs.990")
                 Receipt()

                 import random

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=10)
                 d3=(d1+d2)
                 ReturnDate.set(d1)
                 DueDate.set(d3)
                 DateofIssued.set(d1)              	 
           
        booklist = Listbox(DataFrameRIGHT,width=20,height=12,font=('Times New Roman',12,'bold'))
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0,column=0,padx=8)

        for items in ListofBooks:
        	booklist.insert(END,items)
        #======================================================================================================================	
        self.lblLabel =Label(FrameDetail,font=('Times New Roman',14,'bold'),pady=7,
        text="MemberType\tRef \tTitle \tFirstname \tLastname \tAddress \tPostCode \tBookTitle \t DateIssued \tDueDate",)
        self.lblLabel.grid(row=0,column=0)

        self.textDisplayR=Text(FrameDetail,font=('arial',13,'bold'),width=141,heigh=4,padx=2,pady=4)
        self.textDisplayR.grid(row=1,column=0)	
        #=======================================Button=========================================================================
        self.btnDisplayData=Button(ButtonFrame,text="DISPLAYDATA",fg="Crimson",bg="cadetblue",font=('Times New Roman',12,'bold'),width=30,bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0,column=0)

        self.btnDelete=Button(ButtonFrame,text="DELETE",fg="Crimson",bg="cadetblue",font=('Times New Roman',12,'bold'),width=30,bd=4,command=Delete)
        self.btnDelete.grid(row=0,column=1)

        self.btnReset=Button(ButtonFrame,text="RESET",fg="Crimson",bg="cadetblue",font=('Times New Roman',12,'bold'),width=30,bd=4,command=Reset)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame,text="EXIT",fg="Crimson",bg="cadetblue",font=('Times New Roman',12,'bold'),width=30,bd=4,command=Exit)
        self.btnExit.grid(row=0,column=3)





if __name__=='__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
