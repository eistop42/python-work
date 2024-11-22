import sqlite3
import tkinter as tk
import json

class NoteModel:
    """База данных для хранения заметок"""

    def __init__(self):
        self._notes = self._load_from_file()

    def get_notes(self):
        return self._notes

    def add_note(self, text):
        """Добавление новой заметки"""
        next_id = self._get_last_id() + 1  # получаем новый id
        note = {"id": next_id, "text": text}  # создаем заметку
        self._notes.append(note)  # добавляем в список

        self.save_to_file()

    def delete_by_id(self, note_id):
        """Удаление по id"""
        for number, note in enumerate(self._notes):
            if note['id'] == note_id:
                self._notes.pop(number)
                break
        else:
            print('Такой заметки нет')

    def find_by_text(self, text):
        """Поиск заметки"""
        res_notes = []
        for note in self._notes:
            if text in note['text']:
                res_notes.append(note)
        return res_notes

    def _load_from_file(self):
        """Загрузка данных из файла"""
        with open('notes.json', 'r', encoding='utf-8') as f:
            notes = json.load(f)
        return notes

    def save_to_file(self):
        with open('notes.json', 'w', encoding='utf-8') as f:
            notes = json.dump(self._notes, f)
        return notes

    def _get_last_id(self):
        """Поиск максимального id"""
        if self._notes:
            max = self._notes[0]['id']
            for note in self._notes:
                if note['id'] > max:
                    max = note['id']
        else:
            max = 0
        return max


class NoteModelSQL:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = self._dict_factory

    def get_notes(self):
        cursor = self.connection.cursor()
        cursor.execute('select * from notes')
        return cursor.fetchall()

    def add_note(self, text):
        with self.connection as connection:
            cursor = connection.cursor()
            # print(text)
            cursor.execute('insert into notes (text) values (?)', (text,))

    @staticmethod
    def _dict_factory(cursor, row):
        d = {}
        # cursor = self.connection.cursor()
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __del__(self):
        print('закрытие подключения')
        self.connection.close()

class NoteWindow:
    def __init__(self, model):
        self.model = model
        self.create_window()
        self.show_notes()
        self.root.mainloop()

    def create_window(self):
        self.root = tk.Tk()
        self.root.title('Заметки')

        # окошко для ввода
        self.input = tk.Text(self.root, height=10, width=20)
        self.input.grid(row=0, column=0, padx=10, pady=10)

        # окошко для вывода
        self.output = tk.Listbox(self.root, height=10, width=20)
        self.output.grid(row=0, column=1, padx=10, pady=10)

        self.button = tk.Button(self.root, text='Добавить заметку', command=self.add_note)
        self.button.grid(row=1, column=0, padx=10, pady=10)

    def show_notes(self):
        notes = self.model.get_notes()

        self.output.delete(0, tk.END)
        for note in notes:
            self.output.insert(tk.END, note['text'])

    def add_note(self):
        text = self.input.get('1.0', tk.END).strip()
        self.model.add_note(text)
        self.show_notes()

        self.input.delete('1.0', tk.END)


# model = NoteModel()
sqlmodel = NoteModelSQL('C:\\Users\\Б - Преподаватель\\Documents\\Евдокимов Илья\\python-work\\db\\notes.db')

window = NoteWindow(sqlmodel)
