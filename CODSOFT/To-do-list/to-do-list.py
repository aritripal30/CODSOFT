import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

#to create the main window
root = tk.Tk()
root.title("To-Do List")

#Entry widget to add tasks
entry = tk.Entry(root, width=30)
entry.pack(padx=20)

#button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

#listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=20, width=30)
listbox.pack(padx=100)

#button to remove selected task
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

#to execute the application
root.mainloop()