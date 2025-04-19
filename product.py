import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def add_product():
    name = entry_name.get()
    category = entry_category.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    
    if not name or not category or not quantity or not price:
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, category, quantity, price) VALUES (?, ?, ?, ?)", 
                   (name, category, int(quantity), float(price)))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Product Added!")
    view_products()

def view_products():
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        tree.insert("", tk.END, values=row)

# GUI Setup
root = tk.Tk()
root.title("Product Management")
root.geometry("700x400")

tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Category").grid(row=0, column=2)
entry_category = tk.Entry(root)
entry_category.grid(row=0, column=3)

tk.Label(root, text="Quantity").grid(row=1, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=1, column=1)

tk.Label(root, text="Price").grid(row=1, column=2)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=3)

tk.Button(root, text="Add Product", command=add_product, bg="green", fg="white").grid(row=1, column=4)

columns = ("ID", "Name", "Category", "Quantity", "Price")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Category", text="Category")
tree.heading("Quantity", text="Quantity")
tree.heading("Price", text="Price")

tree.grid(row=2, column=0, columnspan=5, pady=20)

view_products()
root.mainloop()
