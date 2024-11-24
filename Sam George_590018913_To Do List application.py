import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Create main application window
app = tk.Tk()
app.title("To-Do List")
app.geometry("400x400")

# Input field and Add button
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

add_task_button = tk.Button(app, text="Add Task", width=20, command=add_task)
add_task_button.pack(pady=5)

# Listbox to display tasks
tasks_listbox = tk.Listbox(app, width=50, height=15)
tasks_listbox.pack(pady=10)

# Buttons to manage tasks
delete_task_button = tk.Button(app, text="Delete Task", width=20, command=delete_task)
delete_task_button.pack(pady=5)

clear_tasks_button = tk.Button(app, text="Clear All Tasks", width=20, command=clear_tasks)
clear_tasks_button.pack(pady=5)

# Run the application
app.mainloop()
