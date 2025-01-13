import mysql.connector

# Database connection details
HOST = "smart-classroom-vision-system.infinityfreeapp.com"
USER = "if0_38095745"            # Your MySQL username
PASSWORD = "p4ygP0D0yJipq "        # Replace with your actual MySQL password
DATABASE = "if0_38095745_smart_classroom_vision_system"  # Your database name

def main():
    conn = None  # Initialize conn as None
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS text_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT NOT NULL
        );
        """
        cursor.execute(create_table_query)

        # Insert text data into the table
        text = input("Enter some text to save in the database: ")
        insert_query = "INSERT INTO text_data (content) VALUES (%s)"
        cursor.execute(insert_query, (text,))
        conn.commit()

        print("Text data saved successfully!")

        # Fetch and display all rows from the table
        cursor.execute("SELECT * FROM text_data")
        rows = cursor.fetchall()
        print("\nSaved Data:")
        for row in rows:
            print(f"ID: {row[0]}, Content: {row[1]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()

