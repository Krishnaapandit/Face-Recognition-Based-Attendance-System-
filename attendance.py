import os
import mysql.connector
import openpyxl
from tkinter import *
from tkinter import filedialog, messagebox

# Global variable for imported data
mydata = []

class Attendance:

    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Import Data to Database")

        import_btn = Button(self.root, text="Import XLSX", command=self.import_data)
        import_btn.pack(pady=20)

        delete_btn = Button(self.root, text="Delete All Data", command=self.delete_all_data)
        delete_btn.pack(pady=10)

    def fetch_data(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No Data Found!")
                return

            conn = mysql.connector.connect(user='root', password='host', host='localhost', database='face_recognition', port=3306)
            mycursor = conn.cursor()

            for row in mydata:
                mycursor.execute("INSERT INTO stdattendance (Name, std_roll_no, std_id, Date, Time, std_attendance) VALUES (%s, %s, %s, %s, %s, %s)",
                                 (row[0], row[1], row[2], row[3], row[4], row[5]))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Data Successfully Imported to Database!")

        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}")

    def delete_all_data(self):
        try:
            conn = mysql.connector.connect(user='root', password='host', host='localhost', database='face_recognition', port=3306)
            mycursor = conn.cursor()

            mycursor.execute("DELETE FROM stdattendance")
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "All Data Successfully Deleted!")

        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}")

    def import_data(self):
        try:
            mydata.clear()
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open XLSX",
                                             filetypes=(("XLSX File", "*.xlsx"), ("All File", "*.*")))
            workbook = openpyxl.load_workbook(fln)
            worksheet = workbook.active

            for row in worksheet.iter_rows(values_only=True):
                mydata.append(row)

            self.fetch_data()

        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
