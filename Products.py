from Database import conn


class Products:
    def __init__(self):
        pass
    @staticmethod
    def create_table():
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                quantity INTEGER NOT NULL
            )
        """)
        conn.commit()
        cur.close()

    @staticmethod
    def insert_product(name, description, price, quantity):
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO products(name, description, price, quantity) VALUES(%s, %s, %s, %s)",
            (name, description, price, quantity)
        )
        conn.commit()
        cur.close()

    @staticmethod
    def update_product(product_id, name=None, description=None, price=None, quantity=None):
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM products WHERE id = %s""",
            (product_id,)
        )

        product_data = cur.fetchone()

        if not product_data:
            print("Product not found with id", product_id)
            cur.close()
            return

        update_fields = []

        if name:
            update_fields.append(f"name='{name}'")

        if description:
            update_fields.append(f"description='{description}'")

        if price:
            update_fields.append(f"price={price}")

        if quantity:
            update_fields.append(f"quantity={quantity}")

        update_query = f"""
            UPDATE products
            SET {', '.join(update_fields)}
            WHERE id = %s
        """

        cur.execute(update_query, (product_id,))
        conn.commit()
        cur.close()

    @staticmethod
    def delete_product(product_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM products WHERE id = %s",
            (product_id,)
        )
        conn.commit()
        cur.close()

    @staticmethod
    def view_products():
        cur = conn.cursor()
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()
        cur.close()
        return products
    
    @staticmethod
    def view_product_id(product_id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cur.fetchone()
        cur.close()
        return product
 
                    

    @staticmethod
    def product_menu():
        while True:
            print("\n1. Create Table")
            print("2. Insert Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. View Products")
            print("6. View Product by ID")
            print("0. Exit Product ")

            choice = input("Enter your choice: ")

            if choice == "1":
                Products().create_table()
                print("Product table created successfully")

            elif choice == "2":
                name = input("Enter product name: ")
                description = input("Enter product description: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                Products().insert_product(name, description, price, quantity)
                print("Product inserted successfully")

            elif choice == "3":
                product_id = (input("Enter product id to update: "))
                name = input("Enter product name: ")
                description = input("Enter product description: ")
                price = (input("Enter product price: "))
                quantity = (input("Enter product quantity: "))
                Products().update_product(product_id, name, description, price, quantity)
                print("Product updated successfully")
            elif choice == "4":
                product_id = int(input("Enter product id to delete: "))
                Products().delete_product(product_id)
                print("Product deleted successfully")

            elif choice == "5":
                products = Products().view_products()

                for p in products:
                    print(p)

            elif choice == "0":
                print("Exiting product menu...")
                break

            else:
                print("Invalid choice. Please try again.")

# Products().product_menu() 