import tkinter as tk
from tkinter import ttk
import sqlite3

def get_count(table):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def update_dashboard():
    label_products.config(text=f"Total Products: {get_count('products')}")
    label_employees.config(text=f"Total Employees: {get_count('employees')}")
    label_suppliers.config(text=f"Total Suppliers: {get_count('suppliers')}")
    label_sales.config(text=f"Total Sales: {get_count('sales')}")

# GUI Setup
root = tk.Tk()
root.title("📊 Inventory Dashboard")
root.geometry("500x300")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label_products = tk.Label(frame, text="Total Products: 0", font=("Arial", 14))
label_products.pack(pady=5)

label_employees = tk.Label(frame, text="Total Employees: 0", font=("Arial", 14))
label_employees.pack(pady=5)

label_suppliers = tk.Label(frame, text="Total Suppliers: 0", font=("Arial", 14))
label_suppliers.pack(pady=5)

label_sales = tk.Label(frame, text="Total Sales: 0", font=("Arial", 14))
label_sales.pack(pady=5)

tk.Button(root, text="Refresh", command=update_dashboard, bg="blue", fg="white").pack(pady=10)

update_dashboard()
root.mainloop()
