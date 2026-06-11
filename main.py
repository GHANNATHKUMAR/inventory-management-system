from Database import get_connection
from Customers import customer 
from Products import Products
from Sales import Sales 
conn=get_connection()

def main_menu():
    while True : 
        print("1. Customer Management ")
        print("2. Product Management ")
        print("3. Sales Management ")
        print("4. Exit Application ")
        choice=input("Select an option: ")
        if choice=="1": 
            customer().customer_menu()
        elif choice=="2" : 
            Products().product_menu()
        elif choice=="3":
            Sales().sales_menu()
        elif choice=="4":
            print("Exiting Application...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
    main_menu()
