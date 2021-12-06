import psycopg2


_SQL_creat_table = """
DROP TABLE IF EXISTS orders; DROP TABLE IF EXISTS goods; DROP TABLE IF EXISTS goods_type;
CREATE TABLE goods_type ( goods_type_id INT GENERATED ALWAYS AS IDENTITY, goods_type_name VARCHAR(255) NOT NULL, PRIMARY KEY(goods_type_id) );
CREATE TABLE goods ( goods_id INT GENERATED ALWAYS AS IDENTITY, goods_name VARCHAR(255) NOT NULL, goods_type_id INT, PRIMARY KEY(goods_id), CONSTRAINT fk_goods FOREIGN KEY(goods_type_id) REFERENCES goods_type(goods_type_id) );
CREATE TABLE orders ( order_id INT GENERATED ALWAYS AS IDENTITY, user_name VARCHAR(255) NOT NULL, total INT, goods_id INT, PRIMARY KEY(order_id), CONSTRAINT fk_order FOREIGN KEY(goods_id) REFERENCES goods(goods_id) );
INSERT INTO goods_type(goods_type_name) VALUES('vegetables'), ('fruits'), ('cookie'); INSERT INTO goods(goods_name, goods_type_id) VALUES('tomato',1), ('potatoes',1), ('banana',2), ('orange',2), ('oreo',3), ('chocopie',3); INSERT INTO orders(user_name, total, goods_id) VALUES('John',2,1),
('John',1,3), ('Jane',3,5), ('Jane',3,6), ('David',10,2), ('David',5,5), ('David',3,1), ('Ann', 1,6);
"""

_SQL_request_top_category = """
SELECT goods_type.goods_type_name AS type_name, SUM(orders.total) as total
FROM orders
JOIN goods on orders.goods_id = goods.goods_id
JOIN goods_type on goods.goods_type_id = goods_type.goods_type_id
GROUP BY goods_type.goods_type_name
ORDER BY total DESC
LIMIT 1"""


def create_table(crt_cursor) -> None:
    """Create table"""
    crt_cursor.execute(_SQL_creat_table)


def get_top_category(crt_cursor) -> str:
    """Get one top category"""
    crt_cursor.execute(_SQL_request_top_category)
    result, *_ = cursor.fetchone()
    return result


if __name__ == '__main__':
    with psycopg2.connect(database="test", user="matt", password='2359', host="127.0.0.1") as conn:
        cursor = conn.cursor()
        create_table(cursor)

        category = get_top_category(cursor)
        print(f'Самая популярная категория товаров: {category}')
