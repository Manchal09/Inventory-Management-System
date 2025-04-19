import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def add_category():
    name = entry_name.get()
    
    if not name:
        messagebox.showerror("Error", "Category name is required!")
        return

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Category Added!")
    view_categories()

def delete_category():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select a category to delete!")
        return

    item_id = tree.item(selected_item)["values"][0]

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categories WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Category Deleted!")
    view_categories()

def view_categories():
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        tree.insert("", tk.END, values=row)

# GUI Setup
root = tk.Tk()
root.title("Category Management")
root.geometry("500x400")

tk.Label(root, text="Category Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Button(root, text="Add Category", command=add_category, bg="green", fg="white").grid(row=0, column=2)
tk.Button(root, text="Delete Category", command=delete_category, bg="red", fg="white").grid(row=0, column=3)

columns = ("ID", "Name")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Category Name")

tree.grid(row=1, column=0, columnspan=4, pady=20)

view_categories()
root.mainloop()
