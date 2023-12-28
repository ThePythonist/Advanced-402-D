import tkinter as tk

def enter_class():
    student_name = entry_name.get()
    student_id = entry_id.get()
    student_major = entry_major.get()
    print(f"دانشجوی {student_name} با کد {student_id} و رشته {student_major} وارد کلاس شد.")

    class_window = tk.Toplevel(window)
    class_window.title("اطلاعات کلاس درس")
    class_window.geometry("300x250")
    class_window.resizable(width=False,height=False)

    class_label = tk.Label(class_window, text="اطلاعات کلاس درس:")
    class_label.pack()

    class_info = tk.Label(class_window, text="نام درس: فیزیک هسته ای\nاستاد: آقای احمد ذوقی \nزمان: شنبه و دوشنبه 10:00 - 12:00")
    class_info.pack()

    welcome_label = tk.Label(class_window, text=f"خوش آمدید، {student_name}!")
    welcome_label.pack()

window = tk.Tk()
window.title("ورود به کلاس")

window.geometry("400x300")
window.resizable(width=False,height=False)


# ایجاد برچسب ورودی نام دانشجو
label_name = tk.Label(window, text="نام دانشجو: ")
label_name.pack()

# ایجاد ورودی نام دانشجو
entry_name = tk.Entry(window)
entry_name.pack()

# ایجاد برچسب ورودی کد دانشجویی
label_id = tk.Label(window, text="کد دانشجویی: ")
label_id.pack()

# ایجاد ورودی کد دانشجویی
entry_id = tk.Entry(window)
entry_id.pack()

# ایجاد برچسب ورودی رشته تحصیلی
label_major = tk.Label(window, text="رشته تحصیلی: ")
label_major.pack()

# ایجاد ورودی رشته تحصیلی
entry_major = tk.Entry(window)
entry_major.pack()

# ایجاد دکمه ورود به کلاس
button = tk.Button(window, text="ورود به کلاس", command=enter_class)
button.pack()

window.mainloop()