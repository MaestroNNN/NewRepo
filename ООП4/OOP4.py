import tkinter as tk
from tkinter import ttk

class CountryInformation:
    COUNTRIES = [
        "Россия", "Германия", "Габон", "Украина",
        "Португалия", "Италия", "Испания", "Сенегал"
    ]
    INFORMATION = [
        "Привет, Россия",
        "Guten Tag, Германия",
        "M'bolo, Габон",
        "здоровеньки булы, Украина",
        "Olá, Португалия",
        "Buongiorno, Италия",
        "Buenos días, Испания",
        "Sa-laam-a-ley-kum, Сенегал"
    ]

def on_combobox_select(event):
    selected_index = combobox.current()
    if selected_index >= 0:
        information = CountryInformation.INFORMATION[selected_index]
        combobox_area.config(state=tk.NORMAL)
        combobox_area.delete("1.0", tk.END)
        combobox_area.insert(tk.END, information)
        combobox_area.config(state=tk.DISABLED)
    else:
        combobox_area.config(state=tk.NORMAL)
        combobox_area.delete("1.0", tk.END)
        combobox_area.insert(tk.END, "Выберите страну")
        combobox_area.config(state=tk.DISABLED)

def on_checkbox_select():
    if checkbox_var.get() == 1:
        checkbox_area.config(state=tk.NORMAL)
        checkbox_area.delete("1.0", tk.END)
        checkbox_area.insert(tk.END, "CheckBox выбран")
        checkbox_area.config(state=tk.DISABLED)
    else:
        checkbox_area.config(state=tk.NORMAL)
        checkbox_area.delete("1.0", tk.END)
        checkbox_area.insert(tk.END, "CheckBox не выбран")
        checkbox_area.config(state=tk.DISABLED)

def on_textfield_enter(event):
    text = textfield.get()
    textfield_area.config(state=tk.NORMAL)
    textfield_area.delete("1.0", tk.END)
    textfield_area.insert(tk.END, "Введенный текст: " + text)
    textfield_area.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Окно")

combobox = tk.ttk.Combobox(root, values=CountryInformation.COUNTRIES)
combobox.bind("<<ComboboxSelected>>", on_combobox_select)
combobox_area = tk.Text(root, height=5, width=30)
combobox_area.insert(tk.END, "Выберите страну")
combobox_area.config(state=tk.DISABLED)

checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Подтвердить", variable=checkbox_var, command=on_checkbox_select)
checkbox_area = tk.Text(root, height=2, width=30)
checkbox_area.insert(tk.END, "CheckBox не выбран")
checkbox_area.config(state=tk.DISABLED)

textfield = tk.Entry(root)
textfield.bind("<Return>", on_textfield_enter)
textfield_area = tk.Text(root, height=2, width=30)
textfield_area.insert(tk.END, "Введите текст")
textfield_area.config(state=tk.DISABLED)

combobox.pack(side=tk.TOP)
combobox_area.pack(side=tk.TOP)
checkbox.pack(side=tk.LEFT)
checkbox_area.pack(side=tk.RIGHT)
textfield.pack(side=tk.BOTTOM)
textfield_area.pack(side=tk.BOTTOM)

root.mainloop()
