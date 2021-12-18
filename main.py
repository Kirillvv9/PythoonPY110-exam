import json


def main():
    """Основная функция: выполняет прогон всех модулей"""

    for i in range(1, 100, 1):

        global conf
        import conf
        c = conf.MODEL

        global random
        import random

        # выводим название книги из текстового файла

        contents = []

        with open(" books.txt") as rnd:
            for line in rnd:
                line = line.strip()
                contents.append(line)
                b = contents[random.randint(0, len(contents) - 1)]

        # выводим случайное число (год)
        from random import randint
        d = randint(1900, 2000)

        # выводим случайное число (страницы)
        from random import randint
        e = randint(100, 200)

        # выводим случайный книжный номер
        from faker import Faker
        fake = Faker()
        f = fake.isbn13()

        # выводим случайный рейтинг
        g = round(random.uniform(1, 5),2)

        # выводим случайную цену
        m = round(random.uniform(500, 3000),2)

        # выводим случайных авторов

        fake = Faker(locale="ru_RU")
        s = fake.name()

        a = dict(model=c,
                 title=b,
                 year=d,
                 pages=e,
                 isbn13=f,
                 rating=g,
                 price=m,
                 authors=s)

        json_data = json.dumps(a, indent=4, ensure_ascii=False)
        with open("knigi.json", "a") as file:
            file.writelines(json_data)


if __name__ == '__main__':
    main()
