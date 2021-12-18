import json


def main():
    i = 1
    while i < 101:
        import conf
        c = conf.model()

        # выводим название книги из текстового файла

        import random
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

        fake = Faker()
        s = fake.name()  # locale="ru_RU" в скобки, чтобы было по-русски. Не разобрался как закодировать надо.

        a = dict(model=c,
                 title=b,
                 year=d,
                 pages=e,
                 isbn13=f,
                 rating=g,
                 price=m,
                 authors=s)

        print(json.dumps(a, indent=4))

        i += 1


if __name__ == '__main__':
    main()
