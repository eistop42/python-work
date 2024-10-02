import tkinter
from abc import ABC, abstractmethod


class NoteModel:
    """База данных для хранения заметок"""

    def __init__(self):
        self._notes = [{"id": 1, "text": "Сижу на паре"}]

    def get_notes(self):
        return self._notes

    def add_note(self, text):
        """Добавление новой заметки"""
        next_id = self._get_last_id() + 1  # получаем новый id
        note = {"id": next_id, "text": text}  # создаем заметку
        self._notes.append(note)  # добавляем в список

    def _get_last_id(self):
        """Поиск максимального id"""
        max = self._notes[0]['id']
        for note in self._notes:
            if note['id'] > max:
                max = note['id']
        return max


class AbstractView(ABC):
    """Абстрактный класс для реализации классов-представлений"""

    @abstractmethod
    def render_notes(self, notes):
        """Абстрактный метод для визуализации заметок"""
        pass


class GraphicView(AbstractView):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Тестовое окошко")
        self.listbox = tkinter.Listbox(self.root, height=10, width=50)
        self.listbox.pack(padx=10, pady=10)

    def render_notes(self, notes):
        """Показывает заметки в окне"""
        self.listbox.delete(0, 'end')
        for note in notes:
            text = f"{note['id']} --- {note['text']}"
            self.listbox.insert(tk.END, text)
        self.root.mainloop()


class ConsoleView(AbstractView):

    def render_notes(self, notes):
        for note in notes:
            text = f"{note['id']} --- {note['text']}"
            print(text)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_notes(self):
        """Показать все заметки на экране"""
        notes = self.model.get_notes()
        self.view.render_notes(notes)

        # for note in notes:
        #     print(f"{note['id']} - {note['text']}")

    def add_note(self):
        text = input('Введи текст заметки: ')
        self.model.add_note(text)


model = NoteModel()

graphic_view = GraphicView()
console_view = ConsoleView()

contr = Controller(model, console_view)

while True:
    print('\n\n1 - Посмотреть все заметки')
    print('2 - Добавить заметку')
    print('q - Выйти')

    choice = input("Выбирай: ")

    if choice == '1':
        contr.show_notes()
    elif choice == '2':
        contr.add_note()
    elif choice == 'q':
        break
