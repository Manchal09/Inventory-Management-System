import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

def process_sale():
    product_name = entry_product.get()
    quantity = entry_quantity.get()

    if not product_name or not quantity:
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    # Check if product exists
    cursor.execute("SELECT quantity, price FROM products WHERE name=?", (product_name,))
    product = cursor.fetchone()

    if not product:
        messagebox.showerror("Error", "Product not found!")
        conn.close()
        return

    stock, price = product
    quantity = int(quantity)

    if quantity > stock:
        messagebox.showerror("Error", "Not enough stock!")
        conn.close()
        return

    total_price = quantity * price

    # Update stock
    cursor.execute("UPDATE products SET quantity = quantity - ? WHERE name=?", (quantity, product_name))

    # Insert into sales table
    cursor.execute("INSERT INTO sales (product_name, quantity, total_price, sale_date) VALUES (?, ?, ?, ?)",
                   (product_name, quantity, total_price, datetime.now()))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", f"Sale Processed!\nTotal: ${total_price:.2f}")
    view_products()

def view_products():
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity, price FROM products")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        tree.insert("", tk.END, values=row)

# GUI Setup
root = tk.Tk()
root.title("Billing System")
root.geometry("600x400")

tk.Label(root, text="Product Name").grid(row=0, column=0)
entry_product = tk.Entry(root)
entry_product.grid(row=0, column=1)

tk.Label(root, text="Quantity").grid(row=0, column=2)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=0, column=3)

tk.Button(root, text="Process Sale", command=process_sale, bg="green", fg="white").grid(row=0, column=4)

columns = ("Name", "Stock", "Price")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Name", text="Product Name")
tree.heading("Stock", text="Stock")
tree.heading("Price", text="Price")

tree.grid(row=1, column=0, columnspan=5, pady=20)

view_products()
root.mainloop()
