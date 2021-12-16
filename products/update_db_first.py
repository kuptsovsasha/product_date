import sqlite3
from sqlite3 import Error
import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine

import json



# update data in bd


def update_table():
    filename="Даты"
    con=sqlite3.connect(filename+".db")
    wb=pd.read_excel(filename+'.xlsx')

    wb.to_sql('Даты',con)
    con.commit()
    con.close()

# create_table()

# Оновлення дат в базі данних



filename = "/home/sashakuptsov/Рабочий стол/Даты"
wb = pd.read_excel(filename + '.xlsx')
data = wb.to_dict(orient='list')




CO_code = data.get('CO_code')
name = data.get('name')
barcode = data.get('barcode')
expire_date = data.get('expire_date')
shop = data.get('shop')
department = data.get('department')
quantity = data.get('quantity')
list = []
for i in expire_date:
    list.append(pd.to_datetime(i).date())
expire_date = list
file = [CO_code, name, barcode, expire_date, shop, department, quantity]
print(file)
def update_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('/home/sashakuptsov/Рабочий стол/django/product date/db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")



        cursor.executemany('''INSERT or IGNORE  INTO products_item VALUES (?,?,?,?,?,?,?)''', tuple(zip(name, shop, department, CO_code, barcode, expire_date, quantity )))
        # cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")





# update_sqlite_table()