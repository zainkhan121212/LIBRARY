import tkinter as tk
from tkinter import messagebox

members = []

def register_member():
    name = entry_name.get()
    member_id = entry_id.get()
    email = entry_email.get()

    if name and member_id and email:
        members.append({'name': name, 'id': member_id, 'email': email})
        messagebox.showinfo("Success", "Member Registered Successfully!")
        entry_name.delete(0, tk.END)
        entry_id.delete(0, tk.END)
        entry_email.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

# GUI Setup
root = tk.Tk()
root.title("Library Member Registration")
root.geometry("400x300")

tk.Label(root, text="Member Name").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Member ID").pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Email").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack()

tk.Button(root, text="Register Member", command=register_member).pack(pady=20)

root.mainloop()
