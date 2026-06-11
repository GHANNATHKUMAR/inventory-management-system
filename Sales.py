from Database import get_connection


class Sales:

    @staticmethod
    def create_table():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS sales(
                id SERIAL PRIMARY KEY,
                customer_id INTEGER,
                date DATE,
                total_amount DECIMAL(10,2)
            )
        """)

        conn.commit()
        cur.close()

    @staticmethod
    def insert_sale(customer_id, date, total):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO sales(customer_id, date, total_amount) VALUES(%s,%s,%s)",
            (customer_id, date, total)
        )

        conn.commit()
        cur.close()

    @staticmethod
    def view_sales():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM sales")
        data = cur.fetchall()

        cur.close()
        return data

    @staticmethod
    def delete_sale(sid):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM sales WHERE id=%s", (sid,))
        conn.commit()
        cur.close()


# Sales().sales_menu() 
