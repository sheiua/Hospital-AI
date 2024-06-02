self.hospital_tabel.column("nameoftable",width=100)
self.hospital_tabel.column("ref",widh=100)
self.hospital_tabel.column("dose",widh=100)
self.hospital_tabel.column("nooftablets",widh=100)
self.hospital_tabel.column("lot",widh=100)
self.hospital_tabel.column("issuedate",widh=100)
self.hospital_tabel.column("expdate",widh=100)
self.hospital_tabel.column("dailydose",widh=100)
self.hospital_tabel.column("storage",widh=100)
self.hospital_tabel.column("nhsnumber",widh=100)
self.hospital_tabel.column("pname",widh=100)
self.hospital_tabel.column("dob",widh=100)
self.hospital_tabel.column("address",widh=100)

self.hospital_tabel.pack(fill=BOTH,expand=1)
self.hospital_table.bind("<BittonRelease=1>",self.get_curson)

self.fatch_data()






def update(self):
    conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
    my_cursor=conn.cursor()
    my_cursor.execute("update hospital set Nameoftablets=%s")






def get_cursor(self,event=):
    cursor_row=self.hospital_table.focus()
    content=self.hospital_table.item(custor_row)
    row=content ["values"]
    self.Nameoftablets.set(row[0])
    self.ref.set(row[1])
    self.Dose.set(row[2])
    self.Numbertablets.set(row[3])
    self.Lot.set(row[4])
    self.Issuedate.set(row[5])
    self.ExpDate.set(row[6])
    self.DailyDose.set(row[7])
    self.StorageAdvice.set(row)[8]
    self.nshNumber.set(row[9])
    self.PatientName.set(row[10])
    self.DateOfBirth.set(row[11])
    self.PatientAddress.ser(row[12])







def iPrectioption(self)
    self.txtProscription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")






def idelete(self):
    conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="Mydata")
    my_cursor=conn.cursor()
    query="dalete from hospital where Reference_No=%s"
    value(self.ref.get(),)
    my_cursor.execute(query,value)

    conn.commit()
    conn.close()
    self.fatch_data()
    messagebox.showinfo("Delete","Patient has been deleted successfully")







def clear(self):
    self.Nameoftablets.set("")





def iExit(self):
    iExit=messagebox.askyesno("Hospital managemnt system","Confirm you want to exit")
    if Iexit>0:
        root.destroy()
        return


