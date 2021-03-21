import psycopg2
from psycopg2 import Error
import datetime

try:
    connection = psycopg2.connect(user='postgres',
                                  password='postgres',
                                  host='127.0.0.1',
                                  port=5432,
                                  database='postgres'
                                  )

    cursor = connection.cursor()

    # Mobile tablosunu düşürüyoruz.

    tablo_drop_sorgu = 'drop table mobile'

    cursor.execute(tablo_drop_sorgu)

    connection.commit()

    print('Mobile tablosu drop edildi')

    # Mobile tablosu oluşturuyoruz.

    tablo_olustur_sorgu = '''create table mobile
    (id int primary key not null,
     model text not null,
     price real)'''

    cursor.execute(tablo_olustur_sorgu)

    connection.commit()

    print('Mobile tablosu oluşturuldu.')

    # Önce insert deniyoruz.

    insert_sorgu1 = "insert into mobile values(1, 'IPhone Telefon', 7000)"
    insert_sorgu2 = "insert into mobile values(2, 'Samsung Telefon', 9000)"
    insert_sorgu3 = "insert into mobile values(3, 'Vestel Telefon', 5000)"
    insert_sorgu4 = "insert into mobile values(4, 'Aselsan Telefon', 15000)"
    insert_sorgu5 = "insert into mobile values(5, 'GM Telefon', 3000)"

    cursor.execute(insert_sorgu1)
    cursor.execute(insert_sorgu2)
    cursor.execute(insert_sorgu3)
    cursor.execute(insert_sorgu4)
    cursor.execute(insert_sorgu5)

    connection.commit()

    # Sonra Select deneyelim.

    select_sorgu = 'select * from mobile'

    cursor.execute(select_sorgu)

    data = cursor.fetchall()

    print('Data:', data)

    print(data[0])
    print(data[0][1])

    # Update deniyoruz.

    update_sorgu = '''update mobile
                    set price=51000
                    where id=3'''

    cursor.execute(update_sorgu)

    sonuc = cursor.rowcount

    connection.commit()

    if sonuc > 0:
        print('Update başarılı')
    else:
        print('Update başarısız', sonuc)

    # Son olarak, delete deniyoruz.

    delete_sorgu = 'delete from mobile where id=5'

    cursor.execute(delete_sorgu)

    connection.commit()

    if cursor.rowcount > 0:
        print('Silme başarılı')
    else:
        print('Silme başarısız')

    #item tablosu düşür.

    item_drop_sorgu='drop table item'

    cursor.execute(item_drop_sorgu)

    connection.commit()

    print("İtem tablosu düşürüldü")

    # Item tablosu oluşturuyoruz.

    item_create_sorgu = '''CREATE TABLE item ( 
	item_id serial NOT NULL PRIMARY KEY, 
	item_name VARCHAR (100) NOT NULL, 
	purchase_time timestamp NOT NULL,
	price NUMERIC(7,2) NOT NULL
    )
    '''
    cursor.execute(item_create_sorgu)
    print('İtem Tablosu Oluşturuldu')

    #item TABLOSUNA insert sorgusu oluşturalım

    item_insert_sorgu='insert into item VALUES (%s, %s, %s, %s)'
    simdi=datetime.datetime.now()

    item_tuple=(12,'Keyboard',simdi,150)

    cursor.execute(item_insert_sorgu,item_tuple)
    connection.commit()

    print('item başarıyla eklendi')



except (Exception, Error) as e:
    print('Hata oluştu', e)

finally:
    if connection:
        cursor.close()
        connection.close()
        print('Bağlantı kapatıldı')
