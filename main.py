
import sqlite3

conn = sqlite3.connect('electronic_magazin.db')
cursor = conn.cursor()

#cursor.execute('''INSERT INTO products (name, category, price)
#VALUES ('iPhone 13', 'смартфони', 999),
       #('Samsung Galaxy S22', 'смартфони', 899),
       #('OnePlus 10 Pro', 'смартфони', 899);''')

#cursor.execute('''INSERT INTO products (name, category, price)
#VALUES ('MacBook Air', 'ноутбуки', 1199),
       #('Dell XPS 13', 'ноутбуки', 999),
       #('HP Spectre x360', 'ноутбуки', 1099);''')

#cursor.execute('''INSERT INTO products (name, category, price)
#VALUES ('iPad Pro', 'планшети', 799),
       #('Samsung Galaxy Tab S8', 'планшети', 699),
       #('Microsoft Surface Pro 8', 'планшети', 899);''')


#cursor.execute('''INSERT INTO customers (first_name, last_name, email)
#VALUES ('Іван', 'Петров', 'ivan@example.com'),
       #('Марія', 'Сидорова', 'maria@example.com'),
       #('Петро', 'Ковальов', 'petro@example.com');
       #''')

#cursor.execute('''INSERT INTO orders (customer_id, product_id, quantity, order_date)
#VALUES (1, 1, 2, '2024-05-04'),
       #(2, 3, 1, '2024-05-04'),
       #(3, 2, 3, '2024-05-05')
#''')

#cursor.execute('''SELECT SUM(products.price * orders.quantity) AS total_sales
#FROM orders
#JOIN products ON orders.product_id = products.product_id;
#''')

summa = cursor.fetchall()
print(summa[0][0])

conn.commit()
conn.close()