from Database import get_connection


class SaleItems:

    @staticmethod
    def create_table():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS sale_items(
                id SERIAL PRIMARY KEY,
                sale_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                price NUMERIC(10,2)
            )
        """)

        conn.commit()
        cur.close()

    @staticmethod
    def insert_item(sale_id, product_id, qty, price):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO sale_items(sale_id, product_id, quantity, price) VALUES(%s,%s,%s,%s)",
            (sale_id, product_id, qty, price)
        )

        conn.commit()
        cur.close()
