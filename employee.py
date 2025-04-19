import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def add_employee():
    name = entry_name.get()
    position = entry_position.get()
    salary = entry_salary.get()
    
    if not name or not position or not salary:
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", 
                   (name, position, float(salary)))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Employee Added!")
    view_employees()

def view_employees():
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        tree.insert("", tk.END, values=row)

# GUI Setup
root = tk.Tk()
root.title("Employee Management")
root.geometry("600x400")

tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Position").grid(row=0, column=2)
entry_position = tk.Entry(root)
entry_position.grid(row=0, column=3)

tk.Label(root, text="Salary").grid(row=0, column=4)
entry_salary = tk.Entry(root)
entry_salary.grid(row=0, column=5)

tk.Button(root, text="Add Employee", command=add_employee, bg="green", fg="white").grid(row=0, column=6)

columns = ("ID", "Name", "Position", "Salary")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Position", text="Position")
tree.heading("Salary", text="Salary")

tree.grid(row=1, column=0, columnspan=7, pady=20)

view_employees()
root.mainloop()
