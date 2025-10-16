import tkinter as tk
from tkinter import messagebox
import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for task in json.load(f):
                listbox.insert(tk.END, task)

def save_tasks():
    with open(FILE, "w") as f:
        json.dump(listbox.get(0, tk.END), f)

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("⚠️ Empty Task", "Please enter a task before adding!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks()
    except:
        messagebox.showinfo("🗑️", "Select a task to delete!")

def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        listbox.delete(0, tk.END)
        save_tasks()

root = tk.Tk()
root.title("📝 Butterfly To-Do List")
root.geometry("400x400")
root.config(bg="#222222")

tk.Label(root, text="✨ To-Do List ✨", fg="white", bg="#222222", font=("Helvetica", 16, "bold")).pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#222222")
button_frame.pack()

tk.Button(button_frame, text="Add Task", command=add_task, bg="#10b981", fg="white", width=12).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#ef4444", fg="white", width=12).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Clear All", command=clear_all, bg="#3b82f6", fg="white", width=12).grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, width=45, height=12, font=("Arial", 11), selectbackground="#3b82f6", bg="#111111", fg="white", relief="flat")
listbox.pack(pady=15)

load_tasks()
root.mainloop()
