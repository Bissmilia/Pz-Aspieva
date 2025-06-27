# Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения
# товаров на оптовой базе. Таблица Товары должна содержать следующие данные: Код
# товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
# товара на складе, Единицы измерения, Оптовая цена.

import sqlite3 as sq

# Данные для таблицы Товары
products_d = [
    (1, 'Молоко', 'Магазин А', 20, 150, 'литры', 45.0),
    (2, 'Хлеб', 'Магазин Б', 30, 200, 'штуки', 25.0),
    (3, 'Сахар', 'Магазин А', 15, 500, 'килограммы', 40.0),
    (4, 'Яйца', 'Магазин В', 10, 300, 'штуки', 69.0),
    (5, 'Кофе', 'Магазин Б', 25, 100, 'килограммы', 350.0),
    (6, 'Чай', 'Магазин А', 12, 5, 'килограммы', 60.0),
    (7, 'Соль', 'Магазин В', 5, 400, 'килограммы', 15.0),
    (8, 'Курица', 'Магазин А', 8, 200, 'килограммы', 600.0),
    (9, 'Пельмени', 'Магазин Б', 20, 250, 'килограммы', 200.0),
    (10, 'Рис', 'Магазин В', 18, 300, 'килограммы', 70.0)
]

# Создаем и заполняем базу данных
with sq.connect('optovaya_baza.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS products")
    cur.execute("""CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name_pr TEXT NOT NULL,
        name_shop TEXT NOT NULL,
        zayavki INTEGER NOT NULL,
        count INTEGER NOT NULL,
        unit TEXT NOT NULL,
        price REAL NOT NULL
    )""")
    cur.executemany("INSERT INTO products VALUES(?, ?, ?, ?, ?, ?, ?)", products_d)


    print("\nВсе товары:")
    cur.execute("SELECT * FROM products")
    for row in cur.fetchall():
        print(row)

    print("\nТовары в Магазине А:")
    cur.execute("SELECT * FROM products WHERE name_shop = 'Магазин А'")
    for row in cur.fetchall():
        print(row)

    print("\nТовары с количеством на складе менее 10:")
    cur.execute("SELECT * FROM products WHERE count < 10")
    for row in cur.fetchall():
        print(row)


    cur.execute("DELETE FROM products WHERE unit = 'литры'")
    print("\nТовары измеряющиеся в литрах удалены")

    cur.execute("DELETE FROM products WHERE id = 7")
    print("Товар с кодом 7 удалён")

    cur.execute("DELETE FROM products WHERE name_pr = 'Чай'")
    print("Товар 'Чай' удалён")

    cur.execute("UPDATE products SET price = price * 1.05 WHERE name_shop = 'Магазин Б'")
    print("\nОптовые цены магазина Б увеличены на 5%")

    cur.execute("UPDATE products SET name_pr = 'Гречка' WHERE name_pr = 'Рис'")
    print("Товар 'Рис' заменен на 'Гречка'")

    cur.execute("UPDATE products SET count = count * 2 WHERE name_shop = 'Магазин А'")
    print("Увеличили количество продуктов на складе в два раза")


    print('\nТаблица после изменений:')
    for row in cur.execute('SELECT * FROM products'):
        print(row)
