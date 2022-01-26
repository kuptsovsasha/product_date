import psycopg2
import pandas as pd
from pandas.io.json import json_normalize
from sqlalchemy import create_engine
import datetime

filename = "/home/sashakuptsov/Рабочий стол/Даты"
wb = pd.read_excel(filename + '.xlsx')

engine = create_engine('postgresql://postgres:postgres@localhost:5432/product')

frame = pd.DataFrame(wb,
                     columns=['name', 'department', 'CO_code', 'barcode', 'expire_date', 'quantity', 'created_at', 'shop_id'])

insert = frame.to_sql(name='products_item', con=engine, index=False, if_exists='append')

print(frame)

# CO_code = data.get('CO_code')
# name = data.get('name')
# barcode = data.get('barcode')
# expire_date = data.get('expire_date')
# shop = data.get('shop')
# department = data.get('department')
# quantity = data.get('quantity')
