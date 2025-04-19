import tkinter as tk
from tkinter import ttk
import sqlite3

def view_sales():
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sales ORDER BY sale_date DESC")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", tk.END, values=row)

# GUI Setup
root = tk.Tk()
root.title("Sales Tracking")
root.geometry("700x400")

tk.Label(root, text="Sales Records", font=("Arial", 16)).pack(pady=10)

columns = ("ID", "Product Name", "Quantity", "Total Price", "Sale Date")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)

tree.pack(pady=20)

tk.Button(root, text="Refresh", command=view_sales, bg="blue", fg="white").pack(pady=5)

view_sales()
root.mainloop()
