import tkinter as tk
import requests
import markdown
import os
import webbrowser

class GraphicView():
    def __init__(self, bot):
        """Показывает заметки в окне"""
        self._create_window()
        self.bot = bot

        self.root.mainloop()

    def _create_window(self):
        self.root = tk.Tk()
        self.root.title('Заметки')

        # окошко для ввода
        self.input = tk.Text(self.root, height=20, width=20)
        self.input.grid(row=0, column=0, padx=10, pady=10)

        # окошко для вывода
        self.output = tk.Text(self.root, height=20, width=100)
        self.output.grid(row=0, column=1, padx=10, pady=10, rowspan=2)

        self.button = tk.Button(self.root, text='Отправить запрос', command=self.send_request)
        self.button.grid(row=2, column=0, padx=10, pady=10)

    def send_request(self):
        text = self.input.get('1.0', tk.END)

        response = self.bot.send_request(text)
        print(response)

        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, response)


class YandexTranslate:
    def __init__(self, token, catalog):
        self.token = token
        self.catalog = catalog

    def send_request(self, text):
        url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
        payload = {
            "sourceLanguageCode": "ru",
            "targetLanguageCode": "fr",
            "format": "HTML",
            "texts": [
                f"{text}"
            ],
            "folderId": f"{self.catalog}",
            "speller": False
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {self.token}"
        }

        response = requests.post(url, headers=headers, json=payload)
        text = response.json()['translations'][0]['text']
        return text


token = ''
catalog = ''

bot = YandexTranslate(token, catalog)
graphic_view = GraphicView(bot)



