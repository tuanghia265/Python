import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import *
root=tk.Tk()
root.title("Đăng kí học phần")
root.geometry("800x600")

id_var=tk.StringVar()
id_label=tk.Label(root,text='Mã số sinh viên: ',foreground='blue',font=('Times New Roman',12)).grid(column=0,row=1,pady=10)
id_entry=tk.Entry(root,textvariable=id_var,font=('Times New Roman',12),width=80).grid(column=1,row=1)

name_var=tk.StringVar()
name_label=tk.Label(root,text='Họ tên:',font=('Times New Roman',12),foreground='blue').grid(column=0,row=2,pady=10)
name_entry=tk.Entry(root,textvariable=name_var,font=('Times New Roman',12),width=80).grid(column=1,row=2)


date_var=tk.StringVar()
date_label=tk.Label(root,text='Ngày sinh:',font=('Times New Roman',12),foreground='blue').grid(column=0,row=3,pady=10)
date_entry=tk.Entry(root,textvariable=date_var,font=('Times New Roman',12),width=80).grid(column=1,row=3)


email_var=tk.StringVar()
email_label=tk.Label(root,text='Email:',font=('Times New Roman',12),foreground='blue').grid(column=0,row=4,pady=10)
email_entry=tk.Entry(root,textvariable=email_var,font=('Times New Roman',12),width=80).grid(column=1,row=4)


phone_var=tk.StringVar()
phone_label=tk.Label(root,text='Số điện thoại:',font=('Times New Roman',12),foreground='blue').grid(column=0,row=5,pady=10)
phone_entry=tk.Entry(root,textvariable=phone_var,font=('Times New Roman',12),width=80).grid(column=1,row=5)


hk_var=tk.StringVar()
hk_label=tk.Label(root,text='Học kỳ:',font=('Times New Roman',12),foreground='blue').grid(column=0,row=6)
hk_entry=tk.Entry(root,textvariable=hk_var,font=('Times New Roman',12),width=80).grid(column=1,row=6)

n=tk.StringVar()
year_label=tk.Label(root,text='Năm học:',foreground='blue',font=('Times New Roman',12)).grid(column=0,row=7,pady=10)
yearchoosen=ttk.Combobox(root,font=('Times New Roman',12),width=80,textvariable=n).grid(column=1,row=7)

sub_label=tk.Label(root,text='Chọn môn học:',foreground='blue',font=('Times New Roman',12)).grid(column=0,row=8)
subcheck1=tk.Checkbutton(root,text='Lập trình python',foreground='blue',font=('Times New Roman',12)).grid(column=1,row=8)
subcheck2=tk.Checkbutton(root,text='Lập trình python',foreground='blue',font=('Times New Roman',12)).grid(column=1,row=8)
subcheck3=tk.Checkbutton(root,text='Lập trình python',foreground='blue',font=('Times New Roman',12)).grid(column=1,row=9)
subcheck4=tk.Checkbutton(root,text='Lập trình python',foreground='blue',font=('Times New Roman',12)).grid(column=1,row=9)



tk.Label(root,text="Thông tin đăng kí học phần",foreground="red",background="light green",font=('Times New Roman',32,'bold')).grid(row=0,column=1)


root.mainloop()