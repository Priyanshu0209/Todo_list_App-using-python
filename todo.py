import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")
        self.root.config(bg="lightblue")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 24, "bold"), bg="lightblue")
        self.title_label.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, font=("Helvetica", 14), width=26)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_task_btn = tk.Button(self.frame, text="Add Task", font=("Helvetica", 14), command=self.add_task)
        self.add_task_btn.pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(self.root, font=("Helvetica", 14), height=10, width=30, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=20)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.update_task_btn = tk.Button(self.button_frame, text="Update Task", font=("Helvetica", 14), command=self.update_task)
        self.update_task_btn.pack(side=tk.LEFT, padx=10)

        self.delete_task_btn = tk.Button(self.button_frame, text="Delete Task", font=("Helvetica", 14), command=self.delete_task)
        self.delete_task_btn.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task != "":
                self.tasks[selected_index] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
