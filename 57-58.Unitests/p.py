text = """Вот пример программы, которая создаёт простое приложение с заметками на основе библиотеки Tkinter в Python:

```python
import tkinter as tk

class NoteBook(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.notes = {}  # Словарь для хранения заметок
        self.note_count = 0  # Счетчик заметок

        # Создаем окно приложения
        window_title = tk.Tk()
        window_title.title("Заметки")
        window_title.geometry("800x400")

        # Добавляем фрейм для заметок
        self._frame = tk.Frame(window_title)
        self._frame.pack(fill="both", expand=True)

        # Отображаем кнопку "Добавить заметку"
        add_note_button = tk.Button(self._frame, text="Добавить заметку", command=self.add_note)
        add_note_button.pack(side=tk.LEFT)

    def add_note(self):
        note_text = input("Введите текст заметки: ")
        if note_text != "":
            self.notes[self.note_count] = note_text
            self.note_count += 1
            # Обновляем список заметок в интерфейсе
            self._update_notes()

    def _update_notes(self):
        note_list = []
        for i in self.notes:
            note_list.append(self.notes[i])
        self.label_notes.config(text="Заметки: \n".join(note_list))

    # Создаем виджеты для отображения заметок и кнопки "Очистить заметки"
    label_notes = tk.Label(self._frame)
    self._update_notes()  # Вызываем функцию для отображения первой заметки

if __name__ == "__main__":
    notebook = NoteBook()
    notebook.master.mainloop()
```

Эта программа создаёт простое окно с кнопкой «Добавить заметку». При нажатии на эту кнопку пользователь может ввести текст заметки, который будет сохранён в словаре `notes`. При каждом добавлении заметки вызывается функция `_update_notes`, которая обновляет интерфейс, отображая список всех заметок.

Также в программе есть кнопка «Очистить заметки», которая очищает словарь `notes` и удаляет все заметки из интерфейса.

Заметьте, что это только пример, и вы можете изменить его в соответствии с вашими потребностями. Например, вы можете добавить возможность удаления заметок, сортировки списка заметок и т.д. """

import markdown
import os
import webbrowser

text = markdown.markdown(text, extensions=['fenced_code'])

# записали данные в файл
with open('text.html', 'w') as f:
    f.write(text)
    # получили путь до файла
    path = os.path.abspath('text.html')

webbrowser.open(path)


