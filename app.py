from flask import Flask, render_template  # Подключаем "движок" сайта
import random  # Подключаем "кубик" для рандома

app = Flask(__name__)  # Инициализация приложения

# БАЗА ДАННЫХ ВАШИХ МОМЕНТОВ
WISHES = [
    {
        "image": "gif.gif",
        "text": "Люмос! Ты освещаешь мой мир.",
        "duration": 3000,
        "size": "80%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    }, # После последнего элемента запятая не обязательна, но внутри списка — всегда.
    {
        "image": "ALBUS2.gif",
        "text": "",
        "duration": 2970,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "rat.gif",
        "text": "",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "love-sweet.gif",
        "text": "I LOVE YOU",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "MALFOY.gif",
        "text": "😏😏😏",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "felix.gif",
        "text": "",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "PENGUIN.gif",
        "text": "🫵🫵🫵",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "NEWT.gif",
        "text": "",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "BK.gif",
        "text": "",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "SEXYKISS.gif",
        "text": "",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "DD.gif",
        "text": "",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "DIARY.gif",
        "text": "Невидимые чернила проявляются только для тебя...",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },
    {
        "image": "VINYL.gif",
        "text": "Ты - моя мелодия, которая никогда не надоест",
        "duration": 3000,
        "size": "100%",
        "animation": "animate__flip",
        "hide": False  # Добавляем параметр: НЕ скрывать
    },

]


@app.route('/')  # Эта строка говорит: "Делай это, когда кто-то зашел на сайт"
def magic_page():
    # Выбираем ОДИН случайный набор (картинка + текст) из списка WISHES
    # Задаем вероятности для каждого элемента из списка WISHES по порядку
    # 10 — часто, 1 — очень редко (секретка)
    weights = [10, 10, 10, 10, 10, 10, 10, 100, 5, 5, 20, 10, 200]  # Например, для трех гифок

    # Выбираем один элемент с учетом весов
    random_content = random.choices(WISHES, weights=weights, k=1)[0]

    # Отправляем этот набор в визуальный шаблон index.html
    return render_template('index.html', content=random_content)


if __name__ == '__main__':
    app.run(debug=True)  # Запуск сервера для тестов на твоем ПК
