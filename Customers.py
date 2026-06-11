from Database import get_connection


class customer:

    def __init__(self):
        pass

    @staticmethod
    def create_table():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                contact VARCHAR(10) NOT NULL
            )
        """)

        conn.commit()
        cur.close()

    @staticmethod
    def insert_customer(name, contact):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO customers(name, contact) VALUES(%s, %s)",
            (name, contact)
        )

        conn.commit()
        cur.close()

    @staticmethod
    def update_customer(customer_id, customer_name=None, customer_contact=None):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM customers WHERE id = %s",
            (customer_id,)
        )

        customer_data = cur.fetchone()

        if not customer_data:
            print("Customer not found with id", customer_id)
            cur.close()
            return

        update_fields = []

        if customer_name:
            update_fields.append(f"name='{customer_name}'")

        if customer_contact:
            update_fields.append(f"contact='{customer_contact}'")

        update_query = f"""
            UPDATE customers
            SET {', '.join(update_fields)}
            WHERE id = %s
        """

        cur.execute(update_query, (customer_id,))
        conn.commit()
        cur.close()

    @staticmethod
    def delete_customer(customer_id):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM customers WHERE id = %s",
            (customer_id,)
        )

        conn.commit()
        cur.close()

    @staticmethod
    def get_all_customers():
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM customers")
        customers = cur.fetchall()

        cur.close()
        return customers

    @staticmethod
    def customer_menu():
        while True:
            print("\n1. Create Table")
            print("2. Insert Customer")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. View Customers")
            print("0. Exit Customer ")

            choice = input("Enter your choice: ")

            if choice == "1":
                customer.create_table()
                print("Customer table created successfully")

            elif choice == "2":
                name = input("Enter customer name: ")
                contact = input("Enter customer contact: ")
                customer.insert_customer(name, contact)
                print("Customer inserted successfully")

            elif choice == "3":
                customer_id = input("Enter customer id to update: ")
                name = input("Enter customer name: ")
                contact = input("Enter customer contact: ")

                customer.update_customer(customer_id, name, contact)
                print("Customer updated successfully")

            elif choice == "4":
                customer_id = int(input("Enter customer id to delete: "))
                customer.delete_customer(customer_id)
                print("Customer deleted successfully")

            elif choice == "5":
                customers = customer.get_all_customers()
                for c in customers:
                    print(c)

            elif choice == "0":
                print("Exiting customer menu...")
                break

            else:
                print("Invalid choice. Please try again.")
