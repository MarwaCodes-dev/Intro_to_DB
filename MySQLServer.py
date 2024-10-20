import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        cursor = connection.cursor()
create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
 cursor.execute(create_db_query)
        print("Database 'alx_book_store' created successfully!")
    
except mysql.connector.Error as err:
        # Handle specific error messages
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid credentials provided!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist!")
        else:
            print(f"Failed to connect or create database: {err}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
