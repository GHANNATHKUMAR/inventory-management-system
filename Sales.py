from Database import conn


class Sales:
    def __init__(self):
        pass
    @staticmethod
    def create_table():
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sales(
                id SERIAL PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                date DATE NOT NULL,
                total_amount DECIMAL(10, 2) NOT NULL,
                CONSTRAINT fk_sales_customer FOREIGN KEY(customer_id) 
                    REFERENCES customers(id) 
                    ON DELETE CASCADE
            )
        """)
        conn.commit()
        cur.close()

    @staticmethod
    def insert_sale(customer_id, date, total_amount):
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO sales(customer_id, date, total_amount) VALUES(%s, %s, %s)",
            (customer_id, date, total_amount)
        )
        conn.commit()
        cur.close()


    @staticmethod
    def view_sales():
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales")
        sales = cur.fetchall()
        cur.close()
        return sales
    

    @staticmethod
    def update_sales(sale_id, customer_id=None, date=None, total_amount=None):
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM sales WHERE id = %s""",
            (sale_id,)
        )

        sale_data = cur.fetchone()

        if not sale_data:
            print("Sale not found with id", sale_id)
            cur.close()
            return

        update_fields = []

        if customer_id is not None:
            update_fields.append(f"customer_id={customer_id}")

        if date is not None:
            update_fields.append(f"date='{date}'")

        if total_amount is not None:
            update_fields.append(f"total_amount={total_amount}")

        update_query = f"""
            UPDATE sales
            SET {', '.join(update_fields)}
            WHERE id = %s
        """ 

        cur.execute(update_query, (sale_id,))
        conn.commit()
        cur.close()

    @staticmethod
    def delete_sale(sale_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM sales WHERE id = %s",
            (sale_id,)
        )
        conn.commit()
        cur.close()

    @staticmethod
    def generate_bill(sale_id):
        cur = conn.cursor()
        cur.execute(
            """
            SELECT quantity, price
            FROM sale_items
            WHERE sale_id = %s
            """,
            (sale_id,)
        )
        sale_items = cur.fetchall()
        cur.close()

        total_amount = sum(item[0] * float(item[1]) for item in sale_items)
        return total_amount

    @staticmethod
    def view_sale_id(sale_id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales WHERE id = %s", (sale_id,))
        sale = cur.fetchone()
        cur.close()
        return sale
    @staticmethod 
    def total_sales_by_date(startdate, enddate):
        cur=conn.cursor()
        cur.execute(
            """SELECT SUM(total_amount) FROM sales WHERE date BETWEEN %s and %s""" , 
            (startdate,enddate,)
        )
        total_sales=cur.fetchone()
        cur.close()
        return total_sales
    
    @staticmethod
    def get_top_selling_products() :
        cur=conn.cursor()
        cur.execute(
            """ 
            SELECT prodcut_id , SUM(quantity)  AS total_quantity FROM sale_items GROUP BY poduct_id ORDER BY total_quantity DESC LIMIT 5"""
        )
        top_products=cur.fetchall()
        cur.close()
        return top_products
    
    @staticmethod 
    def get_sales_by_customer(customer_id) : 
        cur=conn.cursor()
        cur.execute(
            """SELECT * FROM sales WHERE customer_id= %s""",
            (customer_id,)
        )
        sales=cur.fetchall()
        cur.close()
        return sales 
    
    @staticmethod
    def sales_menu():
        while True:
            print("\n1. Create Table")
            print("2. Insert Table ")
            print("3. Update sales")
            print("4. Delete sales")
            print("5. View sales")
            print("6. View sales by ID")
            print("7. Generate Bill ")
            print("8. Total Sales by Date")
            print("9. Get Top 5 Selling Products")
            print("10. Get Sales by Customer")
            print("0. Exit Sales ")

            choice = input("Enter your choice: ")

            if choice == "1":
                Sales().create_table()
                print("sales table created successfully")

            elif choice == "2":
                customer_id=input("Enter customer id : ")
                date=input("Enter date (YYYY-MM-DD) : ")
                total_amount=input("Enter total amount : ")
                Sales().insert_sale(customer_id , date , total_amount)
                print("sales  inserted successfully")

            elif choice == "3":
                sale_id = (input("Enter sale id to update: "))
                customer_id = input("Enter customer id: ")
                date = input("Enter date (YYYY-MM-DD): ")
                total_amount = (input("Enter total amount: "))
                Sales().update_sale(sale_id, customer_id, date, total_amount)
                print("Sale updated successfully")

            elif choice == "4":
                sale_id = int(input("Enter sale id to delete: "))
                Sales().delete_sale(sale_id)
                print("Sale deleted successfully")
            elif choice == "5":
                sales = Sales().view_sales()
                for s in sales:
                    print(s)

            elif choice == "6":
                sale_id = (input("Enter sale id to view: "))
                sale = Sales().view_sale_id(sale_id)
                print(sale)
            elif choice=="7" :
                sale_id=(input("Enter sale id to generate bill: "))
                generate_bill=Sales().generate_bill(sale_id)
                print("Total Amount: ", generate_bill)
            elif choice=="8" : 
                startdate=input("Enter start date (YYYY-MM-DD) : ")
                enddate=input("Enter end date (YYYY-MM-DD) : ")
                total_sales=Sales().total_sales_by_date(startdate, enddate)
                print("Total Sales: ", total_sales)
            elif choice=="9" : 
                top_products=Sales().get_top_selling_products()
                print("Top 5 selling products .. ")
                for p in top_products:
                    print(p)
            elif choice=="10" :
                customer_id=(input("Enter customer id: "))
                sales=Sales().get_sales_by_customer(customer_id)
                print("Sales for customer ", customer_id, ":")
                for s in sales:
                    print(s)
            elif choice == "0":
                print("Exiting sales menu...")
                break

            else:
                print("Invalid choice. Please try again.")


# Sales().sales_menu() 