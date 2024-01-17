import tkinter as tk
from tkinter import Toplevel, Listbox, Button, messagebox

class lab_7:
    def __init__(self, master):
        self.master = master
        self.master.title("Это окно")
        self.master.geometry("600x400")  # Устанавливаем размер основного окна

        self.button_panel = tk.Frame(self.master)
        self.button_panel.pack(side=tk.TOP, pady=20)

        self.set_button = tk.Button(self.button_panel, text="Set", command=self.set_selection, width=15, height=2)
        self.reset_button = tk.Button(self.button_panel, text="Reset", command=self.reset_selection, width=15, height=2)
        self.exit_button = tk.Button(self.master, text="Выход", command=self.confirm_exit, width=15, height=2)

        self.set_button.pack(side=tk.LEFT, padx=10)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        self.exit_button.pack(side=tk.LEFT, padx=10)

        self.available_listbox = tk.Listbox(self.master, selectmode=tk.MULTIPLE, width=30, height=15)
        self.available_listbox.pack(side=tk.LEFT, padx=10)

        self.selected_listbox = tk.Listbox(self.master, selectmode=tk.MULTIPLE, width=30, height=15)
        self.selected_listbox.pack(side=tk.RIGHT, padx=10)

        self.move_button = tk.Button(self.master, text="Добавить >", command=self.move_selection, width=15, height=2)
        self.move_all_button = tk.Button(self.master, text="Добавить все >", command=self.move_all_selection, width=15, height=2)
        self.remove_button = tk.Button(self.master, text="< Убрать", command=self.remove_selection, width=15, height=2)
        self.remove_all_button = tk.Button(self.master, text="< Убрать все", command=self.remove_all_selection, width=15, height=2)

        self.move_button.pack()
        self.move_all_button.pack()
        self.remove_button.pack()
        self.remove_all_button.pack()

        self.initialize_lists()

        self.selected_elements = []

        self.master.mainloop()
    def initialize_lists(self):
        initial_elements = ["Granta",
                            "Solaris",
                            "2107",
                            "Zeekr",
                            "BMW"]
        for element in initial_elements:
            self.available_listbox.insert(tk.END, element)

    def move_selection(self):
        selected_indices = self.available_listbox.curselection()
        for idx in selected_indices[::-1]:
            item = self.available_listbox.get(idx)
            self.available_listbox.delete(idx)
            self.selected_listbox.insert(tk.END, item)

    def move_all_selection(self):
        all_items = self.available_listbox.get(0, tk.END)
        for item in all_items:
            self.selected_listbox.insert(tk.END, item)
        self.available_listbox.delete(0, tk.END)

    def remove_selection(self):
        selected_indices = self.selected_listbox.curselection()
        for idx in selected_indices[::-1]:
            item = self.selected_listbox.get(idx)
            self.selected_listbox.delete(idx)
            self.available_listbox.insert(tk.END, item)

    def remove_all_selection(self):
        all_items = self.selected_listbox.get(0, tk.END)
        for item in all_items:
            self.available_listbox.insert(tk.END, item)
        self.selected_listbox.delete(0, tk.END)

    def set_selection(self):
        self.selected_elements = self.selected_listbox.get(0, tk.END)
        set_window = Toplevel(self.master)
        set_window.title("Вы выбрали к покупке")
        set_listbox = Listbox(set_window, selectmode=tk.MULTIPLE, width=50, height=5)

        for element in self.selected_elements:
            set_listbox.insert(tk.END, element)
        set_listbox.pack()

    def reset_selection(self):
        all_items = self.selected_listbox.get(0, tk.END)
        for item in all_items:
            self.available_listbox.insert(tk.END, item)
        self.selected_listbox.delete(0, tk.END)
        self.selected_elements = []

    def confirm_exit(self):
        response = messagebox.askokcancel("Подтверждение выхода", "Вы уверены, что заплатили?")
        if response:
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = lab_7(root)
    root.mainloop()