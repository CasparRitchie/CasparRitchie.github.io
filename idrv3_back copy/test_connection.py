from db_utils import create_connection

def test_connection():
    try:
        cnx, cursor = create_connection()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print("Successfully connected! Tables in the database:", tables)
    except Exception as e:
        print("Error while connecting:", e)
    finally:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    test_connection()
