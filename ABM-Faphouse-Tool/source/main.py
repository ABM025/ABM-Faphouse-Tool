# main.py - GUI Launcher
import tkinter as tk
from browser import check_account

def on_submit():
    email = email_entry.get()
    password = pass_entry.get()
    result = check_account(email, password)
    output_label.config(text=result)

root = tk.Tk()
root.title('ABM-Faphouse Login')
tk.Label(root, text='Email:').pack()
email_entry = tk.Entry(root)
email_entry.pack()
tk.Label(root, text='Password:').pack()
pass_entry = tk.Entry(root, show='*')
pass_entry.pack()
tk.Button(root, text='Login', command=on_submit).pack()
output_label = tk.Label(root, text='')
output_label.pack()
root.mainloop()
