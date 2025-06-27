import tkinter as tk
from tkinter import messagebox

def register():
    if not (first_name.get() and last_name.get() and email.get() and username.get() and password.get() and confirm.get()):
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля!")
        return
    if password.get() != confirm.get():
        messagebox.showerror("Ошибка", "Пароли не совпадают!")
        return
    if not agree_var.get():
        messagebox.showwarning("Ошибка", "Вы должны согласиться с условиями.")
        return
    messagebox.showinfo("Успех", "Регистрация прошла успешно!")

root = tk.Tk()
root.title("Register Form")
root.geometry("400x500")
root.configure(bg="#1e1e1e")


header = tk.Label(root, text="Register", font=("Helvetica", 18, "bold"),
                  bg="#2b2b2b", fg="white", pady=10)
header.pack(fill="x")

form = tk.Frame(root, bg="#1e1e1e")
form.pack(pady=20)

def add_entry(label_text, show=None):
    label = tk.Label(form, text=label_text, fg="white", bg="#1e1e1e", anchor="w")
    label.pack(fill="x", padx=40)
    entry = tk.Entry(form, bg="#2b2b2b", fg="white", insertbackground="white",
                     highlightthickness=0, relief="flat", font=("Arial", 10), show=show)
    entry.pack(padx=40, pady=5, fill="x")
    return entry

first_name = add_entry("First Name")
last_name = add_entry("Last Name")
email = add_entry("Email Address")
username = add_entry("User Name")
password = add_entry("Password", show="*")
confirm = add_entry("Confirm Password", show="*")


agree_var = tk.BooleanVar()
agree_check = tk.Checkbutton(form, text="I agree to the Terms and Conditions", variable=agree_var,
                             bg="#1e1e1e", fg="white", activebackground="#1e1e1e",
                             selectcolor="#1e1e1e")
agree_check.pack(pady=10, padx=40, anchor="w")


btn = tk.Button(form, text="Sign Me Up >", command=register,
                bg="#44c767", fg="white", font=("Arial", 12, "bold"),
                activebackground="#5cbf2a", relief="flat")
btn.pack(pady=10, padx=30, fill="x")

root.mainloop()