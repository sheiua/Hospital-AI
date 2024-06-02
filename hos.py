





































Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
Detailsframe.place(x=0,y=600,width=1530,height=190)

# ==============================================================DataframeLeft=========================================================================

lblNameTablet=Label (DataframeLeft,font=("arial",12,"bold"),text="Name OF Tablets",padx=2,pady=6)
lblNameTablet.grid(row=0,colomn=0,sticky=W)

comNametablet=ttk.Combobox(DataframeLeft,state="readonly"),
                                                font=("arial",12,"bold"),width=33)
comNametablet["values"]=("NIce","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
comNametablet.current(0)
comNametablet.grid(row=0,colomn=1)

lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
lblref.grid(row=1,colomn=0,sticky=W)
txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
txtref.grid(row=1,colomn=1)

lblDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
lblDose.grid(row=2,colomn=0,sticky=W)
txtDose=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
txtDose.grid(row=2,colomn=1)

lblNoOftablets=Label(DataFrameLeft,font=("arial",12,"bold"),text="No Of Tablets::",padx=2,pady=6)
lblNoOftablets.grid(row=3,colomn=0,sticky=W)
txtNoOftablets=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
txtNoOftablets.grid(row=3,colomn=1)

lblLot=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
lblLot.grid(row=4,colomn=0,sticky=W)
txtLot=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
txtLot.grid(row=4,colomn=1)

lblissueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
lblissueDate.grid(row=5,colomn=0,sticky=W)
txtissueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
txtissueDate.grid(row=5,colomn=1)

lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
lblExpDate.grid(row=6,colomn=0,sticky=W)
txtExpDate=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
txtExpDate.grid(row=6,colomn=1)

lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
lblDailyDose.grid(row=7,colomn=0,sticky=W)
txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
txtDailyDose.grid(row=7,colomn=1)

lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
lblSideEffect.grid(row=8,colomn=0,sticky=W)
txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),width=35)
txtSideEffect.grid(row=8,colomn=1)

lblFurtherinfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Information",padx=2)
lblFurtherinfo.grid(row=0,colomn=2,sticky=W)
txtFurtherinfo=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
txtFurtherinfo.grid(row=0,colomn=3)

lblBloodPressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure",padx=2,pady=6)
lblBloodPressure.grid(row=1,colomn=2,sticky=W)
txtBloodPressure=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
txtBloodPressure.grid(row=1,colomn=3)

lblStorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
lblStorage.grid(row=2,colomn=2,sticky=W)
txtStorage=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
txtStorage.grid(row=2,colomn=3)

lblMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mediciation",padx=2,pady=6)
lblMedicine.grid(row=3,colomn=2,sticky=W)
txtMedicine=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
txtMedicine.grid(row=3,colomn=3,sticky=W)

lblPatientId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Id",padx=2,pady=6)
lblPatientId.grid(row=4,colomn=2,sticky=W)
txtPatientId=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
txtPatientId.grid(row=4,colomn=3)

lblNhsNumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number",padx=2,pady=6)
lblNhsNumber.grid(row=5,colomn=2,sticky=W)
txtNhsNumber=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
txtNhsNumber.grid(row=5,colomn=3)


lblPatientName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name",padx=2,pady=6)
lblPatientName.grid(row=6,colomn=2,sticky=W)
txtPatientName=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
txtPatientName.grid(row=6,colomn=3)

lblDateOfBirth=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Of Birth",padx=2,pady=6)
lblDateOfBirth(row=7,colomn=2,sticky=W)
txtDateOfBirth=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
txtDateOfBirth.grid(row=7,colomn=3)

lblPatientAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address",padx=2,pady=6)
lblPatientAddress.grid(row=8,colomn=2,sticky=W)
txtPatientAddress=Entry(DataFrameLeft,font=("arial",12,"bold"),width=35)
txtPatientAddress.grid(row=8,colomn=3)


# ============================================================DataframeRight=================================================================================================================================
self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
self.txtPrescription.grid(row=0,colomn=0)


# ========================================Buttons================================================================================
btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnPrescription.grid(row=0,colomn=0)

btnPrescriptionData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnPrescriptionData.grid(row=0,colomn=1)


btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnUpdate.grid(row=0,colomn=2)


btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnDelete.grid(row=0,colomn=3)


btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnClear.grid(row=0,colomn=4)

btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
btnExit.grid(row=0,colomn=5)


# =============================================Table===========================================================
# ===========================================Scrollbar=========================================================
scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
self.hospital_table=ttk.Treeview(Detailsframe,colomn=("nameoftablets","ref","dose","nooftablets","lot","issuedate",
                            "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack=(side=BOTTOM,fill=X)
scroll_y.pack=(side=RIGHT,fill=Y)

scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

self.hospital_table.heading("nameoftable",text="Name Of Table")
self.hospital_table.heading("ref",text="Reference No.")
self.hospital_table.heading("dose",text="Dose")
self.hospital_table.heading(nooftablets",text="No Of Tablets")
self.hospital_table.heading("lot",text="Lot")
self.hospital_table.heading("issuedate",text="Issue Date")
self.hospital_table.heading("expdate",text="Exp Date")
self.hospital_table.heading("dailydose",text="Daily Dose")
self.hospital_table.heading("storage",text="Storage")
self.hospital_table.heading("nhsnumber",text="NHS Number")
self.hospital_table.heading("pname",text="Patient Name")
self.hospital_table.heading("dob",text="DOB")
self.hospital_table.heading("address",text="Address")

self.hospital_table["snow"]="headings"

self.hospital_table.pack(fill=BOTH,expand=1)