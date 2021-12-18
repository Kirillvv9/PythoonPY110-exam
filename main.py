import json


def main():
    """Основная функция: выполняет прогон всех модулей"""

    global conf
    import conf
    c = conf.MODEL

    global random
    import random

    # выводим название книги из текстового файла
    def title():
        contents = []

        with open(" books.txt") as rnd:
            for line in rnd:
                line = line.strip()
                contents.append(line)
        return contents[random.randint(0, len(contents) - 1)]

        # выводим случайное число (год)
    def year():
        from random import randint
        return randint(1900, 2000)

        # выводим случайное число (страницы)
    def pages():
        from random import randint
        return randint(100, 200)

        # выводим случайный книжный номер
    def isbn():
        from faker import Faker
        fake = Faker()
        return fake.isbn13()

        # выводим случайный рейтинг
    def rating():
        return round(random.uniform(1, 5),2)

        # выводим случайную цену
    def price():
        return round(random.uniform(500, 3000),2)

        # выводим случайных авторов
    def authors():
        from faker import Faker
        fake = Faker(locale="ru_RU")
        return fake.name()

    a = dict(model=c,
             title=title(),
             year=year(),
             pages=pages(),
             isbn13=isbn(),
             rating=rating(),
             price=price(),
             authors=authors())

    json_data = json.dumps(a, indent=4, ensure_ascii=False)
    with open("knigi.json", "w") as file:
        file.writelines(json_data)


if __name__ == '__main__':
    main()
