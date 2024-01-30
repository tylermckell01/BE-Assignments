import os

import psycopg2

database_name = os.environ.get('DATABASE_NAME')


conn = psycopg2.connect(f"dbname={database_name}")
cursor = conn.cursor()

def create_all():
    print("Creating tables...")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS companies (
            company_id SERIAL PRIMARY KEY,
            company_name VARCHAR UNIQUE NOT NULL
        );
""")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS categories (
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR UNIQUE NOT NULL
        );
""")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS products (          
            product_id SERIAL PRIMARY KEY,
            company_id SERIAL REFERENCES companies(company_id),
            product_name VARCHAR NOT NULL UNIQUE,
            description VARCHAR,
            price FLOAT,
            active BOOLEAN DEFAULT true
        );
""")
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS products_categories_xref (
            product_id SERIAL REFERENCES products(product_id),
            category_id SERIAL REFERENCES categories(category_id)
        );
""")
    conn.commit()
