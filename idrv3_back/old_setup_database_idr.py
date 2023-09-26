# this is not used but it seems quite a nice way of making the database
# KEEP IT FOR LATER
import mysql.connector

def setup_database():
    # Database configuration
    config = {
        'user': 'root',
        'password': 'YOUR_PASSWORD',
        'host': '127.0.0.1',
        'raise_on_warnings': True
    }

    # Create a new MySQL connection
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS YourDatabaseName;")
        print("Database created successfully.")

        # Use the database
        cursor.execute("USE YourDatabaseName;")
        
        # Now, add all the table creation and data insertion SQL commands
        commands = [
            # ... Your table creation commands go here ...

            # Modify the SIRET column to VARCHAR
            "ALTER TABLE clients MODIFY COLUMN client_siret VARCHAR(14);",

            # ... Your data insertion commands go here ...
        ]

        for command in commands:
            cursor.execute(command)

        print("Tables created and data inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()
        cnx.close()

# Call the function
setup_database()
