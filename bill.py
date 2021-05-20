from tkinter import*
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("NISHAN BILLING SOFTWARE")
        bg_color="#074463"
        title=Label(self.root,text="NISHAN STORE",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
      #======================variable=======================================
     #===================cosmetic=============
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
       #============================grocery=============
        self.rice=IntVar()
        self.sugar=IntVar()
        self.dal=IntVar()
        self.flour=IntVar()
        self.masala=IntVar()
        self.noodles=IntVar()

        #================drinking===========
        self.juice=IntVar()
        self.soft=IntVar()
        self.wine=IntVar()
        self.alochol=IntVar()
        self.apple=IntVar()
        self.energy=IntVar()
        #===========total product price=======
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.drinking_price=StringVar()       
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.drinking_tax=StringVar() 

        #=========customer=======
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()  
        self.search_no=StringVar()       
      


      
      
  #----------------customer details haru--------------
        f1=LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(f1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(f1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(f1,text="Phone NO.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(f1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        c_bill_lbl=Label(f1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(f1,width=15,textvariable=self.search_no,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        bill_btn=Button(f1,text="Search",width=8,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)
        #---------COSMETIC FRAME----------------
        f2=LabelFrame(self.root,bd=10,relief=GROOVE, text="Cosmetic",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f2.place(x=5,y=180,width=325,height=380)

        bath_lable=Label(f2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(f2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_lable=Label(f2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_txt=Entry(f2,width=10,textvariable=self.face_cream, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        face_w_lable=Label(f2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        facw_w_txt=Entry(f2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        hair_s_lable=Label(f2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(f2,width=10,textvariable=self.spray, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        hair_g_lable=Label(f2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(f2,width=10,textvariable=self.gell ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lable=Label(f2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(f2,width=10,textvariable=self.loshan, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)




        #---------Grocery FRAME----------------
        f3=LabelFrame(self.root,bd=10,relief=GROOVE, text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f3.place(x=320,y=180,width=325,height=380)

        rice_lable=Label(f3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(f3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        sugar_lable=Label(f3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(f3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        dal_lable=Label(f3,text="Dal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        dal_txt=Entry(f3,width=10,textvariable=self.dal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        flour_lable=Label(f3,text="Flour",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        flour_txt=Entry(f3,width=10,textvariable=self.flour,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        masala_lable=Label(f3,text="Masala",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        masala_txt=Entry(f3,width=10,textvariable=self.masala,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        noodles_lable=Label(f3,text="Noodles",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        noodles_txt=Entry(f3,width=10,textvariable=self.noodles,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

 #---------Drinking----------------
        f4=LabelFrame(self.root,bd=10,relief=GROOVE, text="Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f4.place(x=620,y=180,width=325,height=380)

        juice_lable=Label(f4,text="Juice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        juice_txt=Entry(f4,width=10,textvariable=self.juice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        soft_lable=Label(f4,text="Soft Drinks",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        soft_txt=Entry(f4,width=10,textvariable=self.soft,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        wine_lable=Label(f4,text="Wine",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        wine_txt=Entry(f4,width=10,textvariable=self.wine,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        alcohol_lable=Label(f4,text="Alcohol",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        alcohol_txt=Entry(f4,width=10,textvariable=self.alochol,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        apple_lable=Label(f4,text="Apple Cider",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        apple_txt=Entry(f4,width=10,textvariable=self.apple,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        energy_lable=Label(f4,text="Energy Drinks",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        energy_txt=Entry(f4,width=10,textvariable=self.energy,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#================bill areaaaaaaa=================================
        f5=Frame(self.root,bd=10,relief=GROOVE)
        f5.place(x=950,y=180,width=340,height=380)
        bill_title=Label(f5,text="Bill Area",font="arial 12 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(f5,orient=VERTICAL)
        self.txtarea=Text(f5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #============button frame===============
        f6=LabelFrame(self.root,bd=10,relief=GROOVE, text="Billing Menu  ",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f6.place(x=0,y=560,relwidth=1,height=142)
        
        m1=Label(f6,text="Total Cosmetic Price",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(f6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
       
        m2=Label(f6,text="Total Grocery Price",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(f6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
       
        m3=Label(f6,text="Total Drinking Price",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(f6,width=18,textvariable=self.drinking_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1=Label(f6,text="Cosmetic Tax",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(f6,width=18,font="arial 10 bold",textvariable=self.cosmetic_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2=Label(f6,text="Grocery Tax",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(f6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        c3=Label(f6,text="Drinking Tax",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(f6,width=18,textvariable=self.drinking_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_f=Frame(f6,bd=7,relief=GROOVE)
        btn_f.place(x=705,width=570,height=105)

        total_btn=Button(btn_f,command=self.total,text="Total",bg="cadetblue",bd=2,fg="white",pady=15,width=9,font="arial 15 bold").grid(row=0,column=0,padx=3,pady=5)
        gbill_btn=Button(btn_f,text="Generate Bill",bg="cadetblue",bd=2,fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=3,pady=5)
        cl_btn=Button(btn_f,text="Clear",bg="cadetblue",bd=2,fg="white",pady=15,width=9,font="arial 15 bold").grid(row=0,column=2,padx=3,pady=5)
        ex_btn=Button(btn_f,text="Exit",bg="cadetblue",bd=2,fg="white",pady=15,width=9,font="arial 15 bold").grid(row=0,column=3,padx=3,pady=5)
        
    def total(self):
        self.total_cosmetic_price=float(
                                    (self.soap.get()*40)+
                                    (self.face_cream.get()*140)+
                                    (self.face_wash.get()*180)+
                                    (self.gell.get()*30)+
                                    (self.spray.get()*340)+
                                    (self.loshan.get()*230)
                                    )
        self.cosmetic_price.set(str(self.total_cosmetic_price))

        self.total_grocery_price=float(
                                    (self.rice.get()*150)+
                                    (self.sugar.get()*95)+
                                    (self.dal.get()*80)+
                                    (self.flour.get()*40)+
                                    (self.masala.get()*35)+
                                    (self.noodles.get()*20)
                                    )
        self.grocery_price.set(str(self.total_grocery_price))


        self.total_drinks_price=float(
                                    (self.soft.get()*180)+
                                    (self.wine.get()*600)+
                                    (self.alochol.get()*350)+
                                    (self.apple.get()*150)+
                                    (self.juice.get()*130)+
                                    (self.energy.get()*45)
                                    )
        self.drinking_price.set(str(self.total_drinks_price))







     

    



root=Tk()
obj= Bill_App(root)
root.mainloop()

