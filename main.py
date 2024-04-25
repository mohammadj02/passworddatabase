import tkinter as tk
from tkinter import messagebox, font as tkfont
import sqlite3

def create_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(username, password):
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "User account created successfully")

def create_account_page():
    app = tk.Tk()
    app.title("Create Account")

    # Styling
    app_font = tkfont.Font(family="Helvetica", size=12)

    # Layout
    tk.Label(app, text="Username", font=app_font).grid(row=0, sticky="w", padx=10, pady=10)
    tk.Label(app, text="Password", font=app_font).grid(row=1, sticky="w", padx=10, pady=10)

    username_entry = tk.Entry(app, font=app_font)
    password_entry = tk.Entry(app, show="*", font=app_font)

    username_entry.grid(row=0, column=1, padx=10, pady=10)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(app, text="Create Account", command=lambda: insert_user(username_entry.get(), password_entry.get()), font=app_font).grid(row=2, column=1, sticky="ew", padx=10, pady=10)

    app.mainloop()

# Ensure the database is initialized and the GUI is started
create_db()
create_account_page()
