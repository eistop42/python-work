import tkinter as tk
import requests
import markdown
import os
import webbrowser

class GraphicView():
    def __init__(self, bot, browser):
        """Показывает заметки в окне"""
        self._create_window()
        self.bot = bot
        self.browser = browser

        self.root.mainloop()

    def _create_window(self):
        self.root = tk.Tk()
        self.root.title('Заметки')

        # окошко для ввода
        self.input = tk.Text(self.root, height=10, width=20)
        self.input.grid(row=0, column=0, padx=10, pady=10)

        # окошко для ввода
        self.input_role = tk.Text(self.root, height=10, width=20)
        self.input_role.grid(row=1, column=0, padx=10, pady=10)

        # окошко для вывода
        self.output = tk.Text(self.root, height=20, width=100)
        self.output.grid(row=0, column=1, padx=10, pady=10, rowspan=1)


        self.button = tk.Button(self.root, text='Отправить запрос', command=self.send_request)
        self.button.grid(row=2, column=0, padx=10, pady=10)

        self.button = tk.Button(self.root, text='Открыть в браузере', command=self.open_browser)
        self.button.grid(row=1, column=1, padx=10, pady=10)

    def send_request(self):
        text = self.input.get('1.0', tk.END)
        text_role = self.input_role.get('1.0', tk.END)

        response = self.bot.send_request(text, text_role)
        print(response)

        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, response)

    def open_browser(self):
        # логика открытия бразуера
        text = self.output.get('1.0', tk.END)
        self.browser.open_text(text)

class Browser:

    @staticmethod
    def open_text(text):
        text = markdown.markdown(text, extensions=['fenced_code'])

        # записали данные в файл
        with open('text.html', 'w') as f:
            f.write(text)
            # получили путь до файла
            path = os.path.abspath('text.html')

        webbrowser.open(path)


class YandexGPT:
    def __init__(self, token, catalog):
        self.token = token
        self.catalog = catalog

    def send_request(self, question, role_text):
        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        prompt = {
            "modelUri": f'gpt://{self.catalog}/yandexgpt-lite',
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": 1000
            },
            "messages" : [
                {
                    "role": "system",
                    "text": f"{role_text}"
                },
                {
                    "role": "user",
                    "text": f"{question}"
                }
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {self.token}"
        }

        response = requests.post(url, headers=headers, json=prompt)
        text = response.json()['result']['alternatives'][0]['message']['text']
        return text


token = ''
catalog = ''

bot = YandexGPT(token, catalog)
browser = Browser()
graphic_view = GraphicView(bot, browser)



