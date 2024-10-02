import tkinter as tk

root = tk.Tk()
root.title("Тестовое окошко")
listbox = tk.Listbox(root, height=10, width=50)
listbox.pack(padx=10, pady=10)

listbox.insert(tk.END, "какой-то текст")
listbox.insert(tk.END, "и потом еще")
root.mainloop()