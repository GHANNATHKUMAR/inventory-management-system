from Database import get_connection


class Products:

    @staticmethod
    def create_table():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                description TEXT,
                price DECIMAL(10,2),
                quantity INTEGER
            )
        """)

        conn.commit()
        cur.close()

    @staticmethod
    def insert_product(name, description, price, quantity):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO products(name, description, price, quantity) VALUES(%s,%s,%s,%s)",
            (name, description, price, quantity)
        )

        conn.commit()
        cur.close()

    @staticmethod
    def view_products():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM products")
        data = cur.fetchall()

        cur.close()
        return data

    @staticmethod
    def view_product_id(pid):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM products WHERE id=%s", (pid,))
        data = cur.fetchone()

        cur.close()
        return data

    @staticmethod
    def update_product(pid, name, description, price, quantity):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE products
            SET name=%s, description=%s, price=%s, quantity=%s
            WHERE id=%s
        """, (name, description, price, quantity, pid))

        conn.commit()
        cur.close()

    @staticmethod
    def delete_product(pid):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM products WHERE id=%s", (pid,))
        conn.commit()
        cur.close()
# Products().product_menu() 
