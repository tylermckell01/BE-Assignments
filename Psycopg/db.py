import os

import psycopg2

database_name = os.environ.get('DATABASE_NAME')


conn = psycopg2.connect(f"dbname={database_name}")
cursor = conn.cursor()

def create_all():
    print("Creating tables...")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS products (          
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR NOT NULL UNIQUE,
            description VARCHAR,
            price FLOAT,
            active BOOLEAN DEFAULT true
        );
""")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS companies (
            company_id UUID4 PRIMARY KEY,
            company_name VARCHAR UNIQUE NOT NULL
        )
""")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS products_categories_xref (
            product_id UUID4,
            category_id UUID4
        )
""")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS categories (
            category_id UUID4 PRIMARY KEY,
            category_name VARCHAR UNIQUE NOT NULL
        )
""")
    conn.commit()
