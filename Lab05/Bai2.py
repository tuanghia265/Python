import tkinter as tk
from tkinter import ttk
import pyodbc 

conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.;DATABASE=QLSinhVien; UID=sa;PWD=123;Encrypt=no')

cursor=conn.cursor()

cursor.execute("SELECT TenNhom FROM NhomMonAn")
dishes=cursor.fetchall()
root = tk.Tk()
root.geometry("820x400+240+180")

root.columnconfigure(0, pad=4)

root.title("Quản lý món ăn")

lblTop = tk.Label(text="Nhóm món ăn").grid(row=0, column=1, sticky='W',pady=20)

n = tk.StringVar()
food_cbb = ttk.Combobox(root, width=20, textvariable=n)
food_cbb.grid(row=0, column=4, sticky='E', pady=20)
food_cbb.insert(0,)

root.mainloop()