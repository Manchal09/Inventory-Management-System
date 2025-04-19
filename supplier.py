import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def add_supplier():
    name = entry_name.get()
    contact = entry_contact.get()
    
    if not name or not contact:
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO suppliers (name, contact) VALUES (?, ?)", (name, contact))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Supplier Added!")
    view_suppliers()

def view_suppliers():
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM suppliers")
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        tree.insert("", tk.END, values=row)

# GUI Setup
root = tk.Tk()
root.title("Supplier Management")
root.geometry("600x400")

tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Contact").grid(row=0, column=2)
entry_contact = tk.Entry(root)
entry_contact.grid(row=0, column=3)

tk.Button(root, text="Add Supplier", command=add_supplier, bg="green", fg="white").grid(row=0, column=4)

columns = ("ID", "Name", "Contact")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Contact", text="Contact")

tree.grid(row=1, column=0, columnspan=5, pady=20)

view_suppliers()
root.mainloop()
