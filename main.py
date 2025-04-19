import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to open modules
def open_dashboard():
    subprocess.Popen(["python", "dashboard.py"])

def open_employee():
    subprocess.Popen(["python", "employee.py"])

def open_supplier():
    subprocess.Popen(["python", "supplier.py"])

def open_category():
    subprocess.Popen(["python", "category.py"])
 
def open_product():
    subprocess.Popen(["python", "product.py"])

def open_sales():
    subprocess.Popen(["python", "sales.py"])

def open_billing():
    subprocess.Popen(["python", "billing.py"])

def exit_system():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("🏪 Inventory Management System")
root.geometry("500x450")

tk.Label(root, text="Main Menu", font=("Arial", 18, "bold")).pack(pady=10)

# Buttons for modules
buttons = [
    ("📊 Dashboard", open_dashboard),
    ("👨‍💼 Employee Management", open_employee),
    ("🚛 Supplier Management", open_supplier),
    ("📂 Category Management", open_category),
    ("📦 Product Management", open_product),
    ("💰 Sales Tracking", open_sales),
    ("🧾 Billing System", open_billing),
    ("❌ Exit", exit_system),
]

for text, command in buttons:
    tk.Button(root, text=text, command=command, font=("Arial", 12), width=30, pady=5).pack(pady=5)

root.mainloop()
