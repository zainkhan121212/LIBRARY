import tkinter as tk
from tkinter import messagebox

lend_records = []

def lend_book():
    book_title = entry_book.get()
    member_id = entry_member_id.get()
    due_date = entry_due_date.get()
#testing
    if book_title and member_id and due_date:
        lend_records.append({'book': book_title, 'member_id': member_id, 'due_date': due_date})
        messagebox.showinfo("Success", f"Book '{book_title}' lent to Member ID {member_id}")
        entry_book.delete(0, tk.END)
        entry_member_id.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

# GUI Setup
root = tk.Tk()
root.title("Book Lending System")
root.geometry("400x300")

tk.Label(root, text="Book Title").pack(pady=5)
entry_book = tk.Entry(root)
entry_book.pack()

tk.Label(root, text="Member ID").pack(pady=5)
entry_member_id = tk.Entry(root)
entry_member_id.pack()

tk.Label(root, text="Due Date (YYYY-MM-DD)").pack(pady=5)
entry_due_date = tk.Entry(root)
entry_due_date.pack()

tk.Button(root, text="Lend Book", command=lend_book).pack(pady=20)

root.mainloop()
