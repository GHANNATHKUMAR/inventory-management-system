import psycopg2;

def connection() : 
    con = psycopg2.connect(
        host="localhost",
        database="ecommerce",
        user="postgres",
        password="Ghannath@87",
        port="5432",
    )
    if con : 
        print("<<<<<<<<<<connection established successfully <<<<<<<<<<<<")
    else: 
        print("<<<<<<<<<<connection failed <<<<<<<<<<<<")
    return con

conn=connection()

