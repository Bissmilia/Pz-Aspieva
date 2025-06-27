import tkinter as tk
from tkinter import messagebox

def show_numbers():
    try:
        A = int(entry_a.get())
        B = int(entry_b.get())
        if A >= B:
            messagebox.showerror("Ошибка", "A должно быть меньше B")
            return

        numbers = list(range(A, B + 1))
        count = len(numbers)
        result_text = f"Числа от {A} до {B}:\n{', '.join(map(str, numbers))}\nКоличество: {count}"
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целые числа")


root = tk.Tk()
root.title("Числа от A до B")

tk.Label(root, text="Введите A:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Введите B:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Показать числа", command=show_numbers).grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()