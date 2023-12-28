import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = combo_box.get()
    label.config(text=f"Selected country: {selected_item}")

window = tk.Tk()
window.title("CITY CHOOSING ")
window.geometry("250x300")

# ایجاد برچسب
label = tk.Label(window, text="Choose your country:")
label.pack()

# ایجاد کمبوباکس
cities = ["USA","UK","Deutschland","Canada","France","China","Gigaland"]
combo_box = ttk.Combobox(window, values=cities)

# تنظیم کارنت
combo_box.current(0)  # انتخاب مورد اول به عنوان کارنت

combo_box.pack()

# تنظیم عملکرد برای رویداد انتخاب آیتم
combo_box.bind("<<ComboboxSelected>>", on_select)

window.mainloop()