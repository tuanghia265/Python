import tkinter as tk

root=tk.Tk()

root.geometry("600x400")

name_var=tk.StringVar()
pass_var=tk.StringVar()

def submit():
    name=name_var.get()
    password=pass_var.get()

    print("The name is : "+name)
    print("The password is : "+password)

    name_var.set("")
    pass_var.set("")

name_label=tk.Label(root,text='Username',font=('calibre',10,'bold'))

name_entry=tk.Entry(root,textvariable=name_var,font=('calibre',10,'normal'))

pass_label=tk.Label(root,text='Password',font=('calibre',10,'bold'))

pass_entry=tk.Entry(root,textvariable=pass_var,font=('calibre',10,'normal'),show='●')

sub_btn=tk.Button(root,text='Submit',command=submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
pass_label.grid(row=1,column=0)
pass_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()

