import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name,port):
    """Create a database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name,
            port=port
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def insert_record(connection, query, values):
    """Insert a record into the database."""
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
        print(f"Record inserted, ID: {cursor.lastrowid}")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def close_connection(connection):
    """Close the database connection."""
    if connection.is_connected():
        connection.close()
        print("The connection is closed")

def main():
    # Database credentials
    host = "192.168.1.60"
    user = "produkte"
    password = "SECRET"
    database = "ICT"
    port = 3306
    
    # SQL query for insertion
    sql_query = """
    INSERT INTO audi_tme ('AOI Ergebnis', 'AOI Datum',Seriennummer) 
    VALUES (%s, %s)
    WHERE Seriennummer = (%s)
    """
    
    # Data to be inserted
    AOI_data = ("Pass", "Date", "123456")
    
    # Create a connection to the database
    db_connection = create_connection(host, user, password, database,port)
    
    # Insert the record
    if db_connection:
        insert_record(db_connection, sql_query, AOI_data)
        
        # Close the connection
        close_connection(db_connection)

if __name__ == "__main__":
    main()
