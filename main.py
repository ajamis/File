from tkinter import filedialog, messagebox, Button, Tk, Label, StringVar
import shutil
import os
import easygui  # pip install easygui
from tkinter import ttk
import pyperclip  # pip install pyperclip

def file_open_box():
    path = easygui.fileopenbox()
    return path

def directory_open_box():
    path = filedialog.askdirectory()
    return path

def open_file():
    path = file_open_box()
    try:
        os.startfile(path)
    except Exception as e:
        messagebox.showinfo("خطا", f"خطا در بازکردن فایل: {e}")

def copy_file():
    source = file_open_box()
    destination = directory_open_box()
    try:
        shutil.copy(source, destination)
        messagebox.showinfo("موفقیت", "فایل با موفقیت کپی شد.")
    except Exception as e:
        messagebox.showinfo("خطا", f"خطا در کپی فایل: {e}")

def delete_file():
    path = file_open_box()
    try:
        os.remove(path)
        messagebox.showinfo("موفقیت", "فایل با موفقیت حذف شد.")
    except Exception as e:
        messagebox.showinfo("خطا", f"خطا در حذف فایل: {e}")

def rename_file():
    path = file_open_box()
    new_name = easygui.enterbox("نام جدید فایل (بدون پسوند) را وارد کنید:")
    if new_name:
        try:
            directory, old_name = os.path.split(path)
            extension = os.path.splitext(old_name)[1]
            new_path = os.path.join(directory, new_name + extension)
            os.rename(path, new_path)
            messagebox.showinfo("موفقیت", "فایل با موفقیت تغییر نام داده شد.")
        except Exception as e:
            messagebox.showinfo("خطا", f"خطا در تغییر نام فایل: {e}")
    else:
        messagebox.showinfo("خطا", "نام جدید وارد نشده است.")

def copy_file_path_to_clipboard():
    path = file_open_box()
    if path:
        pyperclip.copy(path)
        messagebox.showinfo("موفقیت", "مسیر فایل در کلیپ‌بورد کپی شد.")
    else:
        messagebox.showinfo("خطا", "هیچ فایلی انتخاب نشده است.")

# تنظیمات رابط کاربری
window = Tk()
window.title("مدیریت فایل")
window.configure(bg="#2c3e50")  # تم تاریک
window.geometry("350x500")


# عنوان
Label(window, text="عملیاتی که می‌خواهید انجام دهید", font=("Helvetica", 14), bg="#2c3e50", fg="white").pack(pady=10)

# دکمه‌ها با طراحی بهتر و رنگ‌بندی متفاوت
button_frame = ttk.Frame(window, padding=10)
button_frame.pack(pady=20)

Button(button_frame, command=open_file, text="باز کردن فایل", fg="white", bg="#3498db", font=("Helvetica", 12), relief="solid", width=20).grid(row=0, column=0, pady=5)
Button(button_frame, command=copy_file, text="کپی فایل", fg="white", bg="#3498db", font=("Helvetica", 12), relief="solid", width=20).grid(row=1, column=0, pady=5)
Button(button_frame, command=delete_file, text="حذف فایل", fg="white", bg="#e74c3c", font=("Helvetica", 12), relief="solid", width=20).grid(row=2, column=0, pady=5)
Button(button_frame, command=rename_file, text="تغییر نام فایل", fg="white", bg="#9b59b6", font=("Helvetica", 12), relief="solid", width=20).grid(row=3, column=0, pady=5)
Button(button_frame, command=copy_file_path_to_clipboard, text="کپی مسیر فایل", fg="white", bg="#2ecc71", font=("Helvetica", 12), relief="solid", width=20).grid(row=4, column=0, pady=5)

# فوتر (اختیاری)
footer_label = Label(window, text="توسعه داده شده توسط سلما عجمی", font=("Helvetica", 10), bg="#2c3e50", fg="white")
footer_label.pack(side="bottom", pady=10)

# شروع حلقه Tkinter
window.mainloop()
