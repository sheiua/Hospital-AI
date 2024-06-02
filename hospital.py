lblNameTablet=Label (DataframeLeft,text="Names OF Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
lblNameTablet.grid(row=0,colomn=0)

comNametablet=ttk.Combobox(DataframeLeft,font=("times new roman",12,"bold"),
                                                                        width=33)
comNametablet["values"]=("NIce","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
comNametablet.grid(row=0,colomn=1)